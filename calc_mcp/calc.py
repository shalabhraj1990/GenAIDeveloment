from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="calc-mcp")

@mcp.tool()
def add(a: int | float , b: int | float) -> int|float:
    '''
    Docstring for add
    
    :param a: Description
    :type a: int | float
    :param b: Description
    :type b: int | float
    :return: Description
    :rtype: int | float
    '''
    return a + b

@mcp.tool()
def sub(a:int|float,b:int|float) -> int | float :
    '''
    Docstring for sub
    
    :param a: Description
    :type a: int | float
    :param b: Description
    :type b: int | float
    :return: Description
    :rtype: int | float
    '''
    return a - b

@mcp.tool()
def mul(a:int|float,b:int|float) -> int | float:
    '''
    Docstring for mul
    
    :param a: Description
    :type a: int | float
    :param b: Description
    :type b: int | float
    :return: Description
    :rtype: int | float
    '''
    return a * b

@mcp.tool()
def div(a:int|float,b:int|float) -> int|float:
    '''
    Docstring for div
    
    :param a: Description
    :type a: int | float
    :param b: Description
    :type b: int | float
    :return: Description
    :rtype: int | float
    '''
    return a/b

@mcp.resource(uri="data://operations")
def operations() -> list[str]:
    return ["add","sub","mul","div"]

@mcp.resource(uri="data://operations/{intent}")
def get_operation(intent:str) -> str:
    if intent == "add":
        return "ADD"
    else:
        return "i Don't know"
    

if __name__ == "__main__":
    mcp.run(transport="stdio")