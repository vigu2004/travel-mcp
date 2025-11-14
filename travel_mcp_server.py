#!/usr/bin/env python3
"""
Travel MCP Server (Auth0-secured)
Exposes tools for the Travel Agent website.
"""

import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider
from travel_tools import register_travel_tools  # your travel tools

# --------------------------------------------------------------------
# ENVIRONMENT VARIABLES
# --------------------------------------------------------------------
AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]           # example: dev-xxxx.us.auth0.com
AUTH0_AUDIENCE = os.environ["AUTH0_AUDIENCE"]       # example: https://travel-mcp/api

# --------------------------------------------------------------------
# AUTH0 CONFIGURATION
# --------------------------------------------------------------------
auth = Auth0Provider(
    issuer=f"https://{AUTH0_DOMAIN}/",   # <---- IMPORTANT (correct param)
    audience=AUTH0_AUDIENCE
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
