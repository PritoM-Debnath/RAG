from app.rag import rag_pipeline

response = rag_pipeline("Is the detective a male person or female person ?", r"D:\AI Projects\RAG\data\data.txt")
print(response)