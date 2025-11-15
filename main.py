#!/usr/bin/env python3
import os
from fastmcp import FastMCP
from travel_tools import register_travel_tools

# Create MCP server
mcp = FastMCP("Travel MCP Server")

# Register tools
register_travel_tools(mcp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
        path="/mcp"
    )
