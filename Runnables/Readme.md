#  Runnables in LangChain (Complete Guide)

##  Introduction

In modern **LangChain**, *Runnables* are the core building blocks used to create AI pipelines.

 A **Runnable** is any component that:

* Takes input
* Processes it
* Returns output

---

##  Why Runnables Are Used

### 1.  Standard Interface

All runnables follow the same methods:

```python
.invoke()   # Run with single input
.batch()    # Run with multiple inputs
.stream()   # Stream output in real-time
```

 This makes all components consistent and easy to use.

---

### 2.  Easy Chaining with LCEL

Runnables enable **LangChain Expression Language (LCEL)**:

```python
chain = prompt | llm | parser
```

 You can connect components like LEGO blocks.

---

### 3.  Replace Old Chains

 Old Way:

```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
```

 New Way (Runnable):

```python
chain = prompt | llm
```

 Cleaner, modern, and more powerful.

---

### 4.  Composability

You can combine multiple components:

* Prompts
* LLMs
* Retrievers
* Tools
* Output Parsers

  Build complex AI pipelines easily.

---

### 5.  Streaming Support

```python
for chunk in chain.stream("Tell me a story"):
    print(chunk)
```

 Output comes token-by-token (real-time like ChatGPT).

---

### 6.  Parallel Execution

```python
chain.batch(["AI", "ML", "DL"])
```

 Run multiple inputs simultaneously.

---

### 7.  Better Debugging & Control

* Inspect each step
* Modify pipeline easily
* Add logging

 Helps in building production-ready apps.

---

##  Basic Example

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Create prompt
prompt = ChatPromptTemplate.from_template("Explain {topic}")

# Initialize model
llm = ChatOpenAI()

# Create runnable chain
chain = prompt | llm

# Run
result = chain.invoke({"topic": "Artificial Intelligence"})
print(result)
```

---

##  How It Works

```
Input → Prompt → LLM → Output
```

 Each step is a Runnable connected using `|`

---

##  When to Use Runnables

Use Runnables when you want to:

* Build chatbots
* Create RAG pipelines
* Process multiple steps
* Stream responses
* Scale AI applications

---

##  Runnable vs Chain

| Feature        | Old Chains | Runnables   |    |
| -------------- | ---------- | ----------- | -- |
| Syntax         | Complex    | Simple (`   | `) |
| Flexibility    | Limited    | High        |    |
| Streaming      | Limited    | Yes         |    |
| Parallelism    | No         | Yes         |    |
| Modern Support | Deprecated | Recommended |    |

---

##  Key Concept

 Runnable = Function
 `|` Operator = Function Composition

---

##  Summary

Runnables are used because they:

* Standardize AI workflows
* Enable easy chaining
* Support streaming & batching
* Replace old chain systems
* Make applications scalable

---

##  Learn More

* https://python.langchain.com/docs/expression_language/
* https://python.langchain.com/docs/modules/chains/

---
