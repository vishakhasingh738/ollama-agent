from langchain_core.tools import tool
from duckduckgo_search import DDGS

@tool
def web_search(query: str) -> str:
    """
    Search the web for current information.
    Use this tool when the user asks about recent events,
    news, current versions, or anything requiring up-to-date information.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return "No results found."

        output = []

        for result in results:
            output.append(
                f"Title: {result['title']}\n"
                f"Body: {result['body']}\n"
                f"URL: {result['href']}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Search Error: {e}"