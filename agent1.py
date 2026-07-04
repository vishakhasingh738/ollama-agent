from langgraph.prebuilt import create_react_agent

from config import llm
from tools import web_search
from tools.calculator import calculator

tools = [calculator, web_search]

agent = create_react_agent(
    model=llm,
    tools=tools,
)