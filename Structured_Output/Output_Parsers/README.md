# LangChain Output Parsers Comparison

## Overview

**Output Parsers** in LangChain help convert the raw (often unstructured) text output from Large Language Models (LLMs) into usable Python data structures.

They are especially useful when working with older models or when you need fine-grained control over formatting instructions in the prompt.

> **Note**: Modern LLMs (like GPT-4o, Claude 3, Grok, Gemini) often support **native structured output** via `.with_structured_output()` or tool calling, which is usually more reliable than legacy output parsers.

---

## The Four Main Output Parsers

| Parser                      | Output Type                  | Validation | Schema Definition          | Best For                              | Limitations                          | When to Use |
|----------------------------|------------------------------|------------|----------------------------|---------------------------------------|--------------------------------------|-------------|
| **StrOutputParser**        | `str` (plain text)           | None       | Not applicable             | Simple text extraction, chatbots, raw responses | No structure at all                  | You just need clean text |
| **JsonOutputParser**       | `dict` (Python dictionary)   | None       | In prompt (JSON schema)    | Flexible JSON-like data               | No type validation, can fail on bad JSON | Quick structured data without strict types |
| **StructuredOutputParser** | `dict` (Python dictionary)   | Basic      | Schema via `ResponseSchema` | Fixed schema with clear instructions  | Less powerful than Pydantic          | When you want a simple schema without Pydantic dependency |
| **PydanticOutputParser**   | Pydantic Model (typed object)| **Full**   | Pydantic BaseModel         | Production-grade apps, type safety, validation | Requires Pydantic models             | When you need strict typing + validation |

---

### 1. StrOutputParser

- **Simplest parser**.
- Extracts only the text content from model outputs (handles `AIMessage`, `AIMessageChunk`, etc.).
- No formatting instructions needed in the prompt.
- Supports streaming.

**Use case**: When you just want the raw response as a string (e.g., for display, summarization chains, or further manual processing).

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
chain = llm | parser
result = chain.invoke(prompt)  # Returns: str