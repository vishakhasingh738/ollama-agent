from typing import TypedDict

class AgentState(TypedDict):
    messages: list
    next_action: str
    tool_name: str
    tool_input: str
    tool_result: str
