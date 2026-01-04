import time
from fastmcp import FastMCP,Context
#from passlib.context import CryptContext
import secrets
from fastmcp.server.dependencies import get_http_headers
from fastmcp.server.middleware import Middleware
from fastmcp.exceptions import ToolError
from fastapi import FastAPI

mcp = FastMCP("AuthLab Username Password Demo")

#pwd = CryptContext(schemes=["bcrypt"],deprecated = "auto")

#Idetally users will be in DB
# USERS = {
#     "admin":pwd.hash("admin@123"),
#     "user":pwd.hash("user@123") 
# }
USERS = {
    "admin":"admin@123",
    "user":"user@123"
}

SESSION_TTL_SECOUNDS = 60*60 # i hours
SESSIONS : dict[str, dict] = {}

def issue_token(username:str) -> str| None:
    token = secrets.token_urlsafe(32)
    SESSIONS[token] = {
        "user":username,
        "exp":SESSION_TTL_SECOUNDS
    }
    return token

def validate_token(token:str) -> str|None:
    session = SESSIONS.get(token)
    if not session:
        return None
    if session["exp"] < time.time():
        return None
    return session["user"]
        
    
#Bad Idea
@mcp.tool("auth_login")
def auth_login(username:str,password:str):
    stored_hash = USERS.get(username)
    if not stored_hash:
        raise PermissionError("invalid username and password")
    if password == stored_hash:
        raise PermissionError("Invalid username or password")
    
    return{
        "session_token":issue_token(username),
        "token_type": "Bearer",
        "expires_in": SESSION_TTL_SECOUNDS
    }
    
    
# @mcp.middleware
# async def auth_middleware(ctx:Context,call_next):
#     headers = get_http_headers()
#     auth = headers.get("authorization","")
#     if auth.lower().startswith("bearer "):
#         token = auth.split(" ")[1].strip()
#         username = validate_token(token)
#         if username:
#             ctx.set_state("username",username)
            
#     return await call_next(ctx)

class SessionAuthMiddleWare(Middleware):
    async def on_call_tool(self, context, call_next):
        tool_name = context.message.tool_name
        if tool_name == "auth_login":
            # skip auth for login
            return await call_next(context)
        headers = get_http_headers()
        auth = headers.get("authorization","")
        if auth.lower().startswith("bearer "):
            token = auth.split(" ")[1].strip()
            username = validate_token(token)
            if username:
                context.set_state("username",username)
        else:
            raise ToolError("missing authorization: Bearer Token")
                
        return await call_next(context)

@mcp.tool()
def whoami(ctx:Context):
    user = ctx.get_state("username")
    if not user:
        raise PermissionError("Not logged in")
    return user


mcp.add_middleware(SessionAuthMiddleWare())
mcp_app = mcp.http_app(path="/")
app = FastAPI(lifespan=mcp_app.lifespan)
app.mount("/mcp",mcp_app)

@app.get("/")
def default_get():
    return {"hellow":"world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=18000)