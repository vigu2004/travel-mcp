from fastmcp import FastMCP
from travel_tools import register_travel_tools

def debug():
    print("DEBUG: register_travel_tools CALLED")

mcp = FastMCP("x")

print("Before register:", mcp._tool_manager._tools.keys())

register_travel_tools(mcp)

print("After register:", mcp._tool_manager._tools.keys())
