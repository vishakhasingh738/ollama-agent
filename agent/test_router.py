from agent.router import route_question

questions = [
    "What is our leave policy?",
    "245 * 18",
    "Who won yesterday's IPL match?"
]

for q in questions:
    print(q)
    print(route_question(q))
    print("-" * 30)