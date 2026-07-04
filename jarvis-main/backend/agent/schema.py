from dataclasses import dataclass
from typing import Optional


@dataclass
class ToolCall:

    tool: str

    action: str

    target: Optional[str] = None

    value: Optional[str] = None