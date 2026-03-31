from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model='gpt-3.5-turbo-instruct', temperature=0.9)

#!temperature
# is a parameter that controls the randomness of the output. A higher temperature will result in more random output, while a lower temperature will result in more deterministic output.

#temperature parameter --> lower value(0.0-0.3) will make the output more focused and deterministic, while a higher value (0.7-1.0) will make the output more creative and diverse.

#!Max_Completion_Tokens
# is a parameter that limits the maximum number of tokens that can be generated in the response. This is useful to prevent the model from generating excessively long responses that may not be relevant or useful.

result=model.invoke("What is the capital of France?")

print(result)

print(model.content) # to get the just content of the response