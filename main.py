#!/usr/bin/env python3

import os
from fastapi import FastAPI
import uvicorn

from fastmcp import FastMCP
from travel_tools import register_travel_tools

# ----------------------------------------------------------
# 1. Create MCP server
# ----------------------------------------------------------
mcp = FastMCP(name="Travel MCP Server")
register_travel_tools(mcp)

# ----------------------------------------------------------
# 2. Create FastAPI app
# ----------------------------------------------------------
app = FastAPI()

# Root health check — so Render sees service alive
@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Travel MCP Server running",
        "mcp_endpoint": "/mcp"
    }

# ----------------------------------------------------------
# 3. Mount MCP HTTP server under /mcp
# ----------------------------------------------------------
# This gives you:
# /mcp/.well-known/mcp/manifest.json
# /mcp/  (SSE streaming endpoint)
app.mount("/mcp", mcp.http_app(path="/mcp"))

# ----------------------------------------------------------
# 4. Uvicorn entrypoint for local + Render
# ----------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
    )
