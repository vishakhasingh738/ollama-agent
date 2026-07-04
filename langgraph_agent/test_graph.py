from langgraph_agent.graph import graph

state = {

    "messages": [

        "User: My favorite language is Python."

    ],

    "next_action": "",

    "tool_name": "",

    "tool_input": "",

    "tool_result": ""

}


config = {

    "configurable":{

        "thread_id":"123"

    }

}
result = graph.invoke(state, config=config)

print(result["messages"])