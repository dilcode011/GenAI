from langchain_huggingface import ChatHuggingFace,HuggingFaceEmbedding
from dotenv import load_dotenv

embedding=HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents=[
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome."
    
]

vector=embedding.embed_query(documents)

print(str(vector))