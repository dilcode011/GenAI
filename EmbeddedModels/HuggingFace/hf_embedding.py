from langchain_huggingface import ChatHuggingFace,HuggingFaceEmbedding
from dotenv import load_dotenv

embedding=HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="What is the capital of France?"

vector=embedding.embed_query(text)

print(str(vector))