"""
Mock MCP Server for Testing ArmorIQ Proxy
This server simulates a real MCP server with business logic endpoints
that ArmorIQ Proxy will protect with policies.
"""
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import uvicorn
from datetime import datetime

app = FastAPI(title="Mock MCP Server")

# ============================================================================
# MOCK DATABASE
# ============================================================================

# In-memory user database
USERS_DB = {
    1: {"id": 1, "name": "Alice Johnson", "email": "alice@company.com", "role": "admin"},
    2: {"id": 2, "name": "Bob Smith", "email": "bob@company.com", "role": "developer"},
    3: {"id": 3, "name": "Charlie Davis", "email": "charlie@company.com", "role": "viewer"},
}

# In-memory files database
FILES_DB = {
    "/home/alice/project/app.py": {"content": "print('Hello World')", "owner": "alice"},
    "/home/bob/notes.txt": {"content": "Important notes", "owner": "bob"},
    "/etc/passwd": {"content": "root:x:0:0:root:/root:/bin/bash", "owner": "root"},
}

# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

class CreateUserRequest(BaseModel):
    name: str
    email: str
    role: str

class UpdateUserRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None

class ReadFileRequest(BaseModel):
    path: str

class WriteFileRequest(BaseModel):
    path: str
    content: str

class ExecuteCommandRequest(BaseModel):
    command: str

class DatabaseQueryRequest(BaseModel):
    query: str

class MCPToolRequest(BaseModel):
    tool: str
    arguments: Dict[str, Any]

class JSONRPCRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: Optional[Dict[str, Any]] = None
    id: Optional[int] = 1

# ============================================================================
# MCP METADATA ENDPOINTS (Discovery)
# ============================================================================

@app.get("/.well-known/mcp.json")
def mcp_wellknown():
    """MCP discovery endpoint"""
    return {
        "protocol": "mcp",
        "version": "1.0.0",
        "name": "Company User Management MCP Server",
        "description": "MCP server for user management and file operations",
        "capabilities": {
            "tools": ["read_file", "execute_command", "write_file", "database_query"],
            "resources": ["users", "files"],
            "prompts": ["code_review", "security_audit"]
        },
        "endpoints": {
            "users": "/api/users",
            "files": "/api/files",
            "mcp_tools": "/mcp/execute-tool",
            "jsonrpc": "/api/mcp"
        }
    }

@app.get("/api/mcp")
def mcp_api_get():
    """Get MCP server information (GET method)"""
    return {
        "serverInfo": {
            "name": "company-user-management",
            "version": "1.0.0",
            "description": "Manages company users and file operations"
        },
        "tools": [
            {
                "name": "read_file",
                "description": "Read files from the filesystem",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Absolute file path"}
                    },
                    "required": ["path"]
                }
            },
            {
                "name": "execute_command",
                "description": "Execute system commands (DANGEROUS!)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Shell command to execute"}
                    },
                    "required": ["command"]
                }
            },
            {
                "name": "write_file",
                "description": "Write content to files",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["path", "content"]
                }
            },
            {
                "name": "database_query",
                "description": "Execute SQL queries",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "SQL query"}
                    },
                    "required": ["query"]
                }
            }
        ],
        "resources": [
            {"uri": "/api/users", "name": "Users", "description": "Company users"},
            {"uri": "/api/files", "name": "Files", "description": "File system access"}
        ],
        "prompts": [
            {"name": "code_review", "description": "Review code with file access"},
            {"name": "security_audit", "description": "Audit security"}
        ]
    }

# ============================================================================
# USER MANAGEMENT ENDPOINTS (Business Logic)
# ============================================================================

@app.get("/api/users")
def list_users():
    """List all users - Requires READ permission"""
    return {
        "success": True,
        "users": list(USERS_DB.values()),
        "count": len(USERS_DB)
    }

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    """Get specific user - Requires READ permission"""
    if user_id not in USERS_DB:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "success": True,
        "user": USERS_DB[user_id]
    }

@app.post("/api/users")
def create_user(user: CreateUserRequest):
    """Create new user - Requires CREATE permission"""
    new_id = max(USERS_DB.keys()) + 1 if USERS_DB else 1
    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }
    USERS_DB[new_id] = new_user
    
    return {
        "success": True,
        "message": "User created successfully",
        "user": new_user
    }

