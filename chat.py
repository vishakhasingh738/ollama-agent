from config import llm
from prompts import SYSTEM_PROMPT
from memory import ConversationMemory
from agent1 import agent



def start_chat():

    print("=" * 40)
    print("AI Assistant")
    print("Type 'exit' to quit")
    print("=" * 40)
    memory = ConversationMemory()

    while True:

        memory.add("system", SYSTEM_PROMPT)
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if question.lower() == "reset":
            memory.clear()
            memory.add("system", SYSTEM_PROMPT)
            print("Conversation cleared.")
            continue

        memory.add("user", question)

        result = agent.invoke(
            {
                "messages": memory.get()
            }
        )

        ai_response = result["messages"][-1]
        # response = llm.invoke(memory.get())
        memory.add("assistant", ai_response.content)

        print(f"\nAI: {ai_response.content}")