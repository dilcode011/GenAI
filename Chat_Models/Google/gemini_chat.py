from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenAI(model='gemini-2.0-pro', temperature=0.9)
result=model.invoke("What is the capital of France?")
print(result)
