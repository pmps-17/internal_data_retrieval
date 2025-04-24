
import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection("data")


# Adding internal documents embeddings to ChromaDB
def build_index(embeddings):

    if not embeddings:
        print("️ No documents found to index.")
        return

    ids, docs, vecs = zip(*embeddings)
    collection.add(
        ids=list(ids),
        documents=list(docs),
        embeddings=list(vecs)
    )
    print(f" Indexed {len(ids)} chunks to Chroma at.")
