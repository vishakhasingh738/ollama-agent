from .loader import load_documents
from .splitter import split_documents
from .embeddings import create_embeddings

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