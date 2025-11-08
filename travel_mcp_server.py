#!/usr/bin/env python3
"""
Travel Company MCP Server (FastAPI Version)
Provides in-memory travel data including flights, hotels, and car rentals.
Deployable as a web service on Render or similar platforms.
"""

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import uvicorn
from datetime import datetime, timedelta
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("travel-mcp-server")

# Create FastAPI app
app = FastAPI(title="Travel Company MCP Server")

# In-memory data storage
FLIGHTS_DATA = [
    {
        "id": "FL001",
        "airline": "SkyWings Airlines",
        "flight_number": "SW123",
        "origin": "New York (JFK)",
        "destination": "London (LHR)",
        "departure_time": "2025-11-15T08:00:00",
        "arrival_time": "2025-11-15T20:30:00",
        "duration": "7h 30m",
        "price": 850.00,
        "currency": "USD",
        "available_seats": 45,
        "class": "Economy"
    },
    {
        "id": "FL002",
        "airline": "SkyWings Airlines",
        "flight_number": "SW124",
        "origin": "New York (JFK)",
        "destination": "London (LHR)",
        "departure_time": "2025-11-15T14:00:00",
        "arrival_time": "2025-11-16T02:30:00",
        "duration": "7h 30m",
        "price": 1250.00,
        "currency": "USD",
        "available_seats": 12,
        "class": "Business"
    },
    {
        "id": "FL003",
        "airline": "Pacific Air",
        "flight_number": "PA456",
        "origin": "Los Angeles (LAX)",
        "destination": "Tokyo (NRT)",
        "departure_time": "2025-11-20T11:00:00",
        "arrival_time": "2025-11-21T15:30:00",
        "duration": "11h 30m",
        "price": 1100.00,
        "currency": "USD",
        "available_seats": 89,
        "class": "Economy"
    },
    {
        "id": "FL004",
        "airline": "Euro Connect",
        "flight_number": "EC789",
        "origin": "Paris (CDG)",
        "destination": "Dubai (DXB)",
        "departure_time": "2025-11-18T09:30:00",
        "arrival_time": "2025-11-18T18:45:00",
        "duration": "6h 15m",
        "price": 720.00,
        "currency": "USD",
        "available_seats": 67,
        "class": "Economy"
    },
    {
        "id": "FL005",
        "airline": "TransAtlantic Airways",
        "flight_number": "TA321",
        "origin": "Miami (MIA)",
        "destination": "Barcelona (BCN)",
        "departure_time": "2025-11-22T17:00:00",
        "arrival_time": "2025-11-23T07:00:00",
        "duration": "9h 00m",
        "price": 950.00,
        "currency": "USD",
        "available_seats": 34,
        "class": "Economy"
    },
    {
        "id": "FL006",
        "airline": "Asia Express",
        "flight_number": "AE567",
        "origin": "Singapore (SIN)",
        "destination": "Sydney (SYD)",
        "departure_time": "2025-11-25T22:00:00",
        "arrival_time": "2025-11-26T08:30:00",
        "duration": "8h 30m",
        "price": 680.00,
        "currency": "USD",
        "available_seats": 102,
        "class": "Economy"
    }
]

