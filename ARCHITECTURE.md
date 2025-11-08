# Travel MCP Server - Architecture

## Overview

This MCP server provides a standardized interface for AI agents to access travel-related data using the Model Context Protocol developed by Anthropic.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         AI Agent / LLM                          │
│                    (Claude, GPT, Custom Agent)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ Natural Language Queries
                             │ ("Find flights to London")
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                      MCP Client Layer                           │
│                   (Converts to JSON-RPC)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ JSON-RPC 2.0 over stdio
                             │ (Structured Tool Calls)
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                   Travel MCP Server                             │
│                  (travel_mcp_server.py)                         │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │              Tool Handlers                              │  │
│  │  • search_flights()                                     │  │
│  │  • search_hotels()                                      │  │
│  │  • search_car_rentals()                                 │  │
│  │  • get_flight_details()                                 │  │
│  │  • get_hotel_details()                                  │  │
│  │  • book_flight()                                        │  │
│  └─────────────────────────────────────────────────────────┘  │
│                           │                                     │
│                           │                                     │
│  ┌─────────────────────────▼───────────────────────────────┐  │
│  │           In-Memory Data Storage                        │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │  │
│  │  │ FLIGHTS_DATA │  │ HOTELS_DATA  │  │CAR_RENTALS   │  │  │
│  │  │              │  │              │  │_DATA         │  │  │
│  │  │ • 6 Flights  │  │ • 6 Hotels   │  │• 6 Rentals   │  │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  │  │
│  └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. Query Flow

```
User Query → AI Agent → MCP Client → JSON-RPC Call → MCP Server → Handler Function → Data Lookup → Response
```

**Example:**
```
"Find flights from NYC to London"
    ↓
Claude processes the request
    ↓
Calls search_flights tool via MCP
    ↓
{
  "method": "tools/call",
  "params": {
    "name": "search_flights",
    "arguments": {
      "origin": "New York",
      "destination": "London"
    }
  }
}
    ↓
Server searches FLIGHTS_DATA
    ↓
Returns formatted results
    ↓
Claude presents results to user
```

### 2. Booking Flow

```
Booking Request → Validation → Data Update → Confirmation
```

**Example:**
```
"Book flight FL001 for John Doe"
    ↓
book_flight tool called
    ↓
Validate flight exists and has seats
    ↓
Update available_seats count
    ↓
Generate booking reference
    ↓
Return confirmation
```

## Components

### 1. Server Core (`travel_mcp_server.py`)

**Responsibilities:**
- Initialize MCP server
- Handle JSON-RPC communication
- Route tool calls to appropriate handlers
- Manage server lifecycle

**Key Functions:**
- `main()` - Server entry point
- `handle_list_tools()` - Returns available tools
- `handle_call_tool()` - Routes tool calls

### 2. Tool Handlers

**Search Tools:**
- `search_flights()` - Query flights with filtering
- `search_hotels()` - Query hotels with filtering
- `search_car_rentals()` - Query car rentals with filtering

**Detail Tools:**
- `get_flight_details()` - Get specific flight info
- `get_hotel_details()` - Get specific hotel info

**Action Tools:**
- `book_flight()` - Simulate booking (modifies data)

### 3. Data Storage

**In-Memory Lists:**
- `FLIGHTS_DATA` - List of flight dictionaries
- `HOTELS_DATA` - List of hotel dictionaries
- `CAR_RENTALS_DATA` - List of car rental dictionaries

**Data Structure Example (Flight):**
```python
{
    "id": "FL001",                    # Unique identifier
    "airline": "SkyWings Airlines",   # Airline name
    "flight_number": "SW123",         # Flight number
    "origin": "New York (JFK)",       # Departure airport
    "destination": "London (LHR)",    # Arrival airport
    "departure_time": "2025-11-15T08:00:00",
    "arrival_time": "2025-11-15T20:30:00",
    "duration": "7h 30m",
    "price": 850.00,
    "currency": "USD",
    "available_seats": 45,
    "class": "Economy"
}
```

## Protocol Details

### MCP Standard Protocol

**Transport:** stdio (stdin/stdout)
**Format:** JSON-RPC 2.0
**Encoding:** UTF-8

