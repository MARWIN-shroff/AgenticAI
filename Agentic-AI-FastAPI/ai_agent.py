#Step-1: Setup api keys for groq, OPENAI and tavily

import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# print(OPENAI_API_KEY)
#Step-2: Setup LLM and tools

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
search_tool = TavilySearchResults(max_results=4)


#Step-3: Setup the AI agent with search tool functionality

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
system_prompt="Act as an AI chatbot who has current affairs knowledge and is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    logging.info(f"Received request: LLM_ID={llm_id}, Provider={provider}, Allow_Search={allow_search}")
    try:
        if provider=="Groq":
            llm=ChatGroq(model=llm_id)
        elif provider=="OpenAI":
            llm=ChatOpenAI(model=llm_id)

        tools=[TavilySearchResults(max_results=2)] if allow_search else []
        agent=create_react_agent(
            model=llm,
            tools=tools,
            state_modifier=system_prompt
        )
        state={"messages": query}
        response=agent.invoke(state)
        messages=response.get("messages")
        ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
        logging.info(f"AI Response: {ai_messages[-1]}")
        return ai_messages[-1]
        
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}