HOTELS_DATA = [
    {
        "id": "HTL001",
        "name": "Grand Plaza Hotel",
        "location": "London, UK",
        "address": "123 Westminster Avenue, London, SW1A 1AA",
        "star_rating": 5,
        "price_per_night": 320.00,
        "currency": "USD",
        "available_rooms": 15,
        "amenities": ["WiFi", "Pool", "Spa", "Restaurant", "Gym", "Room Service"],
        "room_type": "Deluxe Suite",
        "check_in": "2025-11-15",
        "check_out": "2025-11-18"
    },
    {
        "id": "HTL002",
        "name": "Sakura Garden Inn",
        "location": "Tokyo, Japan",
        "address": "456 Shibuya Street, Tokyo, 150-0002",
        "star_rating": 4,
        "price_per_night": 180.00,
        "currency": "USD",
        "available_rooms": 28,
        "amenities": ["WiFi", "Restaurant", "Bar", "Concierge"],
        "room_type": "Standard Room",
        "check_in": "2025-11-21",
        "check_out": "2025-11-24"
    },
    {
        "id": "HTL003",
        "name": "Desert Oasis Resort",
        "location": "Dubai, UAE",
        "address": "789 Sheikh Zayed Road, Dubai, 00000",
        "star_rating": 5,
        "price_per_night": 450.00,
        "currency": "USD",
        "available_rooms": 8,
        "amenities": ["WiFi", "Pool", "Spa", "Restaurant", "Gym", "Beach Access", "Butler Service"],
        "room_type": "Luxury Villa",
        "check_in": "2025-11-18",
        "check_out": "2025-11-22"
    },
    {
        "id": "HTL004",
        "name": "Barcelona Beach Hotel",
        "location": "Barcelona, Spain",
        "address": "321 La Rambla, Barcelona, 08002",
        "star_rating": 4,
        "price_per_night": 210.00,
        "currency": "USD",
        "available_rooms": 22,
        "amenities": ["WiFi", "Pool", "Restaurant", "Beach Access"],
        "room_type": "Sea View Room",
        "check_in": "2025-11-23",
        "check_out": "2025-11-26"
    },
    {
        "id": "HTL005",
        "name": "Sydney Harbour View",
        "location": "Sydney, Australia",
        "address": "567 Circular Quay, Sydney, NSW 2000",
        "star_rating": 5,
        "price_per_night": 380.00,
        "currency": "USD",
        "available_rooms": 11,
        "amenities": ["WiFi", "Restaurant", "Bar", "Gym", "Harbour View"],
        "room_type": "Premium Harbour Suite",
        "check_in": "2025-11-26",
        "check_out": "2025-11-29"
    },
    {
        "id": "HTL006",
        "name": "Budget Stay Inn",
        "location": "London, UK",
        "address": "88 Camden Road, London, NW1 9EA",
        "star_rating": 3,
        "price_per_night": 95.00,
        "currency": "USD",
        "available_rooms": 42,
        "amenities": ["WiFi", "Breakfast"],
        "room_type": "Standard Room",
        "check_in": "2025-11-15",
        "check_out": "2025-11-18"
    }
]

CAR_RENTALS_DATA = [
    {
        "id": "CAR001",
        "company": "QuickRent Cars",
        "location": "London Heathrow Airport",
        "car_model": "Toyota Camry",
        "car_type": "Sedan",
        "transmission": "Automatic",
        "seats": 5,
        "price_per_day": 45.00,
        "currency": "USD",
        "available_units": 8,
        "features": ["GPS", "Bluetooth", "Cruise Control"]
    },
    {
        "id": "CAR002",
        "company": "QuickRent Cars",
        "location": "London Heathrow Airport",
        "car_model": "BMW X5",
        "car_type": "SUV",
        "transmission": "Automatic",
        "seats": 7,
        "price_per_day": 95.00,
        "currency": "USD",
        "available_units": 3,
        "features": ["GPS", "Bluetooth", "Leather Seats", "Panoramic Roof"]
    },
    {
        "id": "CAR003",
        "company": "Tokyo Auto Rent",
        "location": "Tokyo Narita Airport",
        "car_model": "Honda Civic",
        "car_type": "Compact",
        "transmission": "Automatic",
        "seats": 5,
        "price_per_day": 38.00,
        "currency": "USD",
        "available_units": 12,
        "features": ["GPS", "Bluetooth"]
    },
    {
        "id": "CAR004",
        "company": "Dubai Luxury Rentals",
        "location": "Dubai International Airport",
        "car_model": "Mercedes-Benz S-Class",
        "car_type": "Luxury Sedan",
        "transmission": "Automatic",
        "seats": 5,
        "price_per_day": 180.00,
        "currency": "USD",
        "available_units": 2,
        "features": ["GPS", "Bluetooth", "Leather Seats", "Massage Seats", "Chauffeur Available"]
    },
    {
        "id": "CAR005",
        "company": "Barcelona Drive",
        "location": "Barcelona El Prat Airport",
        "car_model": "Volkswagen Golf",
        "car_type": "Hatchback",
        "transmission": "Manual",
        "seats": 5,
        "price_per_day": 32.00,
        "currency": "USD",
        "available_units": 15,
        "features": ["GPS", "Bluetooth"]
    },
    {
        "id": "CAR006",
        "company": "Sydney Wheels",
        "location": "Sydney Kingsford Smith Airport",
        "car_model": "Ford Explorer",
        "car_type": "SUV",
        "transmission": "Automatic",
        "seats": 7,
        "price_per_day": 85.00,
        "currency": "USD",
        "available_units": 6,
        "features": ["GPS", "Bluetooth", "4WD", "Roof Rack"]
    }
]

