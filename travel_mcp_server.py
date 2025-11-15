#!/usr/bin/env python3

import os
from fastmcp import FastMCP

from travel_tools import register_travel_tools


mcp = FastMCP(
    name="Travel MCP Server",

)
register_travel_tools(mcp)
if __name__ == "__main__":
    # Get port from environment variable (Cloud Run sets this)
    port = int(os.environ.get("PORT", 8080))
    
    # Run with HTTP transport
    mcp.run(
        transport="http",
        port=port,
        host="0.0.0.0"
    )