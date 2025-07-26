from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.agent_graph import graph as graph
from starlette.responses import JSONResponse
# import os
import uvicorn
from src.save_md import save_md

app = FastAPI(title="Travel Agent API", description="API for Travel Agent and Expense Planner")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return "Welcome to the Travel Agent API!"


@app.post("/query")
async def query_travel_agent(query : str):
    # print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
    messages={"messages": [query]}
    output = graph.invoke(messages)

    if isinstance(output, dict) and "messages" in output:
        final_output = output["messages"][-1].content
    else:
        final_output = str(output)
    
    path = save_md(final_output)
    return JSONResponse(content={
        "response": final_output,
        "Result": f'LLM result saved at {path}!'
    })

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, host='0.0.0.0')