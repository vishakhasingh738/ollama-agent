from tools.registry import TOOLS

def execute_action(action):
    """
    Execute the selected tool.
    """

    tool = action["tool"]
    tool_input = action["input"]

    if tool not in TOOLS:
        return f"Unknown tool: {tool}"

    tool_obj = TOOLS[tool]
    
    # Check if it's a LangChain tool with .run() method
    if hasattr(tool_obj, 'run'):
        return tool_obj.run(tool_input)
    else:
        # It's a regular function, call it directly
        return tool_obj(tool_input)