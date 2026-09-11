from pathlib import Path
from app.parsers.apache_parser import ApacheAccessLogParser
from app.parsers.firewall_parser import FirewallLogParser
from app.parsers.linux_parser import LinuxSyslogParser
from app.parsers.windows_parser import WindowsEventParser

SAMPLE_LOGS_DIR = Path(__file__).resolve().parent.parent.parent / "sample_logs"


def test_linux_syslog_parser():
    file_path = SAMPLE_LOGS_DIR / "linux_auth_ssh_attack.log"
    content = file_path.read_text()

    parser = LinuxSyslogParser()
    events = parser.parse(content)

    assert len(events) >= 10
    event_types = [e.event_type for e in events]
    assert "FAILED_LOGIN" in event_types
    assert "SUCCESSFUL_LOGIN" in event_types
    assert "PRIVILEGE_ESCALATION_ATTEMPT" in event_types

    # Verify IP extraction
    failed_logins = [e for e in events if e.event_type == "FAILED_LOGIN"]
    assert all(e.source_ip == "198.51.100.45" for e in failed_logins)


def test_windows_event_parser():
    file_path = SAMPLE_LOGS_DIR / "windows_event_brute_force.json"
    content = file_path.read_text()

    parser = WindowsEventParser()
    events = parser.parse(content)

    assert len(events) == 5
    event_types = [e.event_type for e in events]
    assert "FAILED_LOGIN" in event_types
    assert "SUCCESSFUL_LOGIN" in event_types
    assert "PRIVILEGE_ASSIGNED" in event_types

    admin_event = [e for e in events if e.user == "Administrator"][0]
    assert admin_event.source_ip == "192.168.1.185"


def test_apache_access_parser():
    file_path = SAMPLE_LOGS_DIR / "apache_web_attacks.log"
    content = file_path.read_text()

    parser = ApacheAccessLogParser()
    events = parser.parse(content)

    assert len(events) == 6
    event_types = [e.event_type for e in events]
    assert "SQL_INJECTION_ATTEMPT" in event_types
    assert "PATH_TRAVERSAL_ATTEMPT" in event_types
    assert "XSS_ATTEMPT" in event_types


def test_firewall_parser():
    file_path = SAMPLE_LOGS_DIR / "firewall_port_scan.csv"
    content = file_path.read_text()

    parser = FirewallLogParser()
    events = parser.parse(content)

    assert len(events) == 8
    event_types = set([e.event_type for e in events])
    assert "FIREWALL_DENY" in event_types
    assert "FIREWALL_ALLOW" in event_types
