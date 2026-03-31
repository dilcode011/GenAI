from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"input": "2+2", "output": "4"},
    {"input": "3+3", "output": "6"},
]

example_prompt = PromptTemplate(
    template="Q: {input}\nA: {output}",
    input_variables=["input", "output"]
)

fewshot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Solve:",
    suffix="Q: {input}\nA:",
    input_variables=["input"]
)

print(fewshot.format(input="5+5"))