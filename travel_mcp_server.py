#!/usr/bin/env python3

import os
from fastmcp import FastMCP
from auth_middleware import Auth0JWTMiddleware
from travel_tools import register_travel_tools

AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
AUTH0_AUDIENCE = os.environ["AUTH0_AUDIENCE"]

auth = Auth0JWTMiddleware(
    domain=AUTH0_DOMAIN,
    audience=AUTH0_AUDIENCE
)

mcp = FastMCP(
    name="Travel MCP Server",
    auth=auth  # <-- just pass the callable middleware
)

register_travel_tools(mcp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Travel MCP Server running on port {port}")
    mcp.run_http(
    port=port
    )

