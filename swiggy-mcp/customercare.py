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
def get_order_information(order_id:str) -> Order :
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
def get_resturant_information(resturantr_id:str) -> Restaurant :
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


##resouces used by LLM for resoning
@mcp.resource("policy://refund")
def get_refund_policy() -> str:
    """
    Docstring for get_refund_policy
    
    :return: Description
    :rtype: str
    """
    lines = []
    with open("data/refundpolicy.md") as refund:
        lines = refund.readlines()
    return "\n".join(lines)

@mcp.resource("complaint://{ctype}")
def get_complaint_resolution(ctype) -> str:
    """
    Docstring for get_complaint_resolution
    
    :param ctype: Description
    :return: Description
    :rtype: str
    """
    lines = []
    with open("data/latetimedelivery.md") as complaint:
        lines = complaint.readlines()
    return "\n".join(lines)

    
if __name__ == "__main__":
    mcp.run(transport="stdio")
        