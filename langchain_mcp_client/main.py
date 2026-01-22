#imports
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model


async def main():
    client = MultiServerMCPClient({
        "hello-mcp":{
            "transport":"stdio",
            "command":"python",
            "args":["S:\\Shalabh_Private\\code\\GIT\\GenAIDeveloment\\langchain_mcp_client\\server.py"]
        }
    })
    tools = await client.get_tools()
    for tool in tools:
        print(tool)
    
    llm = init_chat_model("gemini-2.5-flash-lite",model_provider="google_vertexai") 
    agent = create_agent(model=llm, tools=tools)
    
    result = await agent.ainvoke({
        "messages":[
            {
                "role":"user",
                "content":"what is 2+2"
            }
        ]
    })
    print(result)
    

if __name__ == "__main__":
    asyncio.run(main())