from app.data_loader import load_text
from app.chunker import chunk_text
from app.embedder import get_embeddings, model
from app.retriever import build_faiss_index, retrieve
from app.generator import generate_answer
import numpy   as np


text = load_text(r"D:\AI Projects\RAG\data\da-ta.txt")
chunks = chunk_text(text, max_words=500)
embeddings = get_embeddings(chunks)
index = build_faiss_index(np.array(embeddings))


def rag_pipeline(query):
    relevant_chunks = retrieve(query, model, index, chunks, top_k=1, threshold_similarity=0.4)
    print(" Retrieved chunk:", relevant_chunks[0])
    return generate_answer(query, relevant_chunks[0])

def answer_query(query: str) -> str:
    relevant_chunks = retrieve(query, model, index, chunks, top_k=1, threshold_similarity=0.4)
    if "দুঃখিত" in relevant_chunks[0]:
        return relevant_chunks[0]
    return generate_answer(query, relevant_chunks[0])