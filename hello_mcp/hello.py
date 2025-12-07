import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("hello-mcp")

# define tools
@mcp.tool()
def add(a:int|float , b:int|float) -> int|float:
    """
    Docstring for add
    
    :param a: Description
    :type a: int | float
    :param b: Description
    :type b: int | float
    :return: Description
    :rtype: int | float
    
    """
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")