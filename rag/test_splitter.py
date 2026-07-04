from loader import load_documents
from splitter import split_documents

def test_split_documents():
    documents = load_documents()
    chunks = split_documents(documents)
    print("Number of chunks:", len(chunks))
    for i,chunk in enumerate(chunks):
        print(f"\nChunk {i+1}:\n")
        print(chunk.page_content)
        print(chunk.metadata)

if __name__ == "__main__":
    test_split_documents()