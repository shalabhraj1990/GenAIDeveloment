from mcp.server.fastmcp import FastMCP

mcp = FastMCP("steamable-http-mcp")
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



if __name__ == "__main__":
    mcp.run(transport="streamable-http")