# In-memory files database (for simulated file operations)
FILES_DB = {
    "/home/travel/bookings.txt": {"content": "Flight bookings data", "owner": "travel"},
    "/home/travel/hotels.txt": {"content": "Hotel bookings data", "owner": "travel"},
    "/etc/config": {"content": "System configuration", "owner": "root"},
}

# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class SearchFlightsRequest(BaseModel):
    origin: str
    destination: str
    date: Optional[str] = None
    cabin_class: Optional[str] = None

class SearchHotelsRequest(BaseModel):
    location: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    min_rating: Optional[int] = None
    max_price: Optional[float] = None

class SearchCarRentalsRequest(BaseModel):
    location: str
    car_type: Optional[str] = None
    max_price: Optional[float] = None

class GetFlightDetailsRequest(BaseModel):
    flight_id: str

class GetHotelDetailsRequest(BaseModel):
    hotel_id: str

class BookFlightRequest(BaseModel):
    flight_id: str
    passenger_name: str
    num_seats: Optional[int] = 1

class MCPToolRequest(BaseModel):
    tool: str
    arguments: Dict[str, Any]

class ReadFileRequest(BaseModel):
    path: str

class WriteFileRequest(BaseModel):
    path: str
    content: str

class ExecuteCommandRequest(BaseModel):
    command: str

class DatabaseQueryRequest(BaseModel):
    query: str

# ============================================================================
# MCP DISCOVERY ENDPOINTS
# ============================================================================

@app.get("/.well-known/mcp.json")
def mcp_wellknown():
    """MCP discovery endpoint"""
    return {
        "protocol": "mcp",
        "version": "1.0.0",
        "name": "Travel Company MCP Server",
        "description": "MCP server for travel bookings - flights, hotels, and car rentals",
        "capabilities": {
            "tools": ["search_flights", "search_hotels", "search_car_rentals", 
                     "get_flight_details", "get_hotel_details", "book_flight",
                     "read_file", "write_file", "execute_command", "database_query"],
            "resources": ["flights", "hotels", "car_rentals"]
        },
        "endpoints": {
            "flights": "/api/flights",
            "hotels": "/api/hotels",
            "car_rentals": "/api/car-rentals",
            "mcp_tools": "/mcp/execute-tool",
            "jsonrpc": "/api/mcp"
        }
    }

