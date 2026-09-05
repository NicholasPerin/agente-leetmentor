"""Forma a interface web via Streamlit."""

import modelo as md
import streamlit as st
import requests


def perguntar(msg: str) -> str:
    """Manda a pergunta para o modelo dentro do Ollama."""
    prompt = f"""
    SYSTEM PROMPT: {md.SYSTEM_PROMPT}

    CONTEXTO DO USUÁRIO: {md.CONTEXT}

    PERGUNTA: {msg}
    """

    r = requests.post(
        md.OLLAMA_URL, json={"model": md.MODEL, "prompt": prompt, "stream": False}
    )
    return r.json()["response"]


# Título dentro do Streamlit
st.title("Olá! Sou o LeetMentor! Escreva sua pergunta abaixo.")

# Envia a pergunta do usuário para o modelo dentro do Streamlit
if pergunta := st.chat_input("Dúvida sobre o LeetCode..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
