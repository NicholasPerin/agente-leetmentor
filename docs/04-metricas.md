# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
| --------- | -------------- | ------------------ |
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar sobre uma lista de questões de um tema específico |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do usuário? | Explicar tópicos de acordo com o nível de aprendizado |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Pergunta fora do escopo

- **Pergunta:** "Qual a temperatura média do tempo hoje?"
- **Resposta esperada:** Desculpe, mas não tenho acesso a dados em tempo real, como a temperatura atual. Posso ajudar com questões ou tópicos de LeetCode se desejar!
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de exercícios

- **Pergunta:** "Me passe uma lista sobre Arrays, de nível fácil."
- **Resposta esperada:** Claro! Aqui vai um roadmap com 15 questões sobre Arrays no LeetCode: ...
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta sobre finanças

- **Pergunta:** "Quanto custava uma share da amazon ontem em média?"
- **Resposta esperada:** Desculpe, mas não tenho acesso a informações atualizadas sobre preços de ações, nem a dados históricos específicos da Amazon. Para obter a média de preço de uma ação da Amazon de ontem, recomendo consultar plataformas financeiras confiáveis, como Yahoo Finance, Bloomberg ou o site oficial da NYSE.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Dica para iniciantes

- **Pergunta:** "Quais questões você recomenda eu fazer como inicante na programação?"
- **Resposta esperada:** Recomendo as questões de número 1 - Two Sum, 2 - Add Two Numbers, ...
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**

- O modelo consegue ajudar bastante relacionado ao LeetCode, seguindo as regras definidas claramente.

**O que pode melhorar:**

- Necessário incluir seu usuário ou no prompt a cada mensagem ou no `historico.csv`, e também as questões já resolvidas.
