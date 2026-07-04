from fastapi import APIRouter
from agent.graph import graph

from api.models import ChatRequest
from api.upload import router as upload_router

router = APIRouter()
router.include_router(upload_router)


@router.post("/chat")
def chat(request: ChatRequest):
    state = {
        "messages": [
            f"User: {request.message}"
        ],
        "next_action": "",
        "tool_name": "",
        "tool_input": "",
        "tool_result": "",
        "approved": False
    }
    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }
    
    result = graph.invoke(state, config=config)
    
    return {
        "answer": result["messages"][-1]
    }