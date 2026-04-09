
# GenAI - LangChain Playground

A clean, well-structured collection of **LangChain** examples demonstrating how to work with multiple LLM providers, embeddings, prompts, and semantic search.

**Supported Providers:**
- OpenAI (GPT-4o, GPT-4o-mini, etc.)
- Anthropic (Claude 3.5 Sonnet, Claude 3 Opus)
- Google Gemini
- Hugging Face (Inference API + Local models with `transformers`)

---

##  Features

- Multiple LLM integrations with unified interface
- Embedding generation & vector similarity search (cosine similarity)
- Advanced prompt engineering (ChatPromptTemplate, few-shot, etc.)
- Structured Output (Pydantic, JSON mode, etc.)
- Local and API-based model support
- Clean, modular, and well-commented code

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
pip install -r requirement.txt
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

##  Use Cases

* Chatbots
* RAG systems
* Semantic search
* AI apps
---
