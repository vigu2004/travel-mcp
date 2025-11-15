#!/usr/bin/env python3

import os
from fastmcp import FastMCP

from travel_tools import register_travel_tools


mcp = FastMCP(
    name="Travel MCP Server",

)
register_travel_tools(mcp)
if __name__ == "__main__":
  
    
    # Run with HTTP transport
    mcp.run()