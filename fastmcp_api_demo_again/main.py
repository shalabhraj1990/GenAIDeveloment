import asyncio
from fastmcp import FastMCP,Context
from fastapi import FastAPI
import uvicorn

mcp = FastMCP()

@mcp.tool()
def add(a:int , b:int) -> int:
    return a + b

@mcp.tool()
def subtract(a:int , b:int) -> int:
    return a - b

@mcp.tool()
async def some_long_running(a:int , b:int , ctx:Context) -> int:
    ctx.info("staring long running code")
    asyncio.sleep(0.1)
    ctx.info("Fineshed long running task")
    return a * b

mcp_app = mcp.http_app(path="/")

app = FastAPI(lifespan=mcp_app.lifespan)
app.mount("/mcp",mcp_app)
@app.get("/")
def read() -> dict:
    return {"hello":"world"}
if __name__ == "__main__":
    
    #starting fastapi
    uvicorn.run(app,host="0.0.0.0",port=8000)
