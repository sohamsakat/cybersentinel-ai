import csv
from datetime import datetime, timezone
import io
from typing import List
from app.parsers.base_parser import BaseLogParser
from app.schemas.log_event import NormalizedLogEvent


class FirewallLogParser(BaseLogParser):
    source_type = "firewall"

    def parse(self, raw_content: str) -> List[NormalizedLogEvent]:
        events: List[NormalizedLogEvent] = []
        raw_content = raw_content.strip()
        if not raw_content:
            return events

        reader = csv.DictReader(io.StringIO(raw_content))
        for row in reader:
            try:
                # Handle ISO timestamps like 2026-09-11T16:00:01Z
                ts_str = row.get("timestamp", "")
                if ts_str:
                    clean_ts = ts_str.replace("Z", "+00:00")
                    timestamp = datetime.fromisoformat(clean_ts)
                else:
                    timestamp = datetime.now(timezone.utc)
            except Exception:
                timestamp = datetime.now(timezone.utc)

            source_ip = row.get("source_ip")
            destination_ip = row.get("destination_ip")
            source_port = int(row["source_port"]) if row.get("source_port") and row["source_port"].isdigit() else None
            destination_port = int(row["destination_port"]) if row.get("destination_port") and row["destination_port"].isdigit() else None
            action = row.get("action", "ALLOW").upper()
            flags = row.get("flags", "")

            event_type = "FIREWALL_DENY" if action == "DENY" else "FIREWALL_ALLOW"
            severity_hint = "WARNING" if action == "DENY" else "INFO"

            events.append(
                NormalizedLogEvent(
                    timestamp=timestamp,
                    source_type=self.source_type,
                    source_ip=source_ip,
                    destination_ip=destination_ip,
                    source_port=source_port,
                    destination_port=destination_port,
                    event_type=event_type,
                    severity_hint=severity_hint,
                    raw_message=",".join([f"{k}={v}" for k, v in row.items()]),
                    metadata={"protocol": row.get("protocol"), "action": action, "flags": flags},
                )
            )
        return events
