#!/usr/bin/env python3
"""
Travel MCP Server (Auth0-secured)
Exposes tools for the Travel Agent website.
"""

import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider
from travel_tools import register_travel_tools  # your travel tools


AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
AUTH0_AUDIENCE = os.environ["AUTH0_AUDIENCE"]

auth = Auth0Provider(
    f"https://{AUTH0_DOMAIN}/",   # issuer
    AUTH0_AUDIENCE               # audience
)

# --------------------------------------------------------------------
# CREATE MCP SERVER
# --------------------------------------------------------------------
mcp = FastMCP(
    name="Travel MCP Server (Auth0 Secured)",
    auth=auth,
)

# Register travel tools
register_travel_tools(mcp)

# --------------------------------------------------------------------
# ENTRY POINT
# --------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Travel MCP Server running on port {port}")

    mcp.run(
        transport="http",      # HTTP transport for Render / Cloud Run
        host="0.0.0.0",
        port=port
    )
