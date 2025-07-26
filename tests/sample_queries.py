from app.rag import rag_pipeline

response = rag_pipeline("Who killed the artist Samarish Basu and stole the painting? No preamble", r"D:\AI Projects\RAG\data\data.txt")
print(response)