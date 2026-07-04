import re

def parse_response(response):
    """
    Parse the LLM response.

    Returns:

    {
        "type": "action",
        "tool": "...",
        "input": "..."
    }

    OR

    {
        "type": "final",
        "answer": "..."
    }
    """

    action_match = re.search(r"Action:\s*(.+)", response)

    input_match = re.search(r"Action Input:\s*(.+)", response)

    final_match = re.search(r"Final Answer:\s*(.+)", response)

    if action_match and input_match:

        return {
            "type": "action",
            "tool": action_match.group(1).strip(),
            "input": input_match.group(1).strip()
        }

    if final_match:

        return {
            "type": "final",
            "answer": final_match.group(1).strip()
        }

    return {
        "type": "unknown"
    }