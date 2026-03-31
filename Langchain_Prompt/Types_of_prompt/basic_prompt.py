from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Explain {topic} in {style} style.",
    input_variables=["topic", "style"]
)

print(template.format(topic="AI", style="simple"))