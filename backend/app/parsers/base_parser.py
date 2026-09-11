from abc import ABC, abstractmethod
from typing import List
from app.schemas.log_event import NormalizedLogEvent


class BaseLogParser(ABC):
    """
    Abstract Base Class for all CyberSentinel log parsers.
    Enforces a standard contract across all log formats.
    """

    @property
    @abstractmethod
    def source_type(self) -> str:
        """Returns the canonical source type (e.g. 'windows', 'linux_syslog', 'apache', 'firewall')."""
        pass

    @abstractmethod
    def parse(self, raw_content: str) -> List[NormalizedLogEvent]:
        """
        Parses raw text or JSON log contents into a list of NormalizedLogEvent objects.
        """
        pass
