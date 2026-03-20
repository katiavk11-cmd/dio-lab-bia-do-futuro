Aqui está o texto completo, formatado estritamente conforme o padrão solicitado (Markdown, sem emojis, com perguntas em citação e respostas fora):

# Base de Conhecimento: Agente XP

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Organize a base de conhecimento do agente "XP" (Educador Financeiro Gamer) usando os 4 arquivos da pasta data/. Explique a função de cada arquivo na narrativa de jogo e monte um exemplo de contexto formatado para o LLM seguindo a estética de "Status do Player".

## Dados Utilizados

| Arquivo | Formato | Para que serve no XP? |
| :--- | :--- | :--- |
| perfil_investidor.json | JSON | Define o Nível e Classe do Player (objetivos, renda e tolerância a risco). |
| historico_atendimento.csv | CSV | Funciona como o Log de Quests, lembrando quais conceitos o player já aprendeu. |
| produtos_financeiros.json | JSON | É o Catálogo de Itens/Equipamentos que o XP usa para explicar as mecânicas. |
| transacoes.csv | CSV | É o Inventário de Gold, usado para analisar onde o player está ganhando ou perdendo recursos. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim. Os dados foram totalmente "gamificados" para o público de 16-25 anos. As categorias de gastos foram renomeadas para termos como Fast_Travel (Transporte) e Skill_Upgrade (Educação). Os produtos financeiros agora possuem descrições de "Lore" para facilitar o entendimento didático através de analogias de RPG/Estratégia.

---

## Estratégia de Integração

### Como os dados são carregados?

> Descreva como seu agente acessa a base de conhecimento.

Os dados serão carregados via Python (Pandas e JSON) e injetados no Contexto de Sistema do Ollama.

```python
import pandas as pd
import json

# Carregando o "Save Game" do Player
perfil = json.load(open('./data/perfil_investidor.json'))
log_quest = pd.read_csv('./data/historico_atendimento.csv')
gold_flow = pd.read_csv('./data/transacoes.csv')
itens_shop = json.load(open('./data/produtos_financeiros.json'))
```

### Como os dados são usados no prompt?

> [explique a lógica de uso dos dados no prompt]

Os dados são convertidos em um resumo de "Status do Personagem" e injetados dinamicamente no prompt. Isso garante que o XP sempre saiba exatamente em que fase o player está e quais itens de "Gold" (dinheiro) ele tem no inventário antes de dar uma explicação.

---

## Exemplo de Contexto Montado

> [monte um exemplo de contexto que será enviado para o LLM]

DADOS DO PLAYER (STATUS):
Nome: João Silva (Nível: Iniciante)
Main Goal: Build de "Reserva de Emergência" (Save Point)
Status de Gold: R$ 10.000 acumulados (Meta: R$ 15.000)
Estilo de Jogo: Seguro / Defensivo

ANÁLISE DE INVENTÁRIO (GASTOS RECENTES):
Skill_Upgrade (Educação): R$ 600,00
Fast_Travel (Transporte): R$ 120,00
Consumíveis (Sobrevivência): R$ 250,00
Social_Loot (Lazer): R$ 85,00
Microtransações (Skins/Streaming): R$ 75,80
Total de Gold Gasto: R$ 1.130,80

ITENS DISPONÍVEIS PARA TUTORIAL:
Tesouro Selic: Shield Nível 1 (Ideal para o objetivo atual)
CDB Liquidez Diária: Poção de Stamina (Recuperação rápida)
LCI/LCA: Escudo Anti-Taxa (Requer Cooldown de 90 dias)
FIIs: Farm de Gold Passivo (Nível Médio)
Fundo de Ações: Dungeon de Alto Risco (Nível Avançado)

