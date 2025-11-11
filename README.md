# Travel Company MCP Server

A secure Model Context Protocol (MCP) server providing in-memory travel data for flights, hotels, and car rentals. This server offers clean, production-ready tools for AI agents to access travel information.

## Features

### 🛫 Flight Search
- Search flights by origin, destination, date, and class
- 6 sample flights across major international routes
- Detailed information including prices, schedules, and availability

### 🏨 Hotel Search
- Search hotels by location, rating, and price range
- 6 hotels across different cities with various price points
- Amenities, room types, and availability information

### 🚗 Car Rental Search
- Search car rentals by location, type, and price
- 6 rental options from economy to luxury vehicles
- Features include transmission type, seating capacity, and extras

## Available Tools

All tools are secure and production-ready:

1. **search_flights** - Search for available flights
   - Parameters: origin, destination, date (optional), cabin_class (optional)
   - Returns: List of matching flights with details
   
2. **search_hotels** - Search for available hotels
   - Parameters: location, check_in (optional), check_out (optional), min_rating (optional), max_price (optional)
   - Returns: List of matching hotels with details
   
3. **search_car_rentals** - Search for car rentals
   - Parameters: location, car_type (optional), max_price (optional)
   - Returns: List of available car rentals
   
4. **get_flight_details** - Get detailed flight information
   - Parameters: flight_id
   - Returns: Complete flight information
   
5. **get_hotel_details** - Get detailed hotel information
   - Parameters: hotel_id
   - Returns: Complete hotel information
   
6. **book_flight** - Simulate flight booking
   - Parameters: flight_id, passenger_name, num_seats (optional)
   - Returns: Booking confirmation with reference number

## Installation

1. Install Python 3.10 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the server with:

```bash
python travel_mcp_server.py
```

The server will start on `http://localhost:8000` by default. You can change the port by setting the `PORT` environment variable:

```bash
PORT=3000 python travel_mcp_server.py
```

## Configuration for Claude Desktop

To use this MCP server with Claude Desktop, add the following to your Claude Desktop configuration file:

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "travel-company": {
      "command": "python",
      "args": ["/path/to/travel_mcp/travel_mcp_server.py"]
    }
  }
}
```

Replace `/path/to/travel_mcp/` with the actual path to your travel_mcp directory.

After adding the configuration, restart Claude Desktop.

## Sample Data

### Flights
- New York → London (Economy & Business)
- Los Angeles → Tokyo
- Paris → Dubai
- Miami → Barcelona
- Singapore → Sydney

### Hotels
- London: Grand Plaza Hotel (5-star), Budget Stay Inn (3-star)
- Tokyo: Sakura Garden Inn (4-star)
- Dubai: Desert Oasis Resort (5-star)
- Barcelona: Barcelona Beach Hotel (4-star)
- Sydney: Sydney Harbour View (5-star)

### Car Rentals
Available at major airports in London, Tokyo, Dubai, Barcelona, and Sydney with options ranging from compact cars to luxury sedans.

## Usage Example with AI Agent

Once the server is running, an AI agent (like Claude) can query it:

```
User: "I need a flight from New York to London next week"
AI Agent: [Calls search_flights tool]
Server: [Returns available flights with details]

User: "Book the economy flight and find me a 4-star hotel in London"
AI Agent: [Calls book_flight and search_hotels tools]
Server: [Returns booking confirmation and hotel options]
```

## API Access

The server exposes an HTTP API at `http://localhost:8000/mcp/v1` using JSON-RPC 2.0.

### Testing with a Simple Client

You can use the provided test client to interact with the server:

```bash
python test_client_example.py
```

## Development

### Adding More Data

Edit the data structures in `travel_tools.py`:
- `FLIGHTS_DATA` - Add more flight entries
- `HOTELS_DATA` - Add more hotel entries
- `CAR_RENTALS_DATA` - Add more car rental entries

### Architecture

The server is built with:
- **FastMCP**: Modern MCP framework for Python
- **Uvicorn**: ASGI server for HTTP transport
- **In-memory data**: No database required, perfect for development and demos

See `ARCHITECTURE.md` for detailed architecture documentation.

## Protocol

This server implements the Model Context Protocol (MCP) specification:
- Uses JSON-RPC 2.0 for communication
- Supports HTTP transport with CORS enabled
- Implements standard MCP tool calling interface

## Testing

Run the test suite:

```bash
python test_travel_server.py
```

This will test all available tools with various inputs.

## Security

✅ This server uses secure coding practices:
- No eval() or exec() calls
- Input validation on all user inputs
- No arbitrary file system access
- No command execution capabilities
- Parameterized queries for any database operations

## License

MIT License - Feel free to use and modify for your needs.

## Next Steps

Build an AI agent that can:
1. Connect to this MCP server
2. Query travel data using natural language
3. Help users plan complete trips (flights + hotels + car rentals)
4. Make bookings and provide confirmations

The server is ready to integrate with any LLM that supports MCP!

## Contributing

Contributions are welcome! Please ensure:
- All code follows secure coding practices
- New tools include comprehensive documentation
- Tests are included for new functionality

