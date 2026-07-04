from config import llm
from agent.prompt import AGENT_PROMPT
from agent.parser import parse_response
from agent.executor import execute_action


MAX_ITERATIONS = 5


def run_agent(user_input):

    scratchpad = f"User: {user_input}\n"

    for step in range(MAX_ITERATIONS):

        prompt = f"""
        {AGENT_PROMPT}

        {scratchpad}
        """

        response = llm.invoke(prompt).content

        print(f"\n===== Iteration {step + 1} =====")
        print(response)

        parsed = parse_response(response)

        if parsed["type"] == "final":
            return parsed["answer"]

        if parsed["type"] == "action":

            observation = execute_action(parsed)

            scratchpad += f"""

        {response}

        Observation:
        {observation}

        """

            continue

        return "Unable to understand model response."

    return "Maximum iterations reached."