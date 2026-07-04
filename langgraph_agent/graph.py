from langgraph.graph import START, END, StateGraph

from langgraph_agent.state import AgentState
from langgraph.checkpoint.memory import MemorySaver

from langgraph_agent.nodes import (

    planner_node,

    tool_node,

    route

)

builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)

builder.add_node("tool", tool_node)
builder.add_edge(START, "planner")

builder.add_conditional_edges(

    "planner",

    route,

    {

        "tool": "tool",

        "end": END

    }

)
builder.add_edge(

    "tool",

    "planner"

)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)