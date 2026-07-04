"""Tests for RAG embeddings."""

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import create_embeddings

def test_embeddings():
    documents = load_documents()
    chunks = split_documents(documents)
    vectors = create_embeddings(chunks)

    print(f"Chunks: {len(chunks)}")
    print(f"Vectors: {len(vectors)}")
    print()
    print("First vector length:")
    print(len(vectors[0]))
    print()
    print("First 10 numbers:")
    print(vectors[0][:10])

if __name__ == "__main__":
    test_embeddings()