@app.get("/api/mcp")
def mcp_api_get():
    """Get MCP server information (GET method)"""
    return {
        "serverInfo": {
            "name": "travel-company-mcp",
            "version": "1.0.0",
            "description": "Travel booking server with flights, hotels, and car rentals"
        },
        "tools": [
            {
                "name": "search_flights",
                "description": "Search for available flights based on origin, destination, and optional date range",
                "inputSchema": {
                "type": "object",
                "properties": {
                        "origin": {"type": "string", "description": "Origin city or airport code"},
                        "destination": {"type": "string", "description": "Destination city or airport code"},
                        "date": {"type": "string", "description": "Optional: Departure date in YYYY-MM-DD format"},
                        "cabin_class": {"type": "string", "description": "Optional: Cabin class (Economy, Business, First)"}
                    },
                    "required": ["origin", "destination"]
                }
            },
            {
                "name": "search_hotels",
                "description": "Search for available hotels in a specific location",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City or location name"},
                        "check_in": {"type": "string", "description": "Optional: Check-in date"},
                        "check_out": {"type": "string", "description": "Optional: Check-out date"},
                        "min_rating": {"type": "number", "description": "Optional: Minimum star rating"},
                        "max_price": {"type": "number", "description": "Optional: Maximum price per night"}
                    },
                    "required": ["location"]
                }
            },
            {
                "name": "search_car_rentals",
                "description": "Search for available car rentals at a specific location",
                "inputSchema": {
                "type": "object",
                "properties": {
                        "location": {"type": "string", "description": "Pickup location"},
                        "car_type": {"type": "string", "description": "Optional: Type of car"},
                        "max_price": {"type": "number", "description": "Optional: Maximum price per day"}
                    },
                    "required": ["location"]
                }
            },
            {
                "name": "get_flight_details",
                "description": "Get detailed information about a specific flight by ID",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "flight_id": {"type": "string", "description": "The unique flight ID"}
                    },
                    "required": ["flight_id"]
                }
            },
            {
                "name": "get_hotel_details",
                "description": "Get detailed information about a specific hotel by ID",
                "inputSchema": {
                "type": "object",
                "properties": {
                        "hotel_id": {"type": "string", "description": "The unique hotel ID"}
                    },
                    "required": ["hotel_id"]
                }
            },
            {
                "name": "book_flight",
                "description": "Book a flight (simulated). Returns booking confirmation",
                "inputSchema": {
                "type": "object",
                "properties": {
                        "flight_id": {"type": "string", "description": "The unique flight ID to book"},
                        "passenger_name": {"type": "string", "description": "Passenger full name"},
                        "num_seats": {"type": "number", "description": "Number of seats to book"}
                    },
                    "required": ["flight_id", "passenger_name"]
                }
            },
            {
                "name": "read_file",
                "description": "Read files from the filesystem (DANGEROUS!)",
                "inputSchema": {
                "type": "object",
                "properties": {
                        "path": {"type": "string", "description": "Absolute file path"}
                    },
                    "required": ["path"]
                }
            },
            {
                "name": "write_file",
                "description": "Write content to files (DANGEROUS!)",
                "inputSchema": {
                "type": "object",
                "properties": {
                        "path": {"type": "string", "description": "File path"},
                        "content": {"type": "string", "description": "File content"}
                    },
                    "required": ["path", "content"]
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
                "name": "database_query",
                "description": "Execute SQL queries (DANGEROUS!)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "SQL query"}
                    },
                    "required": ["query"]
                }
            }
        ]
    }

# ============================================================================
# BUSINESS LOGIC FUNCTIONS
# ============================================================================

def search_flights_logic(args: dict) -> dict:
    """Search for flights based on criteria."""
    origin = args.get("origin", "").lower()
    destination = args.get("destination", "").lower()
    date = args.get("date")
    cabin_class = args.get("cabin_class") or args.get("class")
    
    results = []
    for flight in FLIGHTS_DATA:
        # Check origin and destination
        if origin in flight["origin"].lower() and destination in flight["destination"].lower():
            # Filter by class if specified
            if cabin_class and flight["class"] != cabin_class:
                continue
            # Filter by date if specified
            if date:
                flight_date = flight["departure_time"].split("T")[0]
                if flight_date != date:
                    continue
            results.append(flight)
    
    if results:
        response = f"Found {len(results)} flight(s):\n\n"
        for flight in results:
            response += f"🛫 Flight {flight['flight_number']} ({flight['id']})\n"
            response += f"   Airline: {flight['airline']}\n"
            response += f"   Route: {flight['origin']} → {flight['destination']}\n"
            response += f"   Departure: {flight['departure_time']}\n"
            response += f"   Arrival: {flight['arrival_time']}\n"
            response += f"   Duration: {flight['duration']}\n"
            response += f"   Class: {flight['class']}\n"
            response += f"   Price: ${flight['price']:.2f} {flight['currency']}\n"
            response += f"   Available Seats: {flight['available_seats']}\n\n"
    else:
        response = f"No flights found from {origin} to {destination} matching your criteria."
    
    return {"success": True, "count": len(results), "message": response, "flights": results}

