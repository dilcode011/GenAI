# LangChain Output Parsers - Complete Comparison

## Overview

**Output Parsers** in LangChain convert the raw output from LLMs (usually text) into structured Python objects.

They are particularly useful with older models or when you need explicit control over output formatting via prompts.

> **Note**: Modern LLMs (GPT-4o, Claude 3.5, Grok, Gemini 1.5, etc.) support **native structured output** using `.with_structured_output()` or tool calling. This is generally more reliable than legacy output parsers.

---

## Comparison Table

| Parser                          | Output Type                  | Validation       | Schema Definition                  | Streaming Support | Best For                                      | Limitations                              |
|--------------------------------|------------------------------|------------------|------------------------------------|-------------------|-----------------------------------------------|------------------------------------------|
| **StrOutputParser**            | `str`                        | None             | Not applicable                     | Yes               | Raw text, chatbots, summarization             | No structure                             |
| **JsonOutputParser**           | `dict`                       | None             | JSON format in prompt              | Yes (partial)     | Flexible JSON data                            | No type validation, brittle              |
| **StructuredOutputParser**     | `dict`                       | Basic            | `ResponseSchema`                   | No                | Simple fixed schema without Pydantic          | Less powerful, no type safety            |
| **PydanticOutputParser**       | Pydantic `BaseModel`         | **Full**         | Pydantic Model                     | No                | Production apps, type safety, validation      | Requires Pydantic                        |
| **PydanticToolsParser**        | Pydantic `BaseModel`         | **Full**         | Tool calling + Pydantic            | No                | When using tools / function calling           | Only works with tool-enabled models      |
| **XmlOutputParser**            | `dict`                       | None             | XML tags in prompt                 | No                | XML-based structured output                   | XML is verbose and less common           |
| **CommaSeparatedListOutputParser** | `list[str]`              | None             | Comma-separated list               | No                | Simple lists of items                         | Very limited use case                    |
| **MarkdownListOutputParser**   | `list[str]`                  | None             | Markdown list format               | No                | Extracting bullet-point lists                 | Limited                                  |
| **OutputFixingParser**         | Any (wrapper)                | Depends on inner | Wraps any parser                   | No                | Fixing malformed outputs from other parsers   | Adds extra LLM call                      |

---