### Tool Call Structure

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_flights",
    "arguments": {
      "origin": "New York",
      "destination": "London",
      "class": "Economy"
    }
  }
}
```

### Tool Response Structure

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found 2 flight(s):\n\n🛫 Flight SW123..."
      }
    ]
  }
}
```

## Security Considerations

### Current Implementation (Development)

- No authentication (local use only)
- No rate limiting
- No data persistence
- No input sanitization beyond type checking

### Production Recommendations

1. **Authentication:** Add API keys or OAuth
2. **Rate Limiting:** Prevent abuse
3. **Input Validation:** Sanitize all inputs
4. **Data Persistence:** Use a database instead of in-memory storage
5. **Logging:** Add comprehensive logging
6. **Error Handling:** More robust error handling
7. **Transport Security:** Use HTTPS for remote connections

## Extending the Server

### Adding a New Data Type

1. **Create data structure:**
```python
CRUISES_DATA = [
    {
        "id": "CR001",
        "name": "Caribbean Paradise",
        "departure_port": "Miami",
        "duration_days": 7,
        "price": 1500.00
    }
]
```

2. **Add search tool:**
```python
types.Tool(
    name="search_cruises",
    description="Search for available cruises",
    inputSchema={...}
)
```

3. **Implement handler:**
```python
async def search_cruises(args: dict) -> list[types.TextContent]:
    # Implementation
    pass
```

4. **Register in router:**
```python
elif name == "search_cruises":
    return await search_cruises(arguments)
```

### Adding Advanced Features

**Examples:**
- Multi-city flight searches
- Hotel room type preferences
- Car rental insurance options
- Package deals (flight + hotel)
- Price history and predictions
- User reviews and ratings
- Real-time availability updates

## Performance Considerations

### Current Performance

- **Latency:** ~10-50ms per query (in-memory)
- **Throughput:** Limited by stdio (single connection)
- **Scalability:** Single process, not horizontally scalable

### Optimization Strategies

1. **Caching:** Add response caching for common queries
2. **Indexing:** Use hash maps for faster lookups
3. **Async Operations:** All handlers are async-ready
4. **Batch Requests:** Support multiple tool calls in one request
5. **Database:** Move to database for better query performance

## Testing

### Unit Tests

Test individual tool handlers:
```python
async def test_search_flights():
    result = await search_flights({
        "origin": "New York",
        "destination": "London"
    })
    assert len(result) > 0
```

### Integration Tests

Test full MCP flow with test client:
```bash
python test_client_example.py
```

### Manual Tests

Test with Claude Desktop or custom AI agent.

## Monitoring

### Logs

The server logs to stdout:
```
INFO:travel-mcp-server:Travel MCP Server starting...
```

### Metrics to Monitor

- Tool call frequency
- Response times
- Error rates
- Data modification events (bookings)
- Connection status

## Future Enhancements

1. **Persistent Storage:** SQLite or PostgreSQL
2. **Real API Integration:** Connect to actual travel APIs
3. **User Sessions:** Track user preferences
4. **Advanced Search:** Fuzzy matching, synonyms
5. **Multi-language Support:** Internationalization
6. **Price Comparison:** Compare across providers
7. **Recommendations:** ML-based suggestions
8. **Notifications:** Price alerts, booking reminders
9. **Payment Processing:** Integration with payment gateways
10. **Admin Dashboard:** Manage data via web interface

## Comparison with REST API

| Feature | MCP Server | REST API |
|---------|-----------|----------|
| Protocol | JSON-RPC 2.0 | HTTP/REST |
| Transport | stdio/SSE | HTTP |
| Discovery | Dynamic tool listing | Static endpoints |
| AI Integration | Native | Requires wrapper |
| Streaming | Yes | Limited |
| Type Safety | JSON Schema | OpenAPI |
| Use Case | AI-to-Service | General purpose |

## Resources

- [Anthropic MCP Documentation](https://docs.anthropic.com/mcp)
- [MCP GitHub Repository](https://github.com/anthropics/mcp)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)
- [MCP Python SDK](https://github.com/anthropics/mcp-python-sdk)

## License

MIT License - See LICENSE file for details.

