from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.schema.runnable import R 

load_dotenv()

model=OpenAI()

print(model.get_input_jsonschema())
print(model.get_output_jsonschema())