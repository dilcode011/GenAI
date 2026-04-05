#It is an output parser in langchain that helps extract structured json data from llm responses based on predefined field schemas

#It works by defining a list of fields(ResponseSchema) that the model should return,ensuring the output follows a strucutred format

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParsers,ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

#schema
schema=[
    ResponseSchema(name='fact_1',description='Fact 1 about the topic')
    ResponseSchema(name='fact_2',description='Fact 2 about the topic')
    ResponseSchema(name='fact_3',description='Fact 3 about the topic')
]
parser=StructuredOutputParsers.from_response_schemas(schema)

template=PromptTemplate(
    template='Give 3 fact about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction',parser.get_format_instructions()}
)

chain=template|model|parser
result=chain.invoke({'topic':'black hole'})

print(result)