@app.put("/api/users/{user_id}")
@app.patch("/api/users/{user_id}")
def update_user(user_id: int, user: UpdateUserRequest):
    """Update user - Requires UPDATE permission"""
    if user_id not in USERS_DB:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.name:
        USERS_DB[user_id]["name"] = user.name
    if user.email:
        USERS_DB[user_id]["email"] = user.email
    if user.role:
        USERS_DB[user_id]["role"] = user.role
    
    return {
        "success": True,
        "message": "User updated successfully",
        "user": USERS_DB[user_id]
    }

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    """Delete user - Requires DELETE permission"""
    if user_id not in USERS_DB:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = USERS_DB.pop(user_id)
    
    return {
        "success": True,
        "message": f"User {deleted_user['name']} deleted successfully",
        "deleted_user": deleted_user
    }

# ============================================================================
# FILE OPERATIONS ENDPOINTS (Business Logic)
# ============================================================================

@app.get("/api/files")
def list_files():
    """List all files - Requires READ permission"""
    files = [
        {"path": path, "owner": info["owner"]}
        for path, info in FILES_DB.items()
    ]
    return {
        "success": True,
        "files": files,
        "count": len(files)
    }

@app.post("/api/files/read")
def read_file(request: ReadFileRequest):
    """Read file content - Requires READ permission"""
    if request.path not in FILES_DB:
        raise HTTPException(status_code=404, detail="File not found")
    
    file_info = FILES_DB[request.path]
    
    return {
        "success": True,
        "path": request.path,
        "content": file_info["content"],
        "owner": file_info["owner"]
    }

@app.post("/api/files/write")
def write_file(request: WriteFileRequest):
    """Write file content - Requires CREATE permission"""
    FILES_DB[request.path] = {
        "content": request.content,
        "owner": "system"
    }
    
    return {
        "success": True,
        "message": f"File written successfully: {request.path}",
        "path": request.path
    }

@app.delete("/api/files")
def delete_file(path: str):
    """Delete file - Requires DELETE permission"""
    if path not in FILES_DB:
        raise HTTPException(status_code=404, detail="File not found")
    
    deleted_file = FILES_DB.pop(path)
    
    return {
        "success": True,
        "message": f"File deleted successfully: {path}",
        "path": path,
        "owner": deleted_file["owner"]
    }

# ============================================================================
# MCP TOOL EXECUTION ENDPOINT
# ============================================================================

@app.post("/mcp/execute-tool")
async def execute_mcp_tool(request: MCPToolRequest):
    """
    Execute MCP tool by name - Requires CREATE permission
    This is the dangerous endpoint that allows calling ANY tool!
    """
    tool = request.tool
    args = request.arguments
    
    if tool == "read_file":
        if "path" not in args:
            raise HTTPException(status_code=400, detail="Missing 'path' argument")
        
        path = args["path"]
        if path not in FILES_DB:
            raise HTTPException(status_code=404, detail="File not found")
        
        return {
            "success": True,
            "tool": "read_file",
            "result": {
                "path": path,
                "content": FILES_DB[path]["content"]
            }
        }
    
    elif tool == "write_file":
        if "path" not in args or "content" not in args:
            raise HTTPException(status_code=400, detail="Missing arguments")
        
        FILES_DB[args["path"]] = {
            "content": args["content"],
            "owner": "system"
        }
        
        return {
            "success": True,
            "tool": "write_file",
            "result": {"message": f"File written: {args['path']}"}
        }
    
    elif tool == "execute_command":
        # DANGEROUS: This would execute arbitrary commands
        return {
            "success": True,
            "tool": "execute_command",
            "result": {
                "warning": "Command execution is disabled in mock mode",
                "command": args.get("command", ""),
                "output": "[SIMULATED] Command would be executed here"
            }
        }
    
    elif tool == "database_query":
        # DANGEROUS: This would execute arbitrary SQL
        return {
            "success": True,
            "tool": "database_query",
            "result": {
                "warning": "Direct SQL execution is disabled in mock mode",
                "query": args.get("query", ""),
                "rows": "[SIMULATED] Query results would appear here"
            }
        }
    
    else:
        raise HTTPException(status_code=404, detail=f"Tool not found: {tool}")

# ============================================================================
# MCP TOOL-SPECIFIC ENDPOINTS (Safer Alternative)
# ============================================================================

@app.post("/mcp/tools/read_file")
def mcp_read_file(request: ReadFileRequest):
    """Execute read_file tool - Requires CREATE permission on this specific path"""
    if request.path not in FILES_DB:
        raise HTTPException(status_code=404, detail="File not found")
    
    return {
        "success": True,
        "tool": "read_file",
        "path": request.path,
        "content": FILES_DB[request.path]["content"]
    }

@app.post("/mcp/tools/write_file")
def mcp_write_file(request: WriteFileRequest):
    """Execute write_file tool - Requires CREATE permission on this specific path"""
    FILES_DB[request.path] = {
        "content": request.content,
        "owner": "system"
    }
    
    return {
        "success": True,
        "tool": "write_file",
        "message": f"File written: {request.path}"
    }

