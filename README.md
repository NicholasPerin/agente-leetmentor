# LeetMentor: O Agente para o LeetCode

Este é um agente de IA feito para te ajudar com questões do LeetCode, rodando localmente usando Ollama com o modelo `gpt-oss`.

Exemplo:

![Exemplo][assets/Questao - lista de exer.png]

## Install

HARNESS:
> Obs: Qualquer harness funciona. Eu optei pelo Ollama.

[Ollama 0.33+](https://ollama.com/download)

```sh
ollama run gpt-oss:20b
```

PYTHON:

```sh
pip install -r ./src/requirements.txt
```

## Estrutura do Repositório

```text
📁 agente-leetmentor/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico.csv                 # Histórico do usuário (CSV)
│   └── leetcode_dataset.csv          # Questões do LeetCode (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   └── 04-metricas.md                # Avaliação e métricas
│
├── 📁 src/                           # Código da aplicação
│   ├── modelo.py                     # Configurações Ollama + prompt
│   └── app.py                        # Forma a interface web
│
└── 📁 assets/                        # Imagens e diagramas
    └── ...
```
