from sentence_transformers import SentenceTransformer

model = model = SentenceTransformer("distiluse-base-multilingual-cased-v2")

def get_embeddings(text_chunks):
    return model.encode(text_chunks)
