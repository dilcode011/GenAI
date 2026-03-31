#  Static vs Dynamic Prompts (LangChain Guide)

A complete guide to understanding **Static and Dynamic Prompts** in prompt engineering using LangChain.

---

##  Overview

Prompts are instructions given to Large Language Models (LLMs) to generate responses.

There are two main types:
- Static Prompts  
- Dynamic Prompts  

---

#  1. Static Prompt

##  Definition
A **static prompt** is a fixed prompt where the input does not change.

It is hardcoded and always produces responses based on the same instruction.

---

##  Example

```python
prompt = "Explain Machine Learning in simple terms."
print(prompt)

#  2. Dynamic Prompt

##  Definition
A **dynamic prompt** uses variables/placeholders that can change based on user input.

It is created using tools like PromptTemplate in LangChain.

---

##  Example

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Explain {topic} in {style} style.",
    input_variables=["topic", "style"]
)

prompt = template.format(topic="AI", style="simple")
print(prompt)