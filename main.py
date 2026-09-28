from typing import List

from pydantic import BaseModel, Field


from inspect import AGEN_CLOSED
from dotenv import load_dotenv
import os

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The url of the source")

class AgentResponse(BaseModel): 
    """Schema for agent response with answer and sources"""

    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list,description="List of sources used to generate the answer")


llm = ChatAnthropic(model="claude-sonnet-4-6")
# llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langgraph-course!")
    content="What is the weather in Tokyo?"
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 jobs postings for an ai engineer using langchain in remote India on linkedin and list their details")]})
    print(result)

if __name__ == "__main__":
    main()
