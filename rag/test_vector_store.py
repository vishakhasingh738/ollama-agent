from .loader import load_documents
from .splitter import split_documents
from .vector_store import create_vector_store,load_vector_store

documents = load_documents()
chunks = split_documents(documents)
db = create_vector_store(chunks)
print("Vector database created successfully!")
print(f"Number of chunks stored: {db.index.ntotal}")

db = load_vector_store()

print(db.index.ntotal)