def search_hotels_logic(args: dict) -> dict:
    """Search for hotels based on criteria."""
    location = args.get("location", "").lower()
    min_rating = args.get("min_rating")
    max_price = args.get("max_price")
    
    results = []
    for hotel in HOTELS_DATA:
        if location in hotel["location"].lower():
            if min_rating and hotel["star_rating"] < min_rating:
                continue
            if max_price and hotel["price_per_night"] > max_price:
                continue
            results.append(hotel)
    
    if results:
        response = f"Found {len(results)} hotel(s) in {location}:\n\n"
        for hotel in results:
            response += f"🏨 {hotel['name']} ({hotel['id']})\n"
            response += f"   Location: {hotel['location']}\n"
            response += f"   Address: {hotel['address']}\n"
            response += f"   Rating: {'⭐' * hotel['star_rating']} ({hotel['star_rating']} stars)\n"
            response += f"   Room Type: {hotel['room_type']}\n"
            response += f"   Price: ${hotel['price_per_night']:.2f} per night\n"
            response += f"   Available Rooms: {hotel['available_rooms']}\n"
            response += f"   Amenities: {', '.join(hotel['amenities'])}\n"
            response += f"   Check-in: {hotel['check_in']} | Check-out: {hotel['check_out']}\n\n"
    else:
        response = f"No hotels found in {location} matching your criteria."
    
    return {"success": True, "count": len(results), "message": response, "hotels": results}

def search_car_rentals_logic(args: dict) -> dict:
    """Search for car rentals based on criteria."""
    location = args.get("location", "").lower()
    car_type = args.get("car_type")
    max_price = args.get("max_price")
    
    results = []
    for car in CAR_RENTALS_DATA:
        if location in car["location"].lower():
            if car_type and car["car_type"] != car_type:
                continue
            if max_price and car["price_per_day"] > max_price:
                continue
            results.append(car)
    
    if results:
        response = f"Found {len(results)} car rental(s) in {location}:\n\n"
        for car in results:
            response += f"🚗 {car['car_model']} ({car['id']})\n"
            response += f"   Company: {car['company']}\n"
            response += f"   Location: {car['location']}\n"
            response += f"   Type: {car['car_type']}\n"
            response += f"   Transmission: {car['transmission']}\n"
            response += f"   Seats: {car['seats']}\n"
            response += f"   Price: ${car['price_per_day']:.2f} per day\n"
            response += f"   Available Units: {car['available_units']}\n"
            response += f"   Features: {', '.join(car['features'])}\n\n"
    else:
        response = f"No car rentals found in {location} matching your criteria."
    
    return {"success": True, "count": len(results), "message": response, "car_rentals": results}

def get_flight_details_logic(args: dict) -> dict:
    """Get detailed information about a specific flight."""
    flight_id = args.get("flight_id")
    
    for flight in FLIGHTS_DATA:
        if flight["id"] == flight_id:
            response = f"✈️ Flight Details for {flight_id}\n\n"
            response += f"Flight Number: {flight['flight_number']}\n"
            response += f"Airline: {flight['airline']}\n"
            response += f"Route: {flight['origin']} → {flight['destination']}\n"
            response += f"Departure: {flight['departure_time']}\n"
            response += f"Arrival: {flight['arrival_time']}\n"
            response += f"Duration: {flight['duration']}\n"
            response += f"Class: {flight['class']}\n"
            response += f"Price: ${flight['price']:.2f} {flight['currency']}\n"
            response += f"Available Seats: {flight['available_seats']}\n"
            return {"success": True, "message": response, "flight": flight}
    
    return {"success": False, "message": f"Flight {flight_id} not found."}

