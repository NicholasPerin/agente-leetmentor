"""Contém as configurações do Ollama + prompt que é enviado ao modelo."""

import pandas as pd


# Configurações pro Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gpt-oss:20b"


# Pega os dados da pasta ./data
HISTORICO = pd.read_csv("data/historico.csv")
QUESTOES = pd.read_csv("data/leetcode_dataset.csv")


# System prompt para o modelo
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


# Contexto para o modelo
CONTEXT = f"""
USUARIO: {HISTORICO["nome"]}
LINGUAGEM DE PROGRAMAÇÃO: {HISTORICO["linguagem_preferida"]}
QUESTÕES RESPONDIDAS: {HISTORICO["questoes_resolvidas"]}
TÓPICO ATUAL DE ESTUDO: {HISTORICO["topico_atual"]}

ID DAS QUESTÕES: {QUESTOES["id"]}
QUESTÕES: {QUESTOES["title"]}
"""
