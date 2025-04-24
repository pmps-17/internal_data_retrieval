import pytest
from app.chroma_loader import build_index, collection

def test_build_index_empty(capsys):
    # Passing an empty list should early-return with a warning
    build_index([])
    captured = capsys.readouterr()
    assert "No documents found to index" in captured.out

def test_build_index_upserts(monkeypatch):
    # Spy on collection.add
    called = {}
    def fake_add(ids, documents, embeddings):
        called['ids'] = ids
        called['documents'] = documents
        called['embeddings'] = embeddings

    monkeypatch.setattr(collection, 'add', fake_add)

    sample = [
        ("idA", "Doc A text", [1.0, 2.0]),
        ("idB", "Doc B text", [3.0, 4.0])
    ]
    build_index(sample)

    assert called['ids'] == ["idA", "idB"]
    assert called['documents'] == ["Doc A text", "Doc B text"]
    assert called['embeddings'] == [[1.0, 2.0], [3.0, 4.0]]
