import argparse
from app.embedder import embed_docs
from app.chroma_loader import build_index
from app.retriever import retrieve
from app.generator import generate_answer


def index():
    # Converting docs to embeddings
    embs = embed_docs()
    # Storing the embeddings of docs in pinecone db
    build_index(embs)
    print(f"Indexed {len(embs)} chunks.")


def main():
    print(" Indexing documents…")
    index()

    print("\n Enter your question (or press Enter to exit):")
    query = input("> ").strip()
    if not query:
        print("No query entered.")
        return

    # Get the top k matches as per the query
    matches = retrieve(query)
    # Generate answer with the help of LLM
    answer = generate_answer(query, matches)
    print("\n=== Answer ===\n", answer)


if __name__ == "__main__":
    main()
