from typing import List
from pydantic import BaseModel,Field



from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """schema for a source used by the agent"""

    url:str=Field(description="the URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer:str=Field(description="the agent's answer to the query")
    sources:List[Source]=Field(default_factory=list,description="list of sources used to generate the answer")

# llm=ChatOllama(model="gpt-oss:20b")
llm=ChatOpenAI(model="gpt-5.4-nano")
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools,response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result=agent.invoke({"messages":HumanMessage(content="search for 3 job posting for ai engineer in mumbai using langchain/langgraph in mumbai using linkedin")})
    print(result)

if __name__ == "__main__":
    main()
