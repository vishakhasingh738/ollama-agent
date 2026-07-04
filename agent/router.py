from config import llm
from agent.router_prompt import ROUTER_PROMPT

def route_question(question: str) -> str:

    prompt = f"""
{ROUTER_PROMPT}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip().lower()