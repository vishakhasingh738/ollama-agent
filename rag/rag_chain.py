from config import llm
from .retriever import retrieve_documents

def answer_question(question):
    """
    Retrieve relevant documents and answer the user's question.
    """
    # Retrieve relevant chunks
    documents = retrieve_documents(question)

    # Combine all chunks into one context string
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, say:
"I don't know based on the provided documents."

Context:
---------
{context}
---------

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content