from config import llm
from agent.prompts import AGENT_PROMPT
from agent.parser import parse_response
from agent.executor import execute_action

def planner_node(state):
    prompt = f"""
{AGENT_PROMPT}

Conversation:

{state['messages']}
"""

    response = llm.invoke(prompt).content

    state["messages"].append(response)

    parsed = parse_response(response)

    if parsed["type"] == "action":
        state["next_action"] = "tool"
        state["tool_name"] = parsed["tool"]
        state["tool_input"] = parsed["input"]

    elif parsed["type"] == "final":
        state["next_action"] = "end"

    else:
        state["next_action"] = "end"

    return state


def tool_node(state):
    action = {
        "tool": state["tool_name"],
        "input": state["tool_input"]
    }

    result = execute_action(action)
    state["tool_result"] = result
    state["messages"].append(f"Observation: {result}")

    return state


def route(state):
    return state["next_action"]
