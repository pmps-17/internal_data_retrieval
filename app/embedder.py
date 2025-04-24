from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("EMBEDDING_MODEL")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
CHUNK_STRIDE = int(os.getenv("CHUNK_STRIDE"))

model = SentenceTransformer(MODEL)


# Splits text into overlapping chunks, so you never lose context at chunk boundaries
def chunk_text(text):
    tokens = text.split()
    for i in range(0, len(tokens), CHUNK_STRIDE):
        chunk = tokens[i:i+CHUNK_SIZE]
        if chunk:
            yield " ".join(chunk)


# Splits each document and store embeddings of each chunk
def embed_docs():
    embeddings = []
    for fname in os.listdir("data/docs"):
        path = os.path.join("data/docs", fname)
        text = open(path, "r").read()
        for idx, chunk in enumerate(chunk_text(text)):
            vec = model.encode(chunk).tolist()
            embeddings.append((f"{fname}#{idx}", chunk, vec))
    return embeddings
