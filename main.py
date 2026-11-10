from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


# llm=ChatOllama(model="gpt-oss:20b")
llm=ChatOpenAI(model="gpt-5.4-nano")
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)


def main():
    print("Hello from langchain-course!")
    result=agent.invoke({"messages":HumanMessage(content="search job posting for ai engineer in mumbai using langchain/langgraph in mumbai using linkedin")})
    print(result)

if __name__ == "__main__":
    main()
