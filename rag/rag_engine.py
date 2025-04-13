import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
index = faiss.read_index("data/faiss_index.idx")
text_chunks = pd.read_csv("data/text_chunks.csv", header=None)[0].tolist()
embedder = SentenceTransformer("all-MiniLM-L6-v2")
generator = pipeline("text-generation",
                     model = "tiiuae/falcon-rw-1b",
                     tokenizer ="tiiuae/falcon-rw-1b",
                     device = -1,
                     max_new_tokens = 50)
def get_rag_answer(query: str) -> str:
    query_vec =embedder.encode([query]).astype('float32')
    _, indices = index.search(query_vec, k=5)
    retrieved_chunks = [text_chunks[i] for i in indices[0]]
    context = "\n".join(retrieved_chunks)
    prompt = f"""You are a hotel data assistant. Use the context below to answer the user's question.
Context:
{context} 
Question: {query}
Answer: """
    response =  generator(prompt)[0]['generated_text']
    return response.strip()