from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider
import os

AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
AUTH0_AUDIENCE = os.environ["AUTH0_AUDIENCE"]

auth = Auth0Provider(
    issuer=f"https://{AUTH0_DOMAIN}/",
    audience=AUTH0_AUDIENCE
)

mcp = FastMCP(
    name="Travel MCP Server (Auth0 Secured)",
    auth=auth
)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
