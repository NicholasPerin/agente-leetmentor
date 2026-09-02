# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
| --------- | --------- | --------------------- |
| `historico.csv` | CSV | Contextualizar interações anteriores |
| `leetcode_dataset - lc.csv` | CSV | Base de dados das questões do LeetCode. |

---

## Estratégia de Integração

### Como os dados são carregados?
>
> Descreva como seu agente acessa a base de conhecimento.

Os dados são carregados no início da sessão e incluídos no contexto do prompt.

```python
import pandas as pd

historico = pd.read_csv("data/historico.csv")
questoes = pd.read_csv("data/leetcode_dataset.csv")
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```text
Dados do Cliente:
- Nome: João Silva
- Perfil: Iniciante
- Exercícios resolvidos no total: 37
- Estudando sobre: Hash table

Questões resolvidas:
1 - Two Sum - Easy
7 - Reverse Integer - Easy
...
```