def get_hotel_details_logic(args: dict) -> dict:
    """Get detailed information about a specific hotel."""
    hotel_id = args.get("hotel_id")
    
    for hotel in HOTELS_DATA:
        if hotel["id"] == hotel_id:
            response = f"🏨 Hotel Details for {hotel_id}\n\n"
            response += f"Name: {hotel['name']}\n"
            response += f"Location: {hotel['location']}\n"
            response += f"Address: {hotel['address']}\n"
            response += f"Rating: {'⭐' * hotel['star_rating']} ({hotel['star_rating']} stars)\n"
            response += f"Room Type: {hotel['room_type']}\n"
            response += f"Price: ${hotel['price_per_night']:.2f} per night\n"
            response += f"Available Rooms: {hotel['available_rooms']}\n"
            response += f"Amenities: {', '.join(hotel['amenities'])}\n"
            response += f"Check-in: {hotel['check_in']}\n"
            response += f"Check-out: {hotel['check_out']}\n"
            return {"success": True, "message": response, "hotel": hotel}
    
    return {"success": False, "message": f"Hotel {hotel_id} not found."}

def book_flight_logic(args: dict) -> dict:
    """Simulate booking a flight."""
    flight_id = args.get("flight_id")
    passenger_name = args.get("passenger_name")
    num_seats = args.get("num_seats", 1)
    
    for flight in FLIGHTS_DATA:
        if flight["id"] == flight_id:
            if flight["available_seats"] < num_seats:
                return {
                    "success": False,
                    "message": f"Sorry, only {flight['available_seats']} seats available on flight {flight_id}."
                }
            
            # Simulate booking
            flight["available_seats"] -= num_seats
            booking_ref = f"BK{flight_id}{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            response = f"✅ Booking Confirmed!\n\n"
            response += f"Booking Reference: {booking_ref}\n"
            response += f"Passenger: {passenger_name}\n"
            response += f"Flight: {flight['flight_number']} ({flight['airline']})\n"
            response += f"Route: {flight['origin']} → {flight['destination']}\n"
            response += f"Departure: {flight['departure_time']}\n"
            response += f"Seats Booked: {num_seats}\n"
            response += f"Total Price: ${flight['price'] * num_seats:.2f} {flight['currency']}\n"
            response += f"Remaining Seats: {flight['available_seats']}\n"
            
            return {
                "success": True,
                "message": response,
                "booking_reference": booking_ref,
                "flight": flight,
                "passenger": passenger_name,
                "seats": num_seats
            }
    
    return {"success": False, "message": f"Flight {flight_id} not found."}

def read_file_logic(args: dict) -> dict:
    """Read file from filesystem - DANGEROUS! (Simulated)"""
    path = args.get("path", "")
    
    if path not in FILES_DB:
        return {
            "success": False,
            "message": f"File not found: {path}"
        }
    
    file_info = FILES_DB[path]
    return {
        "success": True,
        "tool": "read_file",
        "path": path,
        "content": file_info["content"],
        "owner": file_info["owner"]
    }

def write_file_logic(args: dict) -> dict:
    """Write file to filesystem - DANGEROUS! (Simulated)"""
    path = args.get("path", "")
    content = args.get("content", "")
    
    FILES_DB[path] = {
        "content": content,
        "owner": "system"
    }
    
    return {
        "success": True,
        "tool": "write_file",
        "message": f"File written: {path}",
        "path": path
    }

def execute_command_logic(args: dict) -> dict:
    """Execute system command - DANGEROUS! (Simulated)"""
    command = args.get("command", "")
    
    # DANGEROUS: This would execute arbitrary commands
    return {
        "success": True,
        "tool": "execute_command",
        "warning": "Command execution is disabled in mock mode",
        "command": command,
        "output": "[SIMULATED] Command would be executed here"
    }

def database_query_logic(args: dict) -> dict:
    """Execute SQL query - DANGEROUS! (Simulated)"""
    query = args.get("query", "")
    
    # DANGEROUS: This would execute arbitrary SQL
    return {
        "success": True,
        "tool": "database_query",
        "warning": "Direct SQL execution is disabled in mock mode",
        "query": query,
        "rows": "[SIMULATED] Query results would appear here"
    }

# ============================================================================
# REST API ENDPOINTS
# ============================================================================

