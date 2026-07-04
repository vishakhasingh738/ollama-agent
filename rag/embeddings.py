from config import embeddings

def create_embeddings(chunks):
    """
    Convert document chunks into embedding vectors.
    """
    texts = []
    for chunk in chunks:
        texts.append(chunk.page_content)
    vectors = embeddings.embed_documents(texts)
    return vectors