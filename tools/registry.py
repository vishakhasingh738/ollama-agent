"""
Tool registry - centralized management of all available tools.
"""

from tools.calculator import calculator
from tools.web_search import web_search
from rag.rag_chain import answer_question

# Registry of all available tools
TOOLS = {
    "calculator": calculator,
    "web_search": web_search,
    "rag": answer_question,
}

def get_tool(tool_name: str):
    """Get a tool by name."""
    return TOOLS.get(tool_name)

def list_tools():
    """List all available tools."""
    return list(TOOLS.keys())

def tool_exists(tool_name: str) -> bool:
    """Check if a tool exists."""
    return tool_name in TOOLS
