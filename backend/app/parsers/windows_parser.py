import json
from datetime import datetime, timezone
from typing import Any, Dict, List
from app.parsers.base_parser import BaseLogParser
from app.schemas.log_event import NormalizedLogEvent


class WindowsEventParser(BaseLogParser):
    source_type = "windows"

    EVENT_MAPPING = {
        4625: ("FAILED_LOGIN", "WARNING"),
        4624: ("SUCCESSFUL_LOGIN", "INFO"),
        4672: ("PRIVILEGE_ASSIGNED", "ALERT"),
        4720: ("ACCOUNT_CREATED", "WARNING"),
        4726: ("ACCOUNT_DELETED", "WARNING"),
        7045: ("SERVICE_INSTALLED", "ALERT"),
    }

    def _parse_event_dict(self, item: Dict[str, Any]) -> NormalizedLogEvent:
        event_id = item.get("EventID")
        time_created_str = item.get("TimeCreated")

        if time_created_str:
            try:
                # Handle ISO format like 2026-09-11T14:22:01.120Z
                cleaned_time = time_created_str.replace("Z", "+00:00")
                timestamp = datetime.fromisoformat(cleaned_time)
            except Exception:
                timestamp = datetime.now(timezone.utc)
        else:
            timestamp = datetime.now(timezone.utc)

        computer = item.get("Computer")
        event_data = item.get("EventData", {})

        mapped = self.EVENT_MAPPING.get(event_id, ("WINDOWS_EVENT", "INFO"))
        event_type, severity_hint = mapped

        user = event_data.get("TargetUserName") or event_data.get("SubjectUserName")
        source_ip = event_data.get("IpAddress")
        if source_ip in ("-", "127.0.0.1", "::1", None):
            source_ip = None

        source_port = None
        if event_data.get("IpPort") and event_data["IpPort"] != "-":
            try:
                source_port = int(event_data["IpPort"])
            except ValueError:
                pass

        return NormalizedLogEvent(
            timestamp=timestamp,
            source_type=self.source_type,
            source_ip=source_ip,
            destination_ip=computer,
            source_port=source_port,
            user=user,
            event_type=event_type,
            severity_hint=severity_hint,
            raw_message=json.dumps(item),
            metadata={"EventID": event_id, **event_data},
        )

    def parse(self, raw_content: str) -> List[NormalizedLogEvent]:
        events: List[NormalizedLogEvent] = []
        raw_content = raw_content.strip()
        if not raw_content:
            return events

        # Try parsing as JSON array
        try:
            data = json.loads(raw_content)
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        events.append(self._parse_event_dict(item))
                return events
            elif isinstance(data, dict):
                events.append(self._parse_event_dict(data))
                return events
        except json.JSONDecodeError:
            pass

        # Fallback: Line-by-line JSON objects (NDJSON)
        for line in raw_content.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
                if isinstance(item, dict):
                    events.append(self._parse_event_dict(item))
            except json.JSONDecodeError:
                continue

        return events
