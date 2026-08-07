# Shared state passed between every node in the graph.
from typing import TypedDict, Optional

class AgentState(TypedDict):
    query: str
    user: Optional[dict]
    intent: str
    reply: str