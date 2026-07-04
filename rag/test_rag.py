from .rag_chain import answer_question

while True:
    question = input("Question: ")
    if question.lower() == "exit":
        break
    answer = answer_question(question)
    print("\nAnswer:")
    print(answer)
    print("-" * 50)