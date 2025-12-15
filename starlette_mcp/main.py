from starlette.applications import Starlette
from starlette.routing import Mount
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sse-demo")
@mcp.tool()
def add(a:int , b:int) -> int|None :
    '''
    Docstring for add
    
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    :return: Description
    :rtype: int | None
    '''
    return a + b
@mcp.tool()
def echo(message:str) -> str | None :
    '''
    Docstring for echo
    
    :param message: Description
    :type message: str
    :return: Description
    :rtype: str | None
    '''
    return f"you typed :{message}"


app = Starlette(routes=[
    Mount("/",app=mcp.sse_app())
])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)