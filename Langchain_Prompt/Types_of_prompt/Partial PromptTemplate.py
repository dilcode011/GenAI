template = PromptTemplate(
    template="Explain {topic} in {style} style.",
    input_variables=["topic", "style"]
)

partial = template.partial(style="simple")

print(partial.format(topic="AI"))