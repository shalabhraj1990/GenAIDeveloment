from pathlib import Path
from mcp.server.fastmcp import FastMCP
from data.customers import CUSTOMERS
from data.restaurants import RESTARAUNTS
from data.orders import ORDERS
#import data.orders as ORDERS
from model.models import Customer,Order,Restaurant

mcp = FastMCP(name="swiggy-mcp",
              website_url="https://github.com/shalabhraj1990")

##tools
@mcp.tool()
def get_customer_summary(cusomer_id:str) -> Customer | None :
    '''
    Docstring for get_customer_summary
    
    :param cusomer_id: Description
    :type cusomer_id: str
    :return: Description
    :rtype: dict | None
    '''
    for customer in CUSTOMERS: #Note you can write this code as comprehension form
        if customer['customerId'] == cusomer_id:
            return Customer(**customer)

    return None

@mcp.tool()
def get_order_information(order_id:str) -> Order | None :
    '''
    Docstring for get_order_information
    
    :param order_id: Description
    :type order_id: str
    :return: Description
    :rtype: list
    '''
    for ord in ORDERS: #Note you can write this code as comprehension form
        if ord['orderId'] == order_id:
            return Order(**ord)

    return None
@mcp.tool()
def get_resturant_information(resturantr_id:str) -> Restaurant | None :
    '''
    Docstring for get_resturant_information
    
    :param resturantr_id: Description
    :type resturantr_id: str
    :return: Description
    :rtype: list
    '''
    for returant in RESTARAUNTS: #Note you can write this code as comprehension form
        if returant['restaurantId'] == resturantr_id:
            return Restaurant(**returant)

    return None

@mcp.tool()
def get_refund_policy_info() -> str:
    return get_refund_policy()

@mcp.tool()
def get_complaint_resolution_info() -> str:
    return get_complaint_resolution()

##resouces used by LLM for resoning
@mcp.resource("policy://refund")
def get_refund_policy() -> str:
    """
    Docstring for get_refund_policy
    
    :return: Description
    :rtype: str
    """
    return read_markdown_file('data/refundpolicy.md')

@mcp.resource("complaint://{ctype}")
def get_complaint_resolution(ctype) -> str:
    """
    Docstring for get_complaint_resolution
    
    :param ctype: Description
    :return: Description
    :rtype: str
    """
    return read_markdown_file('data/latetimedelivery.md')



def read_markdown_file(file_path):
    """
    Reads the content of a Markdown file with UTF-8 encoding.

    Args:
        file_path (str): The path to the Markdown file.

    Returns:
        str: The content of the Markdown file as a string.
    """
    try:
        current_dir = Path(__file__).parent
        full_file_path = current_dir.joinpath(file_path) 
        with open(full_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{full_file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    
if __name__ == "__main__":
    #mcp.run(transport="stdio")
    mcp.run(transport="streamable-http")
        