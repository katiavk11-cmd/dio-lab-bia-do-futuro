
# 🚀 Passo a Passo de Execução: Agente XP

## 🛠️ Setup do Ollama

1. **Instalar Ollama:** Baixe e instale através do site oficial [ollama.com](https://ollama.com).
2. **Baixar o Modelo (O "Cérebro"):** Abra o terminal (PowerShell) e baixe o modelo que configuramos no código:
   ```powershell
   ollama pull llama3
   ```
   *(Ou `ollama pull tinyllama` se preferir a versão ultra leve).*
3. **Testar a Conexão:**
   ```powershell
   ollama run llama3 "E aí, XP! Tá online?"
   ```

---

## 🐍 Código e Dependências

Todo o código-fonte atualizado deve estar no arquivo `app.py`. Certifique-se de que a pasta `data/` com os arquivos JSON e CSV está no mesmo diretório.

### 1. Instalar Bibliotecas (Plugins)
Com o seu ambiente virtual (`venv`) ativo, instale as dependências necessárias:
```powershell
pip install streamlit pandas ollama
```
> **Nota:** Trocamos `requests` pela biblioteca oficial `ollama`, que é mais rápida e estável para o nosso código.

---

## 🎮 Como Rodar o App

1. **Garantir que o Servidor está Ativo:**
   Verifique se o ícone do Ollama está aparecendo na barra de tarefas (perto do relógio). Se não estiver, abra o app Ollama ou digite no terminal:
   ```powershell
   ollama serve
   ```

2. **Executar o Streamlit:**
   Vá para a pasta onde o seu projeto está salvo e rode o comando:
   ```powershell
   streamlit run app.py
   ```
   *Se o seu arquivo estiver dentro de uma pasta `src`, use:* `streamlit run src/app.py`.

---

## 🔍 Verificação de Debug (Caso dê erro)

* **Erro de Modelo (404):** Verifique se o nome do modelo no `app.py` é exatamente o mesmo que você baixou no `ollama pull`.
* **Erro de Caminho (Path):** Se o XP não ler o seu saldo, confirme se a pasta `data` está na mesma pasta que o `app.py`.
* **Lentidão:** A primeira resposta demora pois o PC está carregando o modelo. As próximas serão instantâneas.

---


## Evidência de Execução

<img width="1920" height="1107" alt="image" src="https://github.com/user-attachments/assets/60feed79-38a6-43dc-b23a-9dd007e34c1d" />