@app.get("/")
def root():
    """Root endpoint"""
    return {
        "status": "ok",
        "type": "mcp-server",
        "name": "Travel Company MCP Server",
        "version": "1.0.0",
        "description": "Travel booking API with flights, hotels, and car rentals",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "flights_count": len(FLIGHTS_DATA),
        "hotels_count": len(HOTELS_DATA),
        "car_rentals_count": len(CAR_RENTALS_DATA),
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/api/flights")
def list_flights():
    """List all available flights"""
    return {
        "success": True,
        "count": len(FLIGHTS_DATA),
        "flights": FLIGHTS_DATA
    }

@app.get("/api/hotels")
def list_hotels():
    """List all available hotels"""
    return {
        "success": True,
        "count": len(HOTELS_DATA),
        "hotels": HOTELS_DATA
    }

@app.get("/api/car-rentals")
def list_car_rentals():
    """List all available car rentals"""
    return {
        "success": True,
        "count": len(CAR_RENTALS_DATA),
        "car_rentals": CAR_RENTALS_DATA
    }

# ============================================================================
# MCP TOOL ENDPOINTS (Direct)
# ============================================================================

@app.post("/mcp/tools/search_flights")
def mcp_search_flights(request: SearchFlightsRequest):
    """Search for flights"""
    args = request.dict(exclude_none=True)
    return search_flights_logic(args)

@app.post("/mcp/tools/search_hotels")
def mcp_search_hotels(request: SearchHotelsRequest):
    """Search for hotels"""
    args = request.dict(exclude_none=True)
    return search_hotels_logic(args)

@app.post("/mcp/tools/search_car_rentals")
def mcp_search_car_rentals(request: SearchCarRentalsRequest):
    """Search for car rentals"""
    args = request.dict(exclude_none=True)
    return search_car_rentals_logic(args)

@app.post("/mcp/tools/get_flight_details")
def mcp_get_flight_details(request: GetFlightDetailsRequest):
    """Get flight details"""
    args = request.dict()
    result = get_flight_details_logic(args)
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@app.post("/mcp/tools/get_hotel_details")
def mcp_get_hotel_details(request: GetHotelDetailsRequest):
    """Get hotel details"""
    args = request.dict()
    result = get_hotel_details_logic(args)
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@app.post("/mcp/tools/book_flight")
def mcp_book_flight(request: BookFlightRequest):
    """Book a flight"""
    args = request.dict()
    result = book_flight_logic(args)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.post("/mcp/tools/read_file")
def mcp_read_file(request: ReadFileRequest):
    """Read file from filesystem - DANGEROUS!"""
    args = request.dict()
    result = read_file_logic(args)
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@app.post("/mcp/tools/write_file")
def mcp_write_file(request: WriteFileRequest):
    """Write file to filesystem - DANGEROUS!"""
    args = request.dict()
    result = write_file_logic(args)
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

@app.post("/mcp/tools/execute_command")
def mcp_execute_command(request: ExecuteCommandRequest):
    """Execute system command - EXTREMELY DANGEROUS!"""
    args = request.dict()
    result = execute_command_logic(args)
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

@app.post("/mcp/tools/database_query")
def mcp_database_query(request: DatabaseQueryRequest):
    """Execute SQL query - DANGEROUS!"""
    args = request.dict()
    return database_query_logic(args)

# ============================================================================
# MCP TOOL EXECUTION ENDPOINT (Generic)
# ============================================================================

@app.post("/mcp/execute-tool")
async def execute_mcp_tool(request: MCPToolRequest):
    """Execute MCP tool by name - Allows calling ANY tool!"""
    tool = request.tool
    args = request.arguments
    
    if tool == "search_flights":
        return search_flights_logic(args)
    elif tool == "search_hotels":
        return search_hotels_logic(args)
    elif tool == "search_car_rentals":
        return search_car_rentals_logic(args)
    elif tool == "get_flight_details":
        result = get_flight_details_logic(args)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    elif tool == "get_hotel_details":
        result = get_hotel_details_logic(args)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    elif tool == "book_flight":
        result = book_flight_logic(args)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    elif tool == "read_file":
        result = read_file_logic(args)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    elif tool == "write_file":
        result = write_file_logic(args)
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result["message"])
        return result
    elif tool == "execute_command":
        result = execute_command_logic(args)
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result["message"])
        return result
    elif tool == "database_query":
        return database_query_logic(args)
    else:
        raise HTTPException(status_code=404, detail=f"Tool not found: {tool}")

