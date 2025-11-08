# Travel MCP Server - Quick Reference

## 🚀 Quick Start

```bash
# Install dependencies (if needed)
pip install mcp

# Run the server
python travel_mcp_server.py

# Test the server
python test_client_example.py
```

## 🛠️ Available Tools

### 1. search_flights
Search for flights by origin and destination.

**Parameters:**
- `origin` (required): "New York", "JFK", etc.
- `destination` (required): "London", "LHR", etc.
- `date` (optional): "2025-11-15"
- `class` (optional): "Economy", "Business", "First"

**Example:**
```json
{
  "origin": "New York",
  "destination": "London",
  "class": "Economy"
}
```

---

### 2. search_hotels
Search for hotels by location.

**Parameters:**
- `location` (required): "London", "Tokyo", etc.
- `check_in` (optional): "2025-11-15"
- `check_out` (optional): "2025-11-18"
- `min_rating` (optional): 1-5
- `max_price` (optional): Maximum price in USD

**Example:**
```json
{
  "location": "London",
  "min_rating": 4,
  "max_price": 300
}
```

---

### 3. search_car_rentals
Search for car rentals by location.

**Parameters:**
- `location` (required): "London Airport", "Tokyo", etc.
- `car_type` (optional): "Sedan", "SUV", "Compact", etc.
- `max_price` (optional): Maximum price per day in USD

**Example:**
```json
{
  "location": "London Airport",
  "car_type": "SUV"
}
```

---

### 4. get_flight_details
Get detailed information about a specific flight.

**Parameters:**
- `flight_id` (required): "FL001", "FL002", etc.

**Example:**
```json
{
  "flight_id": "FL001"
}
```

---

### 5. get_hotel_details
Get detailed information about a specific hotel.

**Parameters:**
- `hotel_id` (required): "HTL001", "HTL002", etc.

**Example:**
```json
{
  "hotel_id": "HTL001"
}
```

---

### 6. book_flight
Book a flight (simulated).

**Parameters:**
- `flight_id` (required): "FL001", "FL002", etc.
- `passenger_name` (required): "John Doe"
- `num_seats` (optional): Number of seats (default: 1)

**Example:**
```json
{
  "flight_id": "FL001",
  "passenger_name": "John Doe",
  "num_seats": 2
}
```

---

## 📊 Sample Data IDs

### Flights
- `FL001` - New York → London (Economy)
- `FL002` - New York → London (Business)
- `FL003` - Los Angeles → Tokyo
- `FL004` - Paris → Dubai
- `FL005` - Miami → Barcelona
- `FL006` - Singapore → Sydney

### Hotels
- `HTL001` - Grand Plaza Hotel (London, 5⭐)
- `HTL002` - Sakura Garden Inn (Tokyo, 4⭐)
- `HTL003` - Desert Oasis Resort (Dubai, 5⭐)
- `HTL004` - Barcelona Beach Hotel (Barcelona, 4⭐)
- `HTL005` - Sydney Harbour View (Sydney, 5⭐)
- `HTL006` - Budget Stay Inn (London, 3⭐)

### Car Rentals
- `CAR001` - Toyota Camry (London)
- `CAR002` - BMW X5 (London)
- `CAR003` - Honda Civic (Tokyo)
- `CAR004` - Mercedes S-Class (Dubai)
- `CAR005` - VW Golf (Barcelona)
- `CAR006` - Ford Explorer (Sydney)

---

## 💬 Natural Language Queries (with AI Agent)

Once connected to an AI agent like Claude:

```
"Find me flights from New York to London"
"Show me 5-star hotels in Dubai under $500 per night"
"What car rentals are available at Tokyo airport?"
"Get me details on flight FL003"
"Book flight FL001 for Jane Smith, 2 seats"
"I need a hotel in Barcelona with a pool"
"Find me an SUV rental in Sydney"
```

---

## ⚙️ Configuration

### Claude Desktop

**Config Location (Windows):**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Config Content:**
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

---

## 🐛 Troubleshooting

### Server won't start
```bash
# Check Python version (need 3.10+)
python --version

# Check MCP is installed
pip show mcp

# Reinstall if needed
pip install --upgrade mcp
```

### Can't connect from Claude
1. Check the config file path
2. Verify the Python path in config
3. Restart Claude Desktop completely
4. Check logs: Help → View Logs

### Tool not found
- Verify tool name spelling
- Check server is running
- Look for error messages in logs

---

## 📁 Project Structure

```
mcp/
├── travel_mcp_server.py          # Main MCP server
├── test_client_example.py         # Test client
├── requirements.txt               # Python dependencies
├── README.md                      # Main documentation
├── setup_guide.md                 # Setup instructions
├── ARCHITECTURE.md                # Technical architecture
├── QUICK_REFERENCE.md             # This file
├── claude_desktop_config_example.json
└── .gitignore
```

---

## 🔧 Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python travel_mcp_server.py

# Run tests
python test_client_example.py

# Check for syntax errors
python -m py_compile travel_mcp_server.py
```

---

## 📚 Additional Resources

- **Full Documentation**: See `README.md`
- **Setup Instructions**: See `setup_guide.md`
- **Architecture Details**: See `ARCHITECTURE.md`
- **MCP Docs**: https://docs.anthropic.com/mcp
- **MCP GitHub**: https://github.com/anthropics/mcp

---

## 🎯 Common Use Cases

### Plan a Trip
1. Search flights to destination
2. Search hotels in destination
3. Search car rentals at airport
4. Book selected options

### Compare Options
1. Search with different criteria
2. Get details on specific options
3. Compare prices and features

### Multi-City Journey
1. Search flights for each leg
2. Search hotels in each city
3. Coordinate dates and times

---

## 💡 Tips

- Use city names or airport codes for searches
- Filter by price to find best deals
- Check availability before booking
- Use detail tools for complete information
- Try natural language with AI agents
- Dates in format: YYYY-MM-DD

---

## 🚦 Status Codes

The server uses standard JSON-RPC 2.0 responses:

- **Success**: Returns result with content
- **Error**: Returns error with message
- **Not Found**: Returns empty result or error message

---

## 📞 Support

For issues, check:
1. This quick reference
2. `setup_guide.md` for detailed setup
3. `ARCHITECTURE.md` for technical details
4. Server logs for error messages

---

**Last Updated**: November 2025
**Version**: 1.0.0
**License**: MIT

