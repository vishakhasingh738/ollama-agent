"""
Evaluation module for the AI Assistant Agent.

This module provides functions to evaluate the performance of the agent
on various test cases and metrics.
"""

from agent.graph import graph
from config import llm


def evaluate_agent(test_cases: list[dict]) -> dict:
    """
    Evaluate the agent on a set of test cases.
    
    Args:
        test_cases: List of test cases with 'input' and 'expected_output' keys
        
    Returns:
        Dictionary with evaluation results and metrics
    """
    results = []
    
    for test_case in test_cases:
        state = {
            "messages": [test_case["input"]],
            "next_action": "",
            "tool_name": "",
            "tool_input": "",
            "tool_result": "",
            "approved": False
        }
        
        try:
            result = graph.invoke(state)
            output = result["messages"][-1]
            
            results.append({
                "input": test_case["input"],
                "output": output,
                "expected": test_case.get("expected_output"),
                "status": "success"
            })
        except Exception as e:
            results.append({
                "input": test_case["input"],
                "output": None,
                "error": str(e),
                "status": "error"
            })
    
    return {
        "total": len(results),
        "successful": sum(1 for r in results if r["status"] == "success"),
        "failed": sum(1 for r in results if r["status"] == "error"),
        "results": results
    }


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        {
            "input": "What is 25 * 40?",
            "expected_output": "1000"
        },
        {
            "input": "Who is the current president of the US?",
            "expected_output": None  # Web search required
        }
    ]
    
    print("Evaluating agent...")
    results = evaluate_agent(test_cases)
    
    print(f"\nTotal: {results['total']}")
    print(f"Successful: {results['successful']}")
    print(f"Failed: {results['failed']}")
    
    for i, result in enumerate(results["results"], 1):
        print(f"\nTest {i}:")
        print(f"  Input: {result['input']}")
        print(f"  Status: {result['status']}")
        if result['status'] == 'error':
            print(f"  Error: {result['error']}")
        else:
            print(f"  Output: {result['output']}")
