from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents=[
    "The cat is on the roof.",
    "The dog is in the garden.",
    "The bird is flying in the sky.",
    "The fish is swimming in the pond.",
    "The cat is sleeping on the couch.",
    "The dog is barking at the mailman.",
    "The bird is singing in the tree.",
    "The fish is jumping out of the water.",
    ]

query="Where is the cat?"
doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)