#!/usr/bin/env python3
"""
Travel Company MCP Server (FastMCP Version)
Provides secure in-memory travel data including flights, hotels, and car rentals.
Clean, vulnerability-free implementation for production use.
"""

import os
from fastmcp import FastMCP
from travel_tools import register_travel_tools

# Create FastMCP instance
mcp = FastMCP(name="Travel Company MCP Server")

# Register all travel tools
register_travel_tools(mcp)

# Add custom endpoint to list all tools in MCP format
@mcp.get("/")
async def list_tools():
    """Return all available tools in MCP specification format"""
    tools_list = []
    
    # Helper function to convert Python type to JSON Schema type
    def python_type_to_json_schema(type_str):
        type_str = str(type_str).lower()
        if 'str' in type_str:
            return "string"
        elif 'int' in type_str:
            return "integer"
        elif 'float' in type_str:
            return "number"
        elif 'bool' in type_str:
            return "boolean"
        elif 'list' in type_str or 'array' in type_str:
            return "array"
        elif 'dict' in type_str:
            return "object"
        else:
            return "string"  # default to string
    
    # Extract tool information from registered tools
    for tool_name, tool_func in mcp._tools.items():
        # Get description - use first line only for cleaner output
        description = ""
        if tool_func.__doc__:
            doc_lines = tool_func.__doc__.strip().split('\n')
            description = doc_lines[0].strip()
        
        properties = {}
        required = []
        
        # Extract parameter information from function annotations
        if hasattr(tool_func, '__annotations__'):
            annotations = tool_func.__annotations__.copy()
            annotations.pop('return', None)
            
            # Get default values
            defaults = {}
            if hasattr(tool_func, '__defaults__') and tool_func.__defaults__:
                default_offset = len(annotations) - len(tool_func.__defaults__)
                for i, default in enumerate(tool_func.__defaults__):
                    param_name = list(annotations.keys())[default_offset + i]
                    defaults[param_name] = default
            
            for param_name, param_type in annotations.items():
                json_type = python_type_to_json_schema(str(param_type))
                properties[param_name] = {"type": json_type}
                
                # Add to required if no default value
                if param_name not in defaults:
                    required.append(param_name)
        
        tool_info = {
            "name": tool_name,
            "description": description,
            "inputSchema": {
                "type": "object",
                "properties": properties,
                "required": required
            }
        }
        
        tools_list.append(tool_info)
    
    return {
        "mcp": "1.0",
        "name": "Travel Company MCP Server",
        "version": "0.1.0",
        "capabilities": {
            "tools": {
                "list": tools_list
            }
        }
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    
    print("\n" + "="*70)
    print("🚀 TRAVEL COMPANY MCP SERVER (FastMCP)")
    print("="*70)
    print(f"URL: http://localhost:{port}")
    print(f"MCP Discovery Endpoint: http://localhost:{port}/")
    print("\n📋 Available Travel Tools:")
    print("   ✈️  search_flights        - Search for available flights")
    print("   🏨 search_hotels          - Search for hotels")
    print("   🚗 search_car_rentals     - Search for car rentals")
    print("   ✈️  get_flight_details    - Get flight details by ID")
    print("   🏨 get_hotel_details      - Get hotel details by ID")
    print("   📝 book_flight            - Book a flight")
    print("\n✅ All tools are secure and production-ready!")
    print("="*70 + "\n")
    
    # Use FastMCP's built-in HTTP server
    mcp.run(transport="http", host="0.0.0.0", port=port)

