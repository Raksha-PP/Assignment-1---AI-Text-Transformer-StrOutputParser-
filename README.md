# Assignment-1---AI-Text-Transformer-StrOutputParser-


## 📌 Objective
The goal of this project is to design and implement a text transformation pipeline using a Large Language Model (LLM), structured prompt engineering, and StrOutputParser.
The application accepts a paragraph as input and performs three key operations:

1. Generates a concise summary of 3–4 lines
2. Identifies the tone of the paragraph (Formal, Casual, or Technical)
3. Produces an enhanced and refined version of the original text
---

## 🛠 Technologies Used

- Python
- LangChain (LCEL)
- Ollama (Local LLM)
- Llama 3.1 model

---

## 🧠 How It Works

This project uses:

- `PromptTemplate` to structure the instructions
- `ChatOllama` to connect to the local Llama 3.1 model
- `StrOutputParser` to ensure the output is returned as a plain string
- LCEL chaining (`prompt | model | parser`) for clean pipeline execution

Pipeline Flow:

User Input → PromptTemplate → LLM (Llama 3.1) → StrOutputParser → Final Output

---

## 📦 Installation

### 1️⃣ Install Ollama
Download from:
https://ollama.com/download

Pull the required model:

```bash
ollama pull llama3.1
