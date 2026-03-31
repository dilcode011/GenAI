# This class is used to create dynamic prompts with placeholders. It allows you to define a template with variables that can be filled in at runtime, making it easier to generate customized prompts for different use cases.
from langchain_core.prompts import PromptTemplate

# template =PromptTemplate is used to create a prompt template with placeholders for dynamic content. The template string contains variables enclosed in curly braces (e.g., {paper_input}, {style_input}, {length_input}) that can be filled in with specific values when the prompt is invoked. The input_variables parameter specifies the list of variables that will be used in the template, and validate_template=True ensures that the template is checked for correctness when it is created.
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)


template.save('template.json')