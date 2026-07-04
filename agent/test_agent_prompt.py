from config import llm
from .prompt import AGENT_PROMPT

question = "What is 245 * 18?"

prompt = f"""
{AGENT_PROMPT}

User:
{question}
"""

response = llm.invoke(prompt)

print(response.content)