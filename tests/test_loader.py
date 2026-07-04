"""Tests for RAG document loading."""

from rag.loader import load_documents

def test_load_documents():
    """
    Test the load_documents function to ensure it loads documents correctly.
    """
    documents = load_documents()
    print(documents)  # Print the loaded documents for verification

    print("Number of documents:", len(documents))

    print("\nContent:\n")
    print(documents[0].page_content)

    print("\nMetadata:\n")
    print(documents[0].metadata)

if __name__ == "__main__":
    test_load_documents()
