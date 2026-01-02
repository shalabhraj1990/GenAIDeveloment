from mcp.server.fastmcp import FastMCP,Context
from mcp.types import SamplingMessage,TextContent

mcp = FastMCP("sampling demo server")

@mcp.tool()
async def explain(ctx:Context,topic:str) -> str:
    """
   Ask MCP client to generate an explanation via mcp sampling
    """
    prompt = f"Explain {topic} in simple terms"
    results = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                content=TextContent(
                    type="text",
                    text=prompt
                ),
                role="user"
            )
        ],
        system_prompt="you are a helful teacher",
        max_tokens=400
        
    )
    
    return results.content

if __name__ == "__main__":
    mcp.run(transport="stdio")