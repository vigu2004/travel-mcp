#!/usr/bin/env python3
"""
Travel Company MCP Server
Provides in-memory travel data including flights, hotels, and car rentals.
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Any, Optional
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("travel-mcp-server")

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

# Create server instance
server = Server("travel-company-mcp")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools for the travel MCP server.
    """
    return [
        types.Tool(
            name="search_flights",
            description="Search for available flights based on origin, destination, and optional date range. Returns flight details including price, times, and availability.",
            inputSchema={
                "type": "object",
                "properties": {
                    "origin": {
                        "type": "string",
                        "description": "Origin city or airport code (e.g., 'New York', 'JFK')"
                    },
                    "destination": {
                        "type": "string",
                        "description": "Destination city or airport code (e.g., 'London', 'LHR')"
                    },
                    "date": {
                        "type": "string",
                        "description": "Optional: Departure date in YYYY-MM-DD format"
                    },
                    "class": {
                        "type": "string",
                        "description": "Optional: Cabin class (Economy, Business, First)",
                        "enum": ["Economy", "Business", "First"]
                    }
                },
                "required": ["origin", "destination"]
            }
        ),
        types.Tool(
            name="search_hotels",
            description="Search for available hotels in a specific location. Returns hotel details including price, amenities, and availability.",
            inputSchema={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City or location name (e.g., 'London', 'Tokyo')"
                    },
                    "check_in": {
                        "type": "string",
                        "description": "Optional: Check-in date in YYYY-MM-DD format"
                    },
                    "check_out": {
                        "type": "string",
                        "description": "Optional: Check-out date in YYYY-MM-DD format"
                    },
                    "min_rating": {
                        "type": "number",
                        "description": "Optional: Minimum star rating (1-5)"
                    },
                    "max_price": {
                        "type": "number",
                        "description": "Optional: Maximum price per night in USD"
                    }
                },
                "required": ["location"]
            }
        ),
        types.Tool(
            name="search_car_rentals",
            description="Search for available car rentals at a specific location. Returns car details including model, type, price, and features.",
            inputSchema={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Pickup location (e.g., 'London Heathrow Airport', 'Tokyo')"
                    },
                    "car_type": {
                        "type": "string",
                        "description": "Optional: Type of car (Sedan, SUV, Compact, Luxury Sedan, Hatchback)"
                    },
                    "max_price": {
                        "type": "number",
                        "description": "Optional: Maximum price per day in USD"
                    }
                },
                "required": ["location"]
            }
        ),
        types.Tool(
            name="get_flight_details",
            description="Get detailed information about a specific flight by flight ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "flight_id": {
                        "type": "string",
                        "description": "The unique flight ID (e.g., 'FL001')"
                    }
                },
                "required": ["flight_id"]
            }
        ),
        types.Tool(
            name="get_hotel_details",
            description="Get detailed information about a specific hotel by hotel ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "hotel_id": {
                        "type": "string",
                        "description": "The unique hotel ID (e.g., 'HTL001')"
                    }
                },
                "required": ["hotel_id"]
            }
        ),
        types.Tool(
            name="book_flight",
            description="Book a flight (simulated). Returns booking confirmation.",
            inputSchema={
                "type": "object",
                "properties": {
                    "flight_id": {
                        "type": "string",
                        "description": "The unique flight ID to book"
                    },
                    "passenger_name": {
                        "type": "string",
                        "description": "Passenger full name"
                    },
                    "num_seats": {
                        "type": "number",
                        "description": "Number of seats to book (default: 1)"
                    }
                },
                "required": ["flight_id", "passenger_name"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Handle tool execution requests.
    """
    if not arguments:
        arguments = {}
    
    if name == "search_flights":
        return await search_flights(arguments)
    elif name == "search_hotels":
        return await search_hotels(arguments)
    elif name == "search_car_rentals":
        return await search_car_rentals(arguments)
    elif name == "get_flight_details":
        return await get_flight_details(arguments)
    elif name == "get_hotel_details":
        return await get_hotel_details(arguments)
    elif name == "book_flight":
        return await book_flight(arguments)
    else:
        raise ValueError(f"Unknown tool: {name}")

async def search_flights(args: dict) -> list[types.TextContent]:
    """Search for flights based on criteria."""
    origin = args.get("origin", "").lower()
    destination = args.get("destination", "").lower()
    date = args.get("date")
    cabin_class = args.get("class")
    
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
    
    return [types.TextContent(type="text", text=response)]

async def search_hotels(args: dict) -> list[types.TextContent]:
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
    
    return [types.TextContent(type="text", text=response)]

async def search_car_rentals(args: dict) -> list[types.TextContent]:
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
    
    return [types.TextContent(type="text", text=response)]

async def get_flight_details(args: dict) -> list[types.TextContent]:
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
            return [types.TextContent(type="text", text=response)]
    
    return [types.TextContent(type="text", text=f"Flight {flight_id} not found.")]

async def get_hotel_details(args: dict) -> list[types.TextContent]:
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
            return [types.TextContent(type="text", text=response)]
    
    return [types.TextContent(type="text", text=f"Hotel {hotel_id} not found.")]

async def book_flight(args: dict) -> list[types.TextContent]:
    """Simulate booking a flight."""
    flight_id = args.get("flight_id")
    passenger_name = args.get("passenger_name")
    num_seats = args.get("num_seats", 1)
    
    for flight in FLIGHTS_DATA:
        if flight["id"] == flight_id:
            if flight["available_seats"] < num_seats:
                return [types.TextContent(
                    type="text",
                    text=f"Sorry, only {flight['available_seats']} seats available on flight {flight_id}."
                )]
            
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
            
            return [types.TextContent(type="text", text=response)]
    
    return [types.TextContent(type="text", text=f"Flight {flight_id} not found.")]

async def main():
    """Run the MCP server using stdio transport."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        logger.info("Travel MCP Server starting...")
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="travel-company-mcp",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())

