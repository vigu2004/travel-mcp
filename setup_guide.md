# Travel MCP Server - Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
# Navigate to the project directory
cd D:\Vigu\vscode\armoriq\mcp

# Install the required package
pip install mcp
```

### 2. Test the Server

Run the server directly to test:

```bash
python travel_mcp_server.py
```

The server will start and wait for JSON-RPC messages via stdin/stdout.

### 3. Test with Client Example (Optional)

```bash
python test_client_example.py
```

This will run automated tests showing all the server capabilities.

## Integrating with Claude Desktop

### Step 1: Locate Claude Desktop Config

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### Step 2: Edit Configuration

Open the config file and add:

```json
{
  "mcpServers": {
    "travel-company": {
      "command": "python",
      "args": [
        "D:\\Vigu\\vscode\\armoriq\\mcp\\travel_mcp_server.py"
      ]
    }
  }
}
```

**Important**: 
- Use the full absolute path to the Python script
- On Windows, escape backslashes (`\\`) or use forward slashes (`/`)
- Make sure Python is in your PATH

### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop completely.

### Step 4: Verify Connection

In Claude Desktop, you should see an icon or indication that the MCP server is connected. Try asking:

```
"Can you search for flights from New York to London?"
```

Claude should automatically use the `search_flights` tool from your MCP server!

## Using the Server with Custom AI Agents

### Python Example

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def query_travel_server():
    server_params = StdioServerParameters(
        command="python",
        args=["D:\\Vigu\\vscode\\armoriq\\mcp\\travel_mcp_server.py"],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Search for flights
            result = await session.call_tool(
                "search_flights",
                arguments={
                    "origin": "New York",
                    "destination": "London",
                    "class": "Economy"
                }
            )
            print(result.content[0].text)

asyncio.run(query_travel_server())
```

### Integration with LangChain or Other Frameworks

The MCP server can be integrated with any framework that supports:
- Subprocess communication via stdin/stdout
- JSON-RPC 2.0 protocol
- Tool/function calling

## Available Queries

### Flight Searches

```
"Find flights from New York to London"
"Show me business class flights to Tokyo"
"What flights are available from Paris to Dubai on November 18?"
```

### Hotel Searches

```
"Find 5-star hotels in London"
"Show me hotels in Tokyo under $200 per night"
"What's available in Barcelona with a minimum 4-star rating?"
```

### Car Rental Searches

```
"Find car rentals at London Heathrow Airport"
"Show me SUVs available in Dubai"
"What compact cars are available in Barcelona?"
```

### Booking

```
"Book flight FL001 for Jane Smith"
"Reserve 2 seats on flight FL003 for John Doe"
```

## Troubleshooting

### Server Won't Start

1. Verify Python version (3.10+):
   ```bash
   python --version
   ```

2. Verify MCP is installed:
   ```bash
   pip show mcp
   ```

3. Check for syntax errors:
   ```bash
   python -m py_compile travel_mcp_server.py
   ```

### Claude Desktop Can't Connect

1. Check the config file path is correct
2. Verify the Python path in the config
3. Look at Claude Desktop logs (Help → View Logs)
4. Try using the full path to python.exe:
   ```json
   "command": "C:\\Python311\\python.exe"
   ```

### Tool Calls Not Working

1. Verify the server is running (check logs)
2. Ensure the tool names match exactly
3. Check that required parameters are provided
4. Look for error messages in the server output

## Data Customization

### Adding More Flights

Edit `FLIGHTS_DATA` in `travel_mcp_server.py`:

```python
FLIGHTS_DATA.append({
    "id": "FL007",
    "airline": "Your Airline",
    "flight_number": "YA100",
    "origin": "City A (AAA)",
    "destination": "City B (BBB)",
    "departure_time": "2025-12-01T10:00:00",
    "arrival_time": "2025-12-01T14:00:00",
    "duration": "4h 00m",
    "price": 500.00,
    "currency": "USD",
    "available_seats": 50,
    "class": "Economy"
})
```

### Adding More Hotels

Edit `HOTELS_DATA` similarly with your hotel information.

### Adding More Car Rentals

Edit `CAR_RENTALS_DATA` with additional rental options.

## Advanced: Adding New Tools

To add a new tool (e.g., "search_vacation_packages"):

1. Add tool definition in `handle_list_tools()`:
```python
types.Tool(
    name="search_vacation_packages",
    description="Search for vacation packages",
    inputSchema={
        "type": "object",
        "properties": {
            "destination": {"type": "string"}
        },
        "required": ["destination"]
    }
)
```

2. Add handler in `handle_call_tool()`:
```python
elif name == "search_vacation_packages":
    return await search_vacation_packages(arguments)
```

3. Implement the function:
```python
async def search_vacation_packages(args: dict) -> list[types.TextContent]:
    # Your implementation
    pass
```

## Next Steps

1. **Test the server** with the test client
2. **Configure Claude Desktop** to use your server
3. **Try natural language queries** with Claude
4. **Customize the data** to match your needs
5. **Add new tools** as needed
6. **Build your AI agent** to interact with the server

Happy travels! ✈️🏨🚗

