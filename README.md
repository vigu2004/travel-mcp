# Travel Company MCP Server

A Model Context Protocol (MCP) server providing in-memory travel data for flights, hotels, and car rentals. Built using Anthropic's official MCP SDK.

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

1. **search_flights** - Search for available flights
   - Parameters: origin, destination, date (optional), class (optional)
   
2. **search_hotels** - Search for available hotels
   - Parameters: location, check_in (optional), check_out (optional), min_rating (optional), max_price (optional)
   
3. **search_car_rentals** - Search for car rentals
   - Parameters: location, car_type (optional), max_price (optional)
   
4. **get_flight_details** - Get detailed flight information
   - Parameters: flight_id
   
5. **get_hotel_details** - Get detailed hotel information
   - Parameters: hotel_id
   
6. **book_flight** - Simulate flight booking
   - Parameters: flight_id, passenger_name, num_seats (optional)

## Installation

1. Install Python 3.10 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python travel_mcp_server.py
```

## Configuration for Claude Desktop

To use this MCP server with Claude Desktop, add the following to your Claude Desktop configuration file:

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "travel-company": {
      "command": "python",
      "args": ["D:\\Vigu\\vscode\\armoriq\\mcp\\travel_mcp_server.py"]
    }
  }
}
```

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

## Development

### Adding More Data

Edit the data structures in `travel_mcp_server.py`:
- `FLIGHTS_DATA` - Add more flight entries
- `HOTELS_DATA` - Add more hotel entries
- `CAR_RENTALS_DATA` - Add more car rental entries

### Adding New Tools

1. Add tool definition in `handle_list_tools()`
2. Add handler in `handle_call_tool()`
3. Implement the tool function

## Protocol

This server implements the Model Context Protocol (MCP) specification:
- Uses JSON-RPC 2.0 for communication
- Runs over stdio transport
- Supports standard MCP tool calling interface

## License

MIT License - Feel free to use and modify for your needs.

## Next Steps

Build an AI agent that can:
1. Connect to this MCP server
2. Query travel data using natural language
3. Help users plan complete trips (flights + hotels + car rentals)
4. Make bookings and provide confirmations

The server is ready to integrate with any LLM that supports MCP!

