# Streamlit Local LLM Chat (Ollama + Phi)
A simple and interactive Streamlit web interface that connects to a locally running Large Language Model (LLM) using Ollama.
This project demonstrates how to integrate a frontend UI with a locally hosted AI model without using cloud APIs.
---

## Features
- Streamlit-based web interface
- Connects to locally installed LLM via Ollama
- Conversation history panel (sidebar)
- Reset chat functionality
- Lightweight model support (Phi)
- Fully local execution (no external API calls)
---

## Tech Stack
- Python
- Streamlit
- Ollama
- Requests
- Git & GitHub
---

## Prerequisites
Make sure the following are installed:
- Python 3.9+
- Ollama (https://ollama.com)
- Git
---

## Installation
### 1. Clone the repository
git clone https://github.com/SalmanSajjad95/Streamlit-Ollama-Local-LLM-Chat.git
cd Streamlit-Ollama-Local-LLM-Chat

### 2. Install dependencies
pip install -r requirements.txt
---

### 3. Pull the Phi Model Via Ollama (Very Important)
ollama pull phi
---

### 4. Run the Application
streamlit run app.py

Run the Streamlit app