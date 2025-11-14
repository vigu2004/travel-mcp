#!/usr/bin/env python3
"""
Travel MCP Server (Auth0-secured)
This server exposes tools for the Travel Agent front-end.
"""

import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider
from travel_tools import register_travel_tools  # your tools file

# --------------------------------------------------------------------
# ENVIRONMENT VARIABLES (required)
# --------------------------------------------------------------------
AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]                 # ex: dev-xxxx.us.auth0.com
AUTH0_AUDIENCE = os.environ["AUTH0_AUDIENCE"]             # ex: https://travel-mcp/api

# --------------------------------------------------------------------
# AUTH0 CONFIGURATION
# --------------------------------------------------------------------
auth = Auth0Provider(
    issuer=f"https://{AUTH0_DOMAIN}/",    # IMPORTANT: issuer, not domain
    audience=AUTH0_AUDIENCE
)

# --------------------------------------------------------------------
# CREATE MCP SERVER
# --------------------------------------------------------------------
mcp = FastMCP(
    name="Travel MCP Server (Auth0 Secured)",
    auth=auth,
)

# Register your tool definitions
register_travel_tools(mcp)

# --------------------------------------------------------------------
# SERVER ENTRY POINT
# --------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Travel MCP Server running on port {port}")
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
