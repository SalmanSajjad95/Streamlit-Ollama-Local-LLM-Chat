import streamlit as st
import requests

st.set_page_config(
    page_title="Local LLM Chat",
    page_icon="💬",
    layout="centered"
)

st.title("Local LLM Chat Ollama + Phi(Lightweight version)")
st.markdown("Running locally using Ollama.")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "phi",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.ConnectionError:
        return "⚠️ Could not connect to Ollama. Make sure it is running."
    except Exception as e:
        return f"Error: {e}"

user_input = st.text_input("Enter your message:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Send"):
        if user_input:
            answer = query_ollama(user_input)
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("LLM", answer))

with col2:
    if st.button("Reset Chat"):
        st.session_state.history = []

st.sidebar.title("🕘 Conversation History")

if st.session_state.history:
    for role, text in st.session_state.history:
        if role == "You":
            st.sidebar.markdown(f"**🧑 {role}:** {text}")
        else:
            st.sidebar.markdown(f"**🤖 {role}:** {text}")
else:
    st.sidebar.write("No conversation yet.")