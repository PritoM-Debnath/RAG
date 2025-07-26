import nltk
nltk.download('punkt')
nltk.download('punkt_tab')  # Just in case

from nltk.tokenize import sent_tokenize

def chunk_text(text, max_words=500):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []

    words = 0
    for sent in sentences:
        word_count = len(sent.split())
        if words + word_count <= max_words:
            current_chunk.append(sent)
            words += word_count
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sent]
            words = word_count
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks
