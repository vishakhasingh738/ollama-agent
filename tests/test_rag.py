"""Tests for RAG chain."""

from rag.rag_chain import answer_question

def test_rag_chain():
    """Interactive test for the RAG chain."""
    while True:
        question = input("Question: ")
        if question.lower() == "exit":
            break
        answer = answer_question(question)
        print("\nAnswer:")
        print(answer)
        print("-" * 50)

if __name__ == "__main__":
    test_rag_chain()
