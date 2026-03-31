#  LLM LangChain Playground

A comprehensive collection of examples demonstrating how to use **LangChain with multiple LLM providers** including:

* OpenAI (GPT)
* Anthropic (Claude)
* Google Gemini
* Hugging Face (API + Local Models)
* Embeddings & Semantic Search

---

##  Features

✔️ Multiple LLM integrations
✔️ Embedding generation (OpenAI + HuggingFace)
✔️ Document similarity using cosine similarity
✔️ Local & API-based model support
✔️ Clean and modular code structure

---

##  Project Structure

```
models/        → LLM integrations
embeddings/    → Embedding examples
similarity/    → Semantic search
demos/         → Simple demos
docs/          → Guides
```

---

##  Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/GenAI.git
cd GenAI
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

```bash
cp .env.example .env
```

Add your API keys inside `.env`.

---

##  Run Example

```bash
python models/openai_chat.py
```

---

##  Example Output

```
What is the capital of France?
→ Paris
```

---

##  Use Cases

* Chatbots
* RAG systems
* Semantic search
* AI apps
---

⭐ Star this repo if you found it helpful!
