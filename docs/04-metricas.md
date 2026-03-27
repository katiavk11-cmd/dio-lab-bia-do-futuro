Aqui está a documentação completa e refinada do **Agente XP**, estruturada em Markdown para você copiar e colar diretamente no `README.md` do seu repositório no GitHub.

---

# 🎮 Agente XP: Seu Mentor de Estratégia Financeira

> **Status do Projeto:** 🛠️ Em Desenvolvimento (Fase Beta)  
> **Público-Alvo:** Jovens de 16 a 25 anos (Estudantes e Recém-formados)  
> **Tech Stack:** Python, Streamlit, Ollama (LLM Local)

---

## 📝 Caso de Uso

### O Problema
A grande barreira de entrada no mundo das finanças para jovens é a desconexão entre a teoria chata e a prática do dia a dia. Muitos entendem que devem "guardar dinheiro", mas não compreendem como a inflação, os juros e o custo de oportunidade afetam seu "gold" real (bolsa-estágio, mesada ou primeiro salário).

### A Solução
O **XP** atua como um mentor de RPG. Ele não apenas explica conceitos, mas analisa os dados reais do usuário (gastos com transporte, lazer, assinaturas) e traduz tudo para mecânicas de jogo. Ele foca em **Alfabetização Financeira Pura**, sem nunca realizar recomendações de compra de ativos específicos.

### Público-Alvo
Jovens entre **16 e 25 anos** que buscam autonomia financeira e preferem uma comunicação direta, informal e gamificada.

---

## 👤 Persona e Tom de Voz

* **Nome:** XP (Your Finance Experience Guide)
* **Personalidade:** Mentor "Pro-Player", estratégico, paciente e totalmente livre de julgamentos.
* **Tom de Comunicação:** Informal, "gamer" e altamente didático.
* **Bordões e Estilo:**
    * *Saudação:* "E aí, Player 1! Pronto para otimizar sua build financeira?"
    * *Conceitos:* "A reserva de emergência é o seu **Save Point**. Sem ela, qualquer Boss inesperado te dá Game Over."
    * *Limitação:* "Isso é uma quest de nível alto. Não posso te dar o 'cheat code' de qual ação comprar, mas te ensino a mecânica do risco!"

---

## 🏗️ Arquitetura do Sistema

```mermaid
flowchart TD
    A[Usuário/Player] --> B["Streamlit (Interface)"]
    B --> C{Orquestrador de Contexto}
    C -->|Prompt de Persona XP| D[LLM - Ollama Local]
    C -->|Dados de Inventário| E[Base de Conhecimento JSON/CSV]
    E --> D
    D --> F[Validação de Segurança]
    F --> G[Resposta do Mentor XP]
```

### Componentes Técnicos
| Componente | Ferramenta |
| :--- | :--- |
| **Interface** | [Streamlit](https://streamlit.io/) |
| **Cérebro (LLM)** | Ollama (Llama 3 / Mistral) |
| **Dataset** | JSON/CSV (Mockados na pasta `/data`) |

---

## 📚 Base de Conhecimento (Data)

O XP utiliza quatro fontes de dados para contextualizar o aprendizado:

1.  **`perfil_investidor.json`**: Status do Player (Nível, Classe, Meta de Gold).
2.  **`transacoes.csv`**: Log de Atividades (Gastos categorizados como `Fast_Travel`, `Social_Loot`, etc).
3.  **`produtos_financeiros.json`**: Catálogo de Itens (Descrições didáticas de Selic, CDB, FIIs).
4.  **`historico_atendimento.csv`**: Quest Log (Histórico de conceitos já aprendidos).

---

## 🛡️ Segurança e Anti-Alucinação

* **[X] Zero Recomendação:** O agente é bloqueado para termos de compra/venda.
* **[X] Grounded Truth:** Respostas baseadas estritamente nos dados fornecidos.
* **[X] Sandbox Educativo:** Se o tema for fora de finanças, o XP redireciona o foco para a "campanha" principal.
* **[X] Privacidade:** Execução local via Ollama, garantindo que os dados do "Player" não saiam da máquina.

---

## 📊 Métricas de Avaliação (Beta Test)

| Métrica | O que avalia | Meta |
| :--- | :--- | :--- |
| **Precisão de Scan** | Extração correta de valores do CSV/JSON. | 100% |
| **Integridade do Shield** | Bloqueio de recomendações de investimento. | 100% |
| **Sintonia da Guilda** | Clareza das analogias de game para o usuário. | Nota > 4/5 |

---

## 🚀 Como Executar (Em breve)

1.  Instale o [Ollama](https://ollama.ai/) e baixe o modelo (ex: `ollama run llama3`).
2.  Clone este repositório.
3.  Instale as dependências: `pip install streamlit pandas ollama`.
4.  Rode o comando: `streamlit run app.py`.

---

**Comentário aberto:** O que você achou desta experiência e o que poderia melhorar?

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]
