from .retriever import retrieve_documents

question = "Who created Python?"
results = retrieve_documents(question)
print(f"Retrieved {len(results)} chunks\n")
for i, doc in enumerate(results, start=1):
    print(f"----- Chunk {i} -----")
    print(doc.page_content)
    print("Metadata:", doc.metadata)
    print()