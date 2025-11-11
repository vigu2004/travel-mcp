#!/usr/bin/env python3
"""
Travel Company MCP Server (FastMCP Version)
Provides secure in-memory travel data including flights, hotels, and car rentals.
Clean, vulnerability-free implementation for production use.
"""

import os
import uvicorn
from fastmcp import FastMCP
from travel_tools import register_travel_tools

# Create FastMCP instance
mcp = FastMCP(name="Travel Company MCP Server")

# Register all travel tools
register_travel_tools(mcp)

# --- Simple ASGI CORS wrapper (works by wrapping an ASGI app) ---
def make_cors_app(asgi_app):
    async def app(scope, receive, send):
        # Only handle HTTP
        if scope["type"] != "http":
            await asgi_app(scope, receive, send)
            return

        # Handle preflight OPTIONS directly
        if scope["method"] == "OPTIONS":
            headers = [
                (b"access-control-allow-origin", b"*"),
                (b"access-control-allow-methods", b"GET, POST, OPTIONS, PUT, DELETE"),
                (b"access-control-allow-headers", b"authorization, content-type, x-requested-with"),
                (b"access-control-max-age", b"3600"),
            ]
            await send({
                "type": "http.response.start",
                "status": 204,
                "headers": headers,
            })
            await send({"type": "http.response.body", "body": b"", "more_body": False})
            return

        # Wrap send to inject CORS headers on real responses
        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                headers = dict(message.setdefault("headers", []))
                # append headers (keep existing)
                message["headers"].extend([
                    (b"access-control-allow-origin", b"*"),
                    (b"access-control-allow-credentials", b"true"),
                ])
            await send(message)

        await asgi_app(scope, receive, send_wrapper)

    return app

# Get the HTTP ASGI app from FastMCP and wrap with CORS
asgi_app = make_cors_app(mcp.http_app())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    
    print("\n" + "="*70)
    print("🚀 TRAVEL COMPANY MCP SERVER (FastMCP)")
    print("="*70)
    print(f"URL: http://localhost:{port}")
    print("\n📋 Available Travel Tools:")
    print("   ✈️  search_flights        - Search for available flights")
    print("   🏨 search_hotels          - Search for hotels")
    print("   🚗 search_car_rentals     - Search for car rentals")
    print("   ✈️  get_flight_details    - Get flight details by ID")
    print("   🏨 get_hotel_details      - Get hotel details by ID")
    print("   📝 book_flight            - Book a flight")
    print("\n✅ All tools are secure and production-ready!")
    print("="*70 + "\n")
    
    uvicorn.run(asgi_app, host="0.0.0.0", port=port)

