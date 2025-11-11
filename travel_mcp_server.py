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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    
    print("\n" + "="*70)
    print("🚀 TRAVEL COMPANY MCP SERVER (FastMCP)")
    print("="*70)
    print(f"URL: http://localhost:{port}")
    print(f"Endpoint: http://localhost:{port}/mcp/")
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

