from dataclasses import dataclass, field, asdict
from typing import List


@dataclass
class AppResearch:

    name: str
    website: str

    category: str = ""

    description: str = ""

    authentication: str = ""

    self_serve: str = ""

    api_surface: str = ""

    mcp_support: str = ""

    buildability: str = ""

    blocker: str = ""

    confidence: float = 0.0

    evidence: List[str] = field(default_factory=list)

    verification_notes: str = ""

    verified: bool = False

    def to_dict(self):

        return asdict(self)