from datetime import datetime, timezone
import re
from typing import List
from app.parsers.base_parser import BaseLogParser
from app.schemas.log_event import NormalizedLogEvent


class ApacheAccessLogParser(BaseLogParser):
    source_type = "apache"

    # Standard Apache Combined Log Format:
    # %h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"
    APACHE_REGEX = re.compile(
        r'^(?P<ip>\S+)\s+(?P<ident>\S+)\s+(?P<user>\S+)\s+\[(?P<timestamp>.*?)\]\s+"(?P<request>.*?)"\s+(?P<status>\d{3})\s+(?P<bytes>\S+)(?:\s+"(?P<referrer>.*?)"\s+"(?P<user_agent>.*?)")?'
    )

    # Common Web Attack Heuristics
    SQL_INJECTION_REGEX = re.compile(r"(union\s+select|select.*from|or\s+['\d]=['\d]|--|/\*|waitfor\s+delay)", re.IGNORECASE)
    PATH_TRAVERSAL_REGEX = re.compile(r"(\.\./\.\./|etc/passwd|winnt/system32)", re.IGNORECASE)
    XSS_REGEX = re.compile(r"(<script|javascript:|document\.cookie|onload=)", re.IGNORECASE)

    def _parse_timestamp(self, ts_str: str) -> datetime:
        try:
            # Format: 11/Sep/2026:10:14:20 +0000
            return datetime.strptime(ts_str, "%d/%b/%Y:%H:%M:%S %z")
        except Exception:
            return datetime.now(timezone.utc)

    def parse(self, raw_content: str) -> List[NormalizedLogEvent]:
        events: List[NormalizedLogEvent] = []
        for line in raw_content.splitlines():
            line = line.strip()
            if not line:
                continue

            match = self.APACHE_REGEX.match(line)
            if not match:
                continue

            data = match.groupdict()
            timestamp = self._parse_timestamp(data["timestamp"])
            source_ip = data["ip"]
            user = data["user"] if data["user"] != "-" else None
            request = data["request"]
            status_code = int(data["status"])
            user_agent = data.get("user_agent", "")

            event_type = "HTTP_REQUEST"
            severity_hint = "INFO"

            # Detect specific web attacks
            if self.SQL_INJECTION_REGEX.search(request) or "sqlmap" in user_agent.lower():
                event_type = "SQL_INJECTION_ATTEMPT"
                severity_hint = "CRITICAL"
            elif self.PATH_TRAVERSAL_REGEX.search(request):
                event_type = "PATH_TRAVERSAL_ATTEMPT"
                severity_hint = "HIGH"
            elif (
                self.XSS_REGEX.search(request)
                or (data.get("referrer") and self.XSS_REGEX.search(data["referrer"]))
                or (user_agent and self.XSS_REGEX.search(user_agent))
            ):
                event_type = "XSS_ATTEMPT"
                severity_hint = "HIGH"
            elif status_code in (401, 403):
                severity_hint = "WARNING"

            events.append(
                NormalizedLogEvent(
                    timestamp=timestamp,
                    source_type=self.source_type,
                    source_ip=source_ip,
                    user=user,
                    event_type=event_type,
                    severity_hint=severity_hint,
                    raw_message=line,
                    metadata={
                        "request": request,
                        "status_code": status_code,
                        "user_agent": user_agent,
                        "bytes": data.get("bytes"),
                    },
                )
            )
        return events
