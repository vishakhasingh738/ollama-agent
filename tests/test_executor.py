"""Tests for tool executor."""

from agent.executor import execute_action

def test_execute_action():
    # Test calculator tool
    action = {
        "type": "action",
        "tool": "calculator",
        "input": "2 + 2"
    }
    result = execute_action(action)
    print("Calculator Result:", result)

    # Test web_search tool
    action = {
        "type": "action",
        "tool": "web_search",
        "input": "Python programming"
    }
    result = execute_action(action)
    print("Web Search Result:", result)

    # Test RAG tool
    action = {
        "type": "action",
        "tool": "rag",
        "input": "What is the capital of France?"
    }
    result = execute_action(action)
    print("RAG Result:", result)


if __name__ == "__main__":
    test_execute_action()
