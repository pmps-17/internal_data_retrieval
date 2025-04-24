import pytest
import numpy as np
from app import retriever

# Replace the embedding model with a dummy that returns a NumPy array
class DummyModel:
    def encode(self, text):
        # Return a NumPy array so .tolist() exists
        return np.array([0.1, 0.2, 0.3], dtype="float32")

@pytest.fixture(autouse=True)
def patch_model(monkeypatch):
    # Monkey-patch retriever.model to our dummy
    monkeypatch.setattr(retriever, 'model', DummyModel())

# Dummy collection.query result
DUMMY_RESULTS = {
    "ids":        [["doc1_id", "doc2_id"]],
    "documents":  [["Text one",   "Text two"]],
    "distances":  [[0.95,         0.85]]
}

@pytest.fixture(autouse=True)
def patch_collection(monkeypatch):
    class DummyCollection:
        def query(self, query_embeddings, n_results):
            return DUMMY_RESULTS
    # Monkey-patch the collection used by retriever
    monkeypatch.setattr(retriever, 'collection', DummyCollection())
    return DUMMY_RESULTS

def test_retrieve_formats_matches_correctly():
    matches = retriever.retrieve("any question", top_k=2)
    assert isinstance(matches, list)
    assert len(matches) == 2

    # First match
    assert matches[0]["id"] == "doc1_id"
    assert pytest.approx(matches[0]["score"], rel=1e-3) == 0.95
    assert matches[0]["metadata"]["text"] == "Text one"

    # Second match
    assert matches[1]["id"] == "doc2_id"
    assert pytest.approx(matches[1]["score"], rel=1e-3) == 0.85
    assert matches[1]["metadata"]["text"] == "Text two"
