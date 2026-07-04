"""
Enterprise Document Copilot - Main Application Entry Point

This application provides:
1. FastAPI HTTP server (api.main:app)
2. Agent-based document processing and retrieval
3. RAG (Retrieval Augmented Generation) capabilities
"""

import uvicorn
import sys

def run_api(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """Run the FastAPI server."""
    print(f"\n{'='*50}")
    print("Starting Enterprise Document Copilot API")
    print(f"{'='*50}")
    print(f"API Server: http://{host}:{port}")
    print(f"Docs: http://{host}:{port}/docs")
    print(f"{'='*50}\n")
    
    uvicorn.run(
        "api.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


if __name__ == "__main__":
    # Run API by default
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "api":
            reload = "--reload" in sys.argv
            run_api(reload=reload)
        elif cmd == "evaluate":
            from evaluate import evaluate_agent
            print("Running agent evaluation...")
            # Add evaluation logic here
        else:
            print(f"Unknown command: {cmd}")
            print("Usage: python app.py [api|evaluate]")
    else:
        run_api(reload=True)