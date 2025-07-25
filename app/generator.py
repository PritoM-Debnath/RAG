from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment. Check your .env file.")

client = Groq(api_key=api_key)

def generate_answer(query, context, model="llama3-70b-8192"):
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that gives answers grounded in context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=256,
        top_p=1.0,
        stop=None,
    )

    return response.choices[0].message.content.strip()
