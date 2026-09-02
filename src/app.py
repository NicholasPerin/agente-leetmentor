import streamlit as st
import pandas as pd
import requests

# Pega os dados da pasta /data
historico = pd.read_csv("data/historico.csv")
questoes = pd.read_csv("data/leetcode_dataset.csv")

# Configurações pro Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

# Contexto para o modelo
CONTEXT = f"""
USUARIO: {historico["nome"]}
LINGUAGEM DE PROGRAMAÇÃO: {historico["linguagem_preferida"]}
QUESTÕES RESPONDIDAS: {historico["questoes_resolvidas"]}
TÓPICO ATUAL DE ESTUDO: {historico["topico_atual"]}

ID DAS QUESTÕES: {questoes["id"]}
QUESTÕES: {questoes["title"]}
"""

# Prompt para o modelo
SYSTEM_PROMPT = """
Você é o LeetMentor, um educador sobre questões do LeetCode.

OBJETIVO:
Seu objetivo é ensinar, guiar, e montar um roadmap de questões sobre um tema que o usuário escolher.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos.
- Nunca invente questões que não são reais.
- Se não souber algo, admita e ofereça alternativas.
- NUNCA dê as soluções de questões inicialmente.
- Caso o aluno pergunte, ensine sobre um tema específico.
- Sempre pergunte se o aluno entendeu, e ajuste seu nível de ensino de acordo.
- Mantenha suas respostas objetivas, sem ultrapassar mais de 3 parágrafos.
- Sempre que passar um exercício, escreva também sua identificação para que seja facilmente encontrado.
"""


def perguntar(msg: str) -> str:
    """Manda a pergunta para o modelo dentro do Ollama."""
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO USUÁRIO: {CONTEXT}

    PERGUNTA: {msg}"""

    r = requests.post(
        OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False}
    )
    return r.json()['response']


# Interface dentro do Streamlit
st.title("Olá! Sou o LeetMentor!")

if pergunta := st.chat_input("Dúvida sobre o LeetCode..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
