#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st
import logging
import os
import time
st.set_page_config(page_title="Agentic AI", page_icon="🤖", layout="wide")
st.title("Agentic AI Chatbot")
st.write("This is a chatbot that can chat with you according to your needs and is smart and friendly")

system_prompt = st.text_area("Define your AI Agent: ", height = 70, placeholder = "Type your system prompt here...")

MODEL_NAMES_GROQ = ["mixtral-8x7b-32768", "llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select model provider: ", ("Groq", "OpenAI"))

if provider == "Groq":
    model_name = st.selectbox("Select Groq Model: ", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    model_name = st.selectbox("Select OpenAI Model: ", MODEL_NAMES_OPENAI) 
    
allow_web_search = st.checkbox("Allow Web Search") 
query = st.text_area("Enter your query: ", height = 150, placeholder = "Type your question here")

API_URL= os.environ.get("API_URL")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
#Step2: Setup API Call to Backend
if st.button("Ask Agent"):
    if query.strip():
        import requests
        payload = {
            "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [query],
            "allow_search": allow_web_search
        }
        
        logging.info(f"Sending API request with payload: {payload}")
        try:
            response = requests.post(API_URL, json=payload)
            with st.spinner("Waiting for response..."):
                response = requests.post(API_URL, json=payload)
                time.sleep(1)
            if response.status_code == 200:
                response_data = response.json()
                logging.info(f"API Response: {response_data}")
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.session_state.chat_history.append((query, response_data))
                    st.subheader("Agent Response:")
                    st.markdown(f"**Final Response:** {response_data}")
            else:
                logging.error(f"API call failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {str(e)}")

if st.session_state.chat_history:
    st.subheader("Conversation History")
    for past_query, past_response in st.session_state.chat_history:
        st.markdown(f"**You:** {past_query}")
        st.markdown(f"**Agent:** {past_response}")
        st.markdown("---")