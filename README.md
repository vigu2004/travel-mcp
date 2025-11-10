# Travel Company MCP Server (With Intentional Vulnerabilities)

A Model Context Protocol (MCP) server providing in-memory travel data for flights, hotels, and car rentals. This server contains **intentional security vulnerabilities** for testing MCP security scanners and demonstrating common web application vulnerabilities.

⚠️ **WARNING:** This server is intentionally vulnerable and should NEVER be used in production!

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

### Safe Travel Tools ✅

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

### Vulnerable Travel Tools ⚠️

7. **calculate_trip_cost** - Calculate trip costs using formulas (CWE-94: eval injection)
   - Parameters: base_price, calculation_formula
   - Vulnerability: Uses `eval()` on user input

8. **apply_discount_code** - Apply discount codes (CWE-94: eval injection)
   - Parameters: price, discount_code
   - Vulnerability: Evaluates discount codes as Python expressions

9. **generate_booking_confirmation** - Generate confirmation messages (CWE-134: format string)
   - Parameters: passenger_name, flight_id, template (optional)
   - Vulnerability: Unsafe string formatting

10. **search_booking_by_name** - Search bookings (CWE-89: SQL injection)
    - Parameters: passenger_name
    - Vulnerability: String concatenation in SQL queries

11. **download_travel_document** - Download travel documents (CWE-22: path traversal)
    - Parameters: document_path
    - Vulnerability: No path validation

12. **fetch_destination_info** - Fetch destination data from APIs (CWE-918: SSRF)
    - Parameters: api_url
    - Vulnerability: Unvalidated HTTP requests

### Critical Dangerous Tools 🚨

13. **read_file** - Read arbitrary files (CWE-22: path traversal)
14. **write_file** - Write arbitrary files (CWE-73: arbitrary file write)
15. **execute_command** - Execute system commands (CWE-78: command injection)
16. **database_query** - Execute raw SQL queries (CWE-89: SQL injection)

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

The server will start on `http://localhost:8000` by default.

## Testing Vulnerabilities

### Run Vulnerability Tests

Test all vulnerable tools to ensure they work:

```bash
python test_vulnerabilities.py
```

This will test each vulnerable tool with sample inputs.

### Security Scanner Testing

This server is designed to test MCP security scanners. Your scanner should detect:

- **CWE-22**: Path Traversal in `read_file`, `write_file`, `download_travel_document`
- **CWE-73**: Arbitrary File Write in `write_file`
- **CWE-78**: Command Injection in `execute_command`
- **CWE-89**: SQL Injection in `database_query`, `search_booking_by_name`
- **CWE-94**: Code Injection (eval) in `calculate_trip_cost`, `apply_discount_code`
- **CWE-134**: Format String vulnerability in `generate_booking_confirmation`
- **CWE-918**: SSRF in `fetch_destination_info`

See `VULNERABILITIES.md` for detailed documentation of each vulnerability.

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

