from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vector_store import create_or_update_vector_store


def index_pdf(file_path: str):
    """
    Complete indexing pipeline:
    PDF -> Documents -> Chunks -> FAISS
    """

    documents = load_pdf(file_path)

    chunks = split_documents(documents)

    create_or_update_vector_store(chunks)

    return {
        "pages": len(documents),
        "chunks": len(chunks)
    }