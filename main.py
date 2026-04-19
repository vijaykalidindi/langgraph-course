from inspect import AGEN_CLOSED
from dotenv import load_dotenv
import os

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


@tool
def search_web(query: str) -> str:
    """
    Tool that searches the web for the given query.
    
    Args:
        query: The query to search the web for.        
    Returns:
        The results of the search.
    """

    print(f"Searching the web for {query}")
    return "Tokyo weather is sunny."


llm = ChatAnthropic(model="claude-sonnet-4-6")
# llm = ChatOpenAI()
tools = [search_web]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langgraph-course!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)

if __name__ == "__main__":
    main()
