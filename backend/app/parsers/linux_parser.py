from datetime import datetime, timezone
import re
from typing import List, Optional
from app.parsers.base_parser import BaseLogParser
from app.schemas.log_event import NormalizedLogEvent


class LinuxSyslogParser(BaseLogParser):
    source_type = "linux_syslog"

    # Standard RFC 3164 Syslog header: "Oct 14 03:14:15 hostname process[pid]: message"
    SYSLOG_LINE_REGEX = re.compile(
        r"^(?P<month>[A-Za-z]{3})\s+(?P<day>\d+)\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<hostname>\S+)\s+(?P<process>[A-Za-z0-9_\-\./]+)(?:\[(?P<pid>\d+)\])?:\s+(?P<message>.*)$"
    )

    # Patterns within SSH and sudo messages
    SSH_FAILED_REGEX = re.compile(
        r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3}) port (?P<port>\d+)"
    )
    SSH_ACCEPTED_REGEX = re.compile(
        r"Accepted password for (?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3}) port (?P<port>\d+)"
    )
    SUDO_FAILURE_REGEX = re.compile(
        r"authentication failure;.*user=(?P<user>\S+)"
    )
    SUDO_ATTEMPTS_REGEX = re.compile(
        r"(?P<attempts>\d+) incorrect password attempts ; .* USER=(?P<target_user>\S+) ; COMMAND=(?P<command>.*)"
    )

    MONTH_MAP = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    def _parse_timestamp(self, month_str: str, day_str: str, time_str: str) -> datetime:
        now = datetime.now(timezone.utc)
        month = self.MONTH_MAP.get(month_str, 1)
        day = int(day_str)
        hour, minute, second = map(int, time_str.split(":"))
        return datetime(year=now.year, month=month, day=day, hour=hour, minute=minute, second=second, tzinfo=timezone.utc)

    def parse(self, raw_content: str) -> List[NormalizedLogEvent]:
        events: List[NormalizedLogEvent] = []
        for line in raw_content.splitlines():
            line = line.strip()
            if not line:
                continue

            match = self.SYSLOG_LINE_REGEX.match(line)
            if not match:
                continue

            groups = match.groupdict()
            event_time = self._parse_timestamp(groups["month"], groups["day"], groups["time"])
            hostname = groups["hostname"]
            process = groups["process"]
            msg = groups["message"]

            source_ip: Optional[str] = None
            source_port: Optional[int] = None
            user: Optional[str] = None
            event_type = "SYSTEM_LOG"
            severity_hint = "INFO"
            metadata = {"hostname": hostname, "process": process, "pid": groups.get("pid")}

            # Check SSH Failed Password
            ssh_failed = self.SSH_FAILED_REGEX.search(msg)
            if ssh_failed:
                user = ssh_failed.group("user")
                source_ip = ssh_failed.group("ip")
                source_port = int(ssh_failed.group("port"))
                event_type = "FAILED_LOGIN"
                severity_hint = "WARNING"
            elif self.SSH_ACCEPTED_REGEX.search(msg):
                ssh_acc = self.SSH_ACCEPTED_REGEX.search(msg)
                user = ssh_acc.group("user")
                source_ip = ssh_acc.group("ip")
                source_port = int(ssh_acc.group("port"))
                event_type = "SUCCESSFUL_LOGIN"
                severity_hint = "INFO"
            elif self.SUDO_ATTEMPTS_REGEX.search(msg):
                sudo_match = self.SUDO_ATTEMPTS_REGEX.search(msg)
                event_type = "PRIVILEGE_ESCALATION_ATTEMPT"
                severity_hint = "CRITICAL"
                metadata["target_user"] = sudo_match.group("target_user")
                metadata["command"] = sudo_match.group("command")
            elif self.SUDO_FAILURE_REGEX.search(msg):
                event_type = "AUTH_FAILURE"
                severity_hint = "ALERT"

            events.append(
                NormalizedLogEvent(
                    timestamp=event_time,
                    source_type=self.source_type,
                    source_ip=source_ip,
                    destination_ip=hostname,
                    source_port=source_port,
                    user=user,
                    event_type=event_type,
                    severity_hint=severity_hint,
                    raw_message=line,
                    metadata=metadata,
                )
            )
        return events
