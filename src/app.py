import streamlit as st
import pandas as pd
import json
import ollama
import os

# 1. Layout e Estilo (Dark Mode Dev)
st.set_page_config(page_title="XP - Mentor", layout="centered")
st.markdown("<style>.main { background-color: #0d1117; color: #c9d1d9; }</style>", unsafe_allow_html=True)

# 2. Loader de Contexto
def carregar_contexto():
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        data_p = os.path.join(base, "data")
        with open(os.path.join(data_p, 'perfil_investidor.json'), encoding='utf-8') as f:
            perf = json.load(f)
        with open(os.path.join(data_p, 'produtos_financeiros.json'), encoding='utf-8') as f:
            prod = json.load(f)
        return perf, prod
    except: return None, None

perfil, produtos = carregar_contexto()

# 3. Sidebar Status
if perfil:
    with st.sidebar:
        st.subheader(f"👾 Player: {perfil['player_name']}")
        st.metric("Shield (Saldo)", f"R$ {perfil['shield_atual']}")
        if st.button("Resetar Terminal"):
            st.session_state.messages = []
            st.rerun()

# 4. Prompt Balanceado (Sem respostas de uma palavra só)
SYSTEM_PROMPT = """
Você é o XP, mentor financeiro de Devs. 
REGRAS: 
- Responda em PT-BR. 
- Explique o conceito de forma direta em no máximo 3 frases.
- Use obrigatoriamente 1 termo de dev/gamer (ex: deploy, bug, loot, lag).
- PROIBIDO responder com apenas uma palavra ou apenas o termo técnico.
- Se o usuário se despedir, diga 'Logs salvos. Até o próximo deploy!' e encerre.
"""

# 5. Interface de Chat
st.title("📟 Agente XP: Debug Financeiro")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Insira o comando..."):
    # Filtro de Despedida Real
    despedidas = ['tchau', 'valeu', 'obrigado', 'fim', 'encerrar']
    if any(x in prompt.lower() for x in despedidas):
        st.session_state.messages.append({"role": "assistant", "content": "Logs salvos. Até o próximo deploy! 🔌"})
        st.info("Sessão finalizada. Limpe o terminal para recomeçar.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_res = ""
        
        cat_str = json.dumps(produtos, ensure_ascii=False)
        input_ia = f"CATÁLOGO DE ITENS: {cat_str}\n\nPERGUNTA: {prompt}"

        try:
            # Opções ajustadas para evitar respostas curtas demais ou alucinações
            for chunk in ollama.chat(
                model='llama3', 
                messages=[
                    {'role': 'system', 'content': SYSTEM_PROMPT},
                    {'role': 'user', 'content': input_ia}
                ],
                options={
                    'temperature': 0.4,   # Um pouco mais de "fala" natural
                    'num_predict': 120,   # Fôlego para completar a explicação
                    'top_p': 0.9          # Estabilidade nas palavras
                },
                stream=True
            ):
                full_res += chunk['message']['content']
                placeholder.markdown(full_res + "▌")
            
            placeholder.markdown(full_res)
            st.session_state.messages.append({"role": "assistant", "content": full_res})
        except Exception as e:
            st.error(f"Erro no Kernel: {e}")
