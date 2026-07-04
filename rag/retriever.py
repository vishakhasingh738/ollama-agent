from rag.vector_store import load_vector_store

def retrieve_documents(query, k=3):
    """
    Retrieve the most relevant document chunks for a query.

    Args:
        query (str): User's question
        k (int): Number of chunks to retrieve

    Returns:
        List[Document]
    """

    db = load_vector_store()
    documents = db.similarity_search(
        query=query,
        k=k
    )
    docs = retriever.invoke(question)

    for doc in docs:
        print(doc.metadata)
    return documents

