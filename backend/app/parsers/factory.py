from typing import Dict, Optional
from app.parsers.apache_parser import ApacheAccessLogParser
from app.parsers.base_parser import BaseLogParser
from app.parsers.firewall_parser import FirewallLogParser
from app.parsers.linux_parser import LinuxSyslogParser
from app.parsers.windows_parser import WindowsEventParser

PARSER_REGISTRY: Dict[str, BaseLogParser] = {
    "windows": WindowsEventParser(),
    "linux_syslog": LinuxSyslogParser(),
    "apache": ApacheAccessLogParser(),
    "firewall": FirewallLogParser(),
}


def get_parser(source_type: str) -> Optional[BaseLogParser]:
    """Retrieve parser instance by canonical source type."""
    return PARSER_REGISTRY.get(source_type.lower())


def auto_detect_parser(filename: str, sample_content: str) -> BaseLogParser:
    """
    Intelligently infer log parser from file extension and sample header content.
    """
    filename_lower = filename.lower()
    if filename_lower.endswith(".json"):
        return PARSER_REGISTRY["windows"]
    elif filename_lower.endswith(".csv"):
        return PARSER_REGISTRY["firewall"]

    # Content heuristic inspection
    sample_preview = sample_content[:500]
    if "EventID" in sample_preview or '"Channel": "Security"' in sample_preview:
        return PARSER_REGISTRY["windows"]
    if "HTTP/1." in sample_preview or "GET /" in sample_preview or "POST /" in sample_preview:
        return PARSER_REGISTRY["apache"]
    if "sshd[" in sample_preview or "sudo:" in sample_preview or "pam_unix" in sample_preview:
        return PARSER_REGISTRY["linux_syslog"]
    if "destination_ip" in sample_preview or "source_ip" in sample_preview:
        return PARSER_REGISTRY["firewall"]

    # Default fallback to linux syslog
    return PARSER_REGISTRY["linux_syslog"]
