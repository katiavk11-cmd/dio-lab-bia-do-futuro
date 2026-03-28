import streamlit as st
import pandas as pd
import json
import ollama
import os

# 1. Setup Visual Dark Mode / Gamer
st.set_page_config(page_title="XP - Mentor Dev", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #58a6ff; }
    .stChatInput { border-radius: 10px; border: 1px solid #238636 !important; }
    section[data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    h1, h2, h3 { color: #58a6ff !important; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# 2. Carregamento de Dados (Inventário do Enzo)
def carregar_contexto():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_path, "data")
        
        def ler_json(nome):
            p = os.path.join(data_path, nome if nome.endswith('.json') else nome + ".json")
            with open(p, encoding='utf-8') as f: return json.load(f)
            
        perfil = ler_json('perfil_investidor')
        transacoes = pd.read_csv(os.path.join(data_path, 'transacoes.csv'))
        return perfil, transacoes
    except Exception as e:
        st.error(f"Erro no Load: {e}")
        return None, None

perfil, transacoes = carregar_contexto()

# 3. Sidebar: Dashboard de Status (Fixa para não poluir o chat)
if perfil:
    with st.sidebar:
        st.title(f"💻 User: {perfil.get('player_name', 'Enzo')}")
        st.write(f"**Stack:** {perfil.get('classe', 'Dev Júnior')}")
        st.write("---")
        st.metric("Shield (Saldo)", f"R$ {perfil.get('shield_atual', 0)}")
        st.write(f"🎯 **Meta:** {perfil.get('missao_principal', 'PC Gamer')}")
        st.write("---")
        if st.button("Resetar Terminal"):
            st.session_state.messages = []
            st.rerun()

# 4. System Prompt: XP - Mentor de Dev Júnior
SYSTEM_PROMPT = """
Você é o XP, mentor financeiro do Enzo (Dev Jr, 20 anos).
REGRAS RÍGIDAS:
1. IDIOMA: PT-BR (com gírias de dev/gamer: deploy, refatorar, bug, lag, hardware).
2. ANTI-CHATICE: Seja curto e seco. Máximo 2 parágrafos.
3. SEM REPETIÇÃO: Não diga o nome dele nem o saldo se ele não perguntar 'Quanto eu tenho?'.
4. ENCERRAMENTO: Se ele disser 'tchau', 'boa noite' ou 'valeu', responda 'Logs salvos. Até o próximo deploy!' e PARE de perguntar coisas.
5. FOCO: Se ele quiser comprar algo, analise se o 'custo de oportunidade' vai dar lag no setup dele.
6. Não dê lição de moral. Seja o 'Duo' dele na estratégia.
"""

# 5. Interface de Chat
st.title("📟 Agente XP: Monitor de Debug Financeiro")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Insira o comando..."):
    # Filtro de encerramento rápido
    despedidas = ['tchau', 'boa noite', 'valeu', 'obrigado', 'encerrar', 'nada mais', 'flw']
    fim_de_papo = any(p in prompt.lower() for p in despedidas)

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        if perfil:
            placeholder = st.empty()
            full_res = ""
            
            # Envia o mínimo para a IA não 'alucinar' com dados desnecessários
            ctx = f"Player: Enzo (Dev Jr). Saldo: {perfil['shield_atual']}. Gastos: {transacoes.tail(3).to_dict()}"
            input_ia = f"CONTEXTO: {ctx}\nPROMPT: {prompt}"

            try:
                for chunk in ollama.chat(model='llama3', messages=[
                    {'role': 'system', 'content': SYSTEM_PROMPT},
                    {'role': 'user', 'content': input_ia}
                ], stream=True):
                    full_res += chunk['message']['content']
                    placeholder.markdown(full_res + "▌")
                
                placeholder.markdown(full_res)
                st.session_state.messages.append({"role": "assistant", "content": full_res})
                
                if fim_de_papo:
                    st.info("Sessão encerrada pelo usuário.")
                    st.stop()
            except Exception as e:
                st.error(f"Erro no Kernel: {e}")
