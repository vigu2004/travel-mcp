#!/usr/bin/env python3
"""
Travel MCP Server (Auth0-secured)
"""

import os
from fastmcp import FastMCP
from fastmcp.auth import Auth0Provider   # <---- NEW CORRECT IMPORT
from travel_tools import register_travel_tools

# ENV
AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
AUTH0_AUDIENCE = os.environ["AUTH0_AUDIENCE"]

# AUTH0 PROVIDER (new API)
auth = Auth0Provider(
    domain=AUTH0_DOMAIN,
    audience=AUTH0_AUDIENCE
)

# MCP server
mcp = FastMCP(
    name="Travel MCP Server (Auth0 Secured)",
    auth=auth
)

register_travel_tools(mcp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Travel MCP Server running on {port}")
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
