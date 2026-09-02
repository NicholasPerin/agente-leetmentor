# Código da Aplicação

Esta pasta contém o código do agente.

## Estrutura Sugerida

```text
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```text
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