@app.post("/mcp/tools/execute_command")
def mcp_execute_command(request: ExecuteCommandRequest):
    """Execute system command - Requires CREATE permission (DANGEROUS!)"""
    return {
        "success": True,
        "tool": "execute_command",
        "warning": "Command execution is disabled in mock mode",
        "command": request.command,
        "output": "[SIMULATED] Command would be executed here"
    }

@app.post("/mcp/tools/database_query")
def mcp_database_query(request: DatabaseQueryRequest):
    """Execute database query - Requires CREATE permission (DANGEROUS!)"""
    return {
        "success": True,
        "tool": "database_query",
        "warning": "Direct SQL is disabled in mock mode",
        "query": request.query,
        "rows": "[SIMULATED] Query results would appear here"
    }

# ============================================================================
# JSON-RPC ENDPOINT (Standard MCP Protocol)
# ============================================================================

@app.post("/")
@app.post("/api/mcp")
async def mcp_jsonrpc(request: Request):
    """Handle JSON-RPC 2.0 requests - Standard MCP protocol"""
    body = await request.json()
    method = body.get("method", "")
    request_id = body.get("id", 1)
    params = body.get("params", {})
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {
                    "name": "company-user-management",
                    "version": "1.0.0"
                },
                "capabilities": {
                    "tools": {},
                    "resources": {},
                    "prompts": {}
                }
            }
        }
    
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "tools": [
                    {"name": "read_file", "description": "Read files from filesystem"},
                    {"name": "execute_command", "description": "Execute system commands"},
                    {"name": "write_file", "description": "Write content to files"},
                    {"name": "database_query", "description": "Execute SQL queries"}
                ]
            }
        }
    
    elif method == "tools/call":
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        
        # This allows calling ANY tool via JSON-RPC
        # ArmorIQ would need body inspection to control this
        
        if tool_name == "read_file":
            path = arguments.get("path", "")
            if path not in FILES_DB:
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {"code": 404, "message": "File not found"}
                }
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": FILES_DB[path]["content"]
                }
            }
        
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32601, "message": f"Tool not implemented: {tool_name}"}
            }
    
    elif method == "resources/list":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "resources": [
                    {"uri": "/api/users", "name": "Users"},
                    {"uri": "/api/files", "name": "Files"}
                ]
            }
        }
    
    elif method == "prompts/list":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "prompts": [
                    {"name": "code_review", "description": "Review code"},
                    {"name": "security_audit", "description": "Audit security"}
                ]
            }
        }
    
    else:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": -32601,
                "message": f"Method not found: {method}"
            }
        }

# ============================================================================
# HEALTH & STATUS
# ============================================================================

@app.get("/")
def root():
    return {
        "status": "ok",
        "type": "mcp-server",
        "name": "Company User Management MCP Server",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "users_count": len(USERS_DB),
        "files_count": len(FILES_DB),
        "timestamp": datetime.utcnow().isoformat()
    }

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 MOCK MCP SERVER RUNNING - Company User Management")
    print("="*70)
    print("URL: http://localhost:5000")
    print("\n📋 Available Endpoints:")
    print("\n  🔍 Discovery:")
    print("     GET  /.well-known/mcp.json")
    print("     GET  /api/mcp")
    print("\n  👥 User Management:")
    print("     GET    /api/users              (READ permission)")
    print("     GET    /api/users/{id}         (READ permission)")
    print("     POST   /api/users              (CREATE permission)")
    print("     PUT    /api/users/{id}         (UPDATE permission)")
    print("     DELETE /api/users/{id}         (DELETE permission)")
    print("\n  📁 File Operations:")
    print("     GET    /api/files              (READ permission)")
    print("     POST   /api/files/read         (READ permission)")
    print("     POST   /api/files/write        (CREATE permission)")
    print("     DELETE /api/files?path=...     (DELETE permission)")
    print("\n  🛠️  MCP Tool Execution:")
    print("     POST   /mcp/execute-tool       (CREATE - allows ANY tool!)")
    print("     POST   /mcp/tools/read_file    (CREATE - specific tool)")
    print("     POST   /mcp/tools/write_file   (CREATE - specific tool)")
    print("     POST   /mcp/tools/execute_command (CREATE - DANGEROUS!)")
    print("     POST   /mcp/tools/database_query  (CREATE - DANGEROUS!)")
    print("\n  📡 JSON-RPC:")
    print("     POST   /api/mcp                (JSON-RPC 2.0)")
    print("\n💡 Test with ArmorIQ Proxy to enforce permissions!")
    print("="*70 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=5000)