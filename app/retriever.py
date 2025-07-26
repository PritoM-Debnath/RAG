import faiss
import numpy as np
import re

def normalize_bangla(text):
    text = re.sub(r'[“”‘’]', '"', text)  # Normalize quotes
    text = re.sub(r'\s+', ' ', text)     # Collapse extra spaces
    return text.strip()


def build_faiss_index(embeddings):
    # Normalize embeddings to unit vectors (important for cosine similarity)
    normalized_embeddings = np.vstack([emb / np.linalg.norm(emb) for emb in embeddings])
    dim = normalized_embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # IP = inner product, used for cosine similarity
    index.add(normalized_embeddings)
    return index

# def retrieve(query, model, index, chunks, top_k=1):
#     query_vec = model.encode([query])
#     D, I = index.search(np.array(query_vec), top_k)
#     return [chunks[i] for i in I[0]]

def retrieve(query, model, index, chunks, top_k=1, threshold_similarity=0.4):
    query = normalize_bangla(query)

    # Encode and normalize query
    query_vec = model.encode([query])
    query_vec = query_vec / np.linalg.norm(query_vec)

    D, I = index.search(np.array(query_vec), top_k)
    cosine_scores = D[0]

    # Debug print
    print(f"🔎 Cosine similarity score: {cosine_scores[0]}")

    if cosine_scores[0] < threshold_similarity:
        print("⚠️ No relevant match found. Similarity too low.")
        return ["দুঃখিত, প্রাসঙ্গিক তথ্য খুঁজে পাওয়া যায়নি।"]

    return [chunks[i] for i in I[0]]

