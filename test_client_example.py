#!/usr/bin/env python3
"""
Example test client to demonstrate how to interact with the Travel MCP Server.
This shows how an AI agent would query the server.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_travel_mcp():
    """Test the travel MCP server."""
    
    # Server parameters - adjust the path to your server
    server_params = StdioServerParameters(
        command="python",
        args=["travel_mcp_server.py"],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            
            print("=" * 60)
            print("Connected to Travel MCP Server!")
            print("=" * 60)
            
            # List available tools
            tools = await session.list_tools()
            print(f"\n📋 Available Tools ({len(tools.tools)}):")
            for tool in tools.tools:
                print(f"  • {tool.name}: {tool.description}")
            
            print("\n" + "=" * 60)
            print("TEST 1: Search for flights from New York to London")
            print("=" * 60)
            
            # Test 1: Search flights
            result = await session.call_tool(
                "search_flights",
                arguments={
                    "origin": "New York",
                    "destination": "London"
                }
            )
            print(result.content[0].text)
            
            print("\n" + "=" * 60)
            print("TEST 2: Search for 4+ star hotels in London")
            print("=" * 60)
            
            # Test 2: Search hotels
            result = await session.call_tool(
                "search_hotels",
                arguments={
                    "location": "London",
                    "min_rating": 4
                }
            )
            print(result.content[0].text)
            
            print("\n" + "=" * 60)
            print("TEST 3: Search for car rentals at London Airport")
            print("=" * 60)
            
            # Test 3: Search car rentals
            result = await session.call_tool(
                "search_car_rentals",
                arguments={
                    "location": "London Airport"
                }
            )
            print(result.content[0].text)
            
            print("\n" + "=" * 60)
            print("TEST 4: Get flight details for FL001")
            print("=" * 60)
            
            # Test 4: Get flight details
            result = await session.call_tool(
                "get_flight_details",
                arguments={
                    "flight_id": "FL001"
                }
            )
            print(result.content[0].text)
            
            print("\n" + "=" * 60)
            print("TEST 5: Book flight FL001 for John Doe")
            print("=" * 60)
            
            # Test 5: Book a flight
            result = await session.call_tool(
                "book_flight",
                arguments={
                    "flight_id": "FL001",
                    "passenger_name": "John Doe",
                    "num_seats": 2
                }
            )
            print(result.content[0].text)
            
            print("\n" + "=" * 60)
            print("All tests completed successfully! ✅")
            print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_travel_mcp())

