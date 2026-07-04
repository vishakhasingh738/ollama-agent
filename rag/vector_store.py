from langchain_community.vectorstores import FAISS
from config import embeddings
import os

def vector_db_exists():
    return os.path.exists(DB_PATH)

DB_PATH = "vector_db"
def create_or_update_vector_store(chunks):
    """
    Create or update a FAISS vector database from document chunks.
    """
    if vector_db_exists():
        vector_store = load_vector_db()
        vector_store.add_documents(chunks)
    else:
        vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=embeddings,
        )
    vector_store.save_local(DB_PATH)
    return vector_store

def load_vector_store():
    vector_store = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )
    return vector_store