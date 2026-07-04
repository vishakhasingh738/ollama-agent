from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

llm = ChatOllama(
    model="llama3.2",
    temperature=0.2,
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)