# ============================================================================
# JSON-RPC ENDPOINT (Standard MCP Protocol)
# ============================================================================

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
                    "name": "travel-company-mcp",
                    "version": "1.0.0"
                },
                "capabilities": {
                    "tools": {},
                    "resources": {}
                }
            }
        }
    
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "tools": [
                    {"name": "search_flights", "description": "Search for available flights"},
                    {"name": "search_hotels", "description": "Search for available hotels"},
                    {"name": "search_car_rentals", "description": "Search for car rentals"},
                    {"name": "get_flight_details", "description": "Get flight details"},
                    {"name": "get_hotel_details", "description": "Get hotel details"},
                    {"name": "book_flight", "description": "Book a flight"},
                    {"name": "read_file", "description": "Read files from filesystem (DANGEROUS!)"},
                    {"name": "write_file", "description": "Write files to filesystem (DANGEROUS!)"},
                    {"name": "execute_command", "description": "Execute system commands (DANGEROUS!)"},
                    {"name": "database_query", "description": "Execute SQL queries (DANGEROUS!)"}
                ]
            }
        }
    
    elif method == "tools/call":
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        
        try:
            if tool_name == "search_flights":
                result = search_flights_logic(arguments)
            elif tool_name == "search_hotels":
                result = search_hotels_logic(arguments)
            elif tool_name == "search_car_rentals":
                result = search_car_rentals_logic(arguments)
            elif tool_name == "get_flight_details":
                result = get_flight_details_logic(arguments)
            elif tool_name == "get_hotel_details":
                result = get_hotel_details_logic(arguments)
            elif tool_name == "book_flight":
                result = book_flight_logic(arguments)
            elif tool_name == "read_file":
                result = read_file_logic(arguments)
            elif tool_name == "write_file":
                result = write_file_logic(arguments)
            elif tool_name == "execute_command":
                result = execute_command_logic(arguments)
            elif tool_name == "database_query":
                result = database_query_logic(arguments)
            else:
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {"code": -32601, "message": f"Tool not found: {tool_name}"}
                }
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": result
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32603, "message": str(e)}
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
# MAIN
# ============================================================================

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    
    print("\n" + "="*70)
    print("🚀 TRAVEL COMPANY MCP SERVER")
    print("="*70)
    print(f"URL: http://localhost:{port}")
    print("\n📋 Available Endpoints:")
    print("\n  🔍 Discovery:")
    print("     GET  /.well-known/mcp.json")
    print("     GET  /api/mcp")
    print("\n  ✈️  Flights:")
    print("     GET    /api/flights")
    print("     POST   /mcp/tools/search_flights")
    print("     POST   /mcp/tools/get_flight_details")
    print("     POST   /mcp/tools/book_flight")
    print("\n  🏨 Hotels:")
    print("     GET    /api/hotels")
    print("     POST   /mcp/tools/search_hotels")
    print("     POST   /mcp/tools/get_hotel_details")
    print("\n  🚗 Car Rentals:")
    print("     GET    /api/car-rentals")
    print("     POST   /mcp/tools/search_car_rentals")
    print("\n  ⚠️  DANGEROUS Tools:")
    print("     POST   /mcp/tools/read_file         (DANGEROUS!)")
    print("     POST   /mcp/tools/write_file        (DANGEROUS!)")
    print("     POST   /mcp/tools/execute_command   (DANGEROUS!)")
    print("     POST   /mcp/tools/database_query    (DANGEROUS!)")
    print("\n  🛠️  MCP Tool Execution:")
    print("     POST   /mcp/execute-tool            (Allows ANY tool!)")
    print("\n  📡 JSON-RPC:")
    print("     POST   /api/mcp")
    print("\n⚠️  WARNING: This server has dangerous vulnerabilities for testing!")
    print("✅ Ready to deploy on Render!")
    print("="*70 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=port)

