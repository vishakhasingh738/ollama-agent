from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="AI Assistant",
    version="1.0.0"
)
app.include_router(router)
@app.get("/")
def home():

    return {

        "message":"AI Assistant Running"

    }