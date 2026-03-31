template = PromptTemplate(
    template="Hello {% if name %}{{name}}{% else %}Guest{% endif %}",
    input_variables=["name"],
    template_format="jinja2"
)