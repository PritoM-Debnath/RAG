from app.data_loader import load_text
from app.chunker import chunk_text
from app.embedder import get_embeddings, model
from app.retriever import build_faiss_index, retrieve
from app.generator import generate_answer
import numpy   as np

def rag_pipeline(query, story_path):
    text = load_text(story_path)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    index = build_faiss_index(np.array(embeddings))
    relevant_chunks = retrieve(query, model, index, chunks)
    return generate_answer(query, relevant_chunks[0])