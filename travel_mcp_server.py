#!/usr/bin/env python3

import os
from fastmcp import FastMCP
from auth_middleware import Auth0JWTMiddleware
from travel_tools import register_travel_tools

# Load environment variables
AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]        # eg: dev-xxxx.us.auth0.com
AUTH0_AUDIENCE = os.environ["AUTH0_AUDIENCE"]    # eg: https://travel-mcp/api

# Auth Middleware
auth = Auth0JWTMiddleware(
    domain=AUTH0_DOMAIN,
    audience=AUTH0_AUDIENCE
)

# Create MCP Server
mcp = FastMCP(
    name="Travel MCP Server",
    auth=auth
)

# Register tools
register_travel_tools(mcp)

# Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Travel MCP Server running on port {port}")
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
