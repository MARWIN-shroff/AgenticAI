#Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List
import logging

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool
    
#Step2: Setup AI Agent from FrontEnd Request

from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
app=FastAPI(title="Agentic AI FastAPI")
ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    try:
        logging.info(f"Received chat request: {request}")
        llm_id = request.model_name
        query = request.messages
        allow_search = request.allow_search
        system_prompt = request.system_prompt
        provider = request.model_provider
        if request.model_name not in ALLOWED_MODEL_NAMES:
            logging.error("Invalid model name")
            return {"error": "Model not found"}
        response = get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider)
        logging.info(f"Chat response sent: {response}")
        return response
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
#Step3: Run app & Explore Swagger UI Docs

if __name__ == "__main__":
    import uvicorn
    logging.info("Starting FastAPI server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
    