from fastmcp import FastMCP

mcp = FastMCP("fastmcp server")

def process_data(input:str) -> str:
    """
    Docstring for process_data
    
    :param input: Description
    :type input: str
    :return: Description
    :rtype: str
    """
    return f"Proccessed: {input}"

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
