Para fechar com chave de ouro, aqui está o seu **README.md** totalmente adaptado para a persona **XP**. Removi o tom de "professor" e apliquei a estética **Dev/Gamer** que a gente construiu.

---

# 🎮 XP - Mentor de Estratégia Financeira

Agente de IA Generativa que transforma a educação financeira em uma jornada de RPG. O **XP** ensina conceitos de economia de forma épica e personalizada, usando os dados reais do Player para montar a melhor "build" de vida.

## 💡 O Que é o XP?

O XP é o seu **Duo de Squad** para finanças: ele **ensina**, não recomenda. Ele traduz conceitos chatos como Selic, CDI e Reserva de Emergência para mecânicas de jogo, analisando seu inventário de gastos para você subir de nível sem dar *game over* no saldo.

### ✅ O que o XP faz:
* **Explica mecânicas:** Traduz o mercado financeiro para linguagem gamer.
* **Scan de Inventário:** Usa seus dados reais como exemplos práticos.
* **Quest Log:** Responde dúvidas sobre itens (produtos) financeiros.
* **Debug de Gastos:** Analisa onde sua Mana está sumindo de forma educativa.

### ❌ O que o XP NÃO faz:
* **Não dá Cheat Codes:** Proibido recomendar ações ou ativos específicos.
* **Sem Invasive Mod:** Não acessa dados bancários sensíveis.
* **NPC de Apoio:** Não substitui um consultor financeiro certificado.

---

## 🏗️ Arquitetura

**Stack de Tecnologia:**
* **Interface:** [Streamlit](https://streamlit.io/) (UI Gamer)
* **LLM:** [Ollama](https://ollama.com/) (Modelo local: `llama3` ou `tinyllama`)
* **Database:** JSON/CSV mockados para simular o save do player.

---

## 📁 Estrutura do Projeto

```text
├── data/                          # Base de Conhecimento (Inventário)
│   ├── perfil_investidor.json     # Status e Classe do Player
│   ├── transacoes.csv             # Log de Gastos (Gold)
│   ├── historico_atendimento.csv  # Quest Log (Interações)
│   └── produtos_financeiros.json  # Catálogo de Itens para Ensino
│
├── docs/                          # Documentação Técnica
│   ├── 01-documentacao-agente.md  # Persona XP e Caso de Uso
│   ├── 02-base-conhecimento.md    # Estratégia de Dados
│   ├── 03-prompts.md              # System Prompts "Anti-Chatice"
│   ├── 04-metricas.md             # Avaliação de Damage/Assertividade
│   └── 05-pitch.md                # Apresentação do Projeto
│
└── src/
    └── app.py                     # Kernel da Aplicação Streamlit
```

---

## 🚀 Como Executar o Deploy

### 1. Preparar o Servidor (Ollama)
```powershell
# Baixar em: ollama.com
ollama pull llama3
ollama serve
```

### 2. Instalar Dependências (Plugins)
```powershell
pip install streamlit pandas ollama
```

### 3. Iniciar a Campanha
```powershell
streamlit run src/app.py
```

---

## 🎯 Exemplos de Diálogo

**Player:** *"O que é CDI?"* **XP:** "O CDI é a taxa de atualização do servidor dos bancos. Se um item rende 100% do CDI, ele acompanha o meta atual do mercado. Quer ver como isso buffa seu Shield (Reserva)?"

**Player:** *"Onde está sumindo meu gold?"* **XP:** "Dando um scan no seu log de outubro: o **'Social Loot'** (R$ 450) está drenando sua Mana mais rápido que o **'Supermercado'** (R$ 300). Sua build está muito focada em exploração! Bora refatorar esses gastos?"

---

## 📊 Métricas de Avaliação

| Métrica | Objetivo |
| :--- | :--- |
| **Assertividade** | O XP respondeu a quest financeira corretamente? |
| **Shield (Segurança)** | O agente evitou recomendar a compra de ativos? |
| **Ping (Coerência)** | A resposta faz sentido com a classe do Player (Enzo/Dev)? |

---

## 🎬 Diferenciais do XP

* **Persona Gamer:** Linguagem informal de programador para programador.
* **100% Local:** Roda com Ollama. Seus dados financeiros não saem do seu servidor.
* **Educação Estratégica:** Foco em ensinar a mecânica, não em vender o loot.
* **Anti-Chatice:** Respostas curtas, diretas e sem enrolação de NPC.


