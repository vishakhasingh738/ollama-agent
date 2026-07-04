from langchain.tools import tool

@tool
def calculator(expression: str):
    """
    Evaluate a simple mathematical expression.

    Example:
        25 * 8
        100 / 4
        (10 + 5) * 3
    """
    try:
        return eval(expression)
    except Exception as e:
        return f"Error evaluating expression: {e}"