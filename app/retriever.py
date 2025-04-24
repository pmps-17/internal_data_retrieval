
import os
from app.embedder import model
from dotenv import load_dotenv
from app.chroma_loader import collection
os.environ["TOKENIZERS_PARALLELISM"] = "false"

load_dotenv()
TOP_K = int(os.getenv("TOP_K"))


def retrieve(query: str, top_k=TOP_K):
    # get the embeddings of the given query
    qvec = model.encode(query).tolist()

    # get the embeddings of top k matches of the given query from chroma db
    results = collection.query(
        query_embeddings=[qvec],
        n_results=top_k
    )
    ids = results["ids"][0]
    docs = results["documents"][0]
    distances = results["distances"][0]

    matches = []
    for doc_id, text, score in zip(ids, docs, distances):
        matches.append({
            "id":    doc_id,
            "score": score,
            "metadata": {"text": text}
        })
    return matches
