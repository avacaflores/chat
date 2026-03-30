# Chat with Ollama

A simple Python Flask web app for chatting with Ollama using the qwen2.5:0.5b model.

## Local Setup

1. Ensure Ollama is installed and running locally.
2. Pull the model: `ollama pull qwen2.5:0.5b`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`

Open http://127.0.0.1:5000/ in your browser.

## Docker Deployment

1. Ensure Ollama is running on 192.168.1.146:11434.
2. Build and run with Docker Compose: `docker-compose up --build`
3. Access the app at http://localhost:5000