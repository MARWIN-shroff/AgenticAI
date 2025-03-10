# Agentic AI Chatbot

Agentic AI Chatbot is an AI-powered chatbot built using FastAPI, LangChain, and Streamlit. It supports Groq and OpenAI models, integrates web search using Tavily, and provides a smart and friendly chat experience.

## Features

- Supports Multiple LLMs: Choose between OpenAI (GPT-4o-mini) and Groq (Llama-3.3-70B Versatile).
- Web Search Integration: Option to enable real-time search with Tavily.
- Customizable AI Agent: Define the system prompt for personalized responses.
- Interactive UI: Built with Streamlit for an easy-to-use frontend.
- FastAPI Backend: Provides an API for chatbot interactions.
- Docker Support: Easily deploy using Docker.

## Project Structure

```
📦 Agentic-AI-FastAPI
├── backend.py            # FastAPI backend
├── frontend.py           # Streamlit frontend
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker build file
├── docker-compose.yml    # Docker Compose configuration
├── .gitignore            # Ignore unnecessary files
└── README.txt            # Project documentation
```

## Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/MARWIN-shroff/Agentic-AI-Chatbot.git
cd Agentic-AI-Chatbot
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file and add the following:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 4. Run the Backend

```sh
uvicorn backend:app --host 127.0.0.1 --port 8000
```

### 5. Run the Frontend

```sh
streamlit run frontend.py
```

## Docker Deployment

### 1. Build & Run with Docker Compose

```sh
docker-compose up --build
```

### 2. Access the Chatbot

- Backend API: `http://127.0.0.1:8000`
- Frontend UI: `http://127.0.0.1:8501`

## API Documentation

FastAPI provides automatic Swagger UI:\
🔗 [Swagger Docs](https://swagger.io/docs/)

## Usage

1. Select AI model provider (Groq/OpenAI).
2. Enter a system prompt (e.g., "Act as a financial advisor").
3. Enable web search (optional).
4. Enter your query and click "Ask Agent".
5. View the AI response.

## Future Improvements

- Enhance conversation memory
- Support more LLM models
- Deploy to cloud (e.g., AWS, GCP)

## Contributing

Feel free to fork the repo and submit a pull request!

## License

This project is open-source under the MIT License.

## Contact

🔹 Author: [MARWIN-shroff](https://github.com/MARWIN-shroff)\
🔹 GitHub Repo: [Agentic-AI-Chatbot](https://github.com/MARWIN-shroff/Agentic-AI-Chatbot)

Happy Coding! 🚀

