"""
Travel Tools for FastMCP Server
Contains all travel-related tool registrations
"""
from typing import List, Dict, Any, Optional
from datetime import datetime

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


def register_travel_tools(app):
    """Register travel booking tools with the MCP app"""
    
    @app.tool()
    def search_flights(
        origin: str,
        destination: str,
        date: Optional[str] = None,
        cabin_class: Optional[str] = None
    ) -> dict:
        """
        Search for available flights based on origin, destination, and optional filters.
        
        Args:
            origin: Origin city or airport code (e.g., "New York", "JFK")
            destination: Destination city or airport code (e.g., "London", "LHR")
            date: Optional departure date in YYYY-MM-DD format
            cabin_class: Optional cabin class (Economy, Business, First)
        
        Returns:
            Dictionary with search results including flight details
        
        Examples:
            >>> search_flights("New York", "London")
            >>> search_flights("Los Angeles", "Tokyo", date="2025-11-20")
            >>> search_flights("New York", "London", cabin_class="Business")
        """
        origin_lower = origin.lower()
        destination_lower = destination.lower()
        
        results = []
        for flight in FLIGHTS_DATA:
            if origin_lower in flight["origin"].lower() and destination_lower in flight["destination"].lower():
                if cabin_class and flight["class"] != cabin_class:
                    continue
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
    
    
    @app.tool()
    def search_hotels(
        location: str,
        check_in: Optional[str] = None,
        check_out: Optional[str] = None,
        min_rating: Optional[int] = None,
        max_price: Optional[float] = None
    ) -> dict:
        """
        Search for available hotels in a specific location.
        
        Args:
            location: City or location name (e.g., "London", "Tokyo")
            check_in: Optional check-in date in YYYY-MM-DD format
            check_out: Optional check-out date in YYYY-MM-DD format
            min_rating: Optional minimum star rating (1-5)
            max_price: Optional maximum price per night in USD
        
        Returns:
            Dictionary with search results including hotel details
        
        Examples:
            >>> search_hotels("London")
            >>> search_hotels("Tokyo", min_rating=4)
            >>> search_hotels("Dubai", max_price=400)
        """
        location_lower = location.lower()
        
        results = []
        for hotel in HOTELS_DATA:
            if location_lower in hotel["location"].lower():
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
    
    
    @app.tool()
    def search_car_rentals(
        location: str,
        car_type: Optional[str] = None,
        max_price: Optional[float] = None
    ) -> dict:
        """
        Search for available car rentals at a specific location.
        
        Args:
            location: Pickup location (e.g., "London Heathrow", "Tokyo Airport")
            car_type: Optional type of car (Sedan, SUV, Compact, etc.)
            max_price: Optional maximum price per day in USD
        
        Returns:
            Dictionary with search results including car rental details
        
        Examples:
            >>> search_car_rentals("London")
            >>> search_car_rentals("Tokyo", car_type="Compact")
            >>> search_car_rentals("Dubai", max_price=100)
        """
        location_lower = location.lower()
        
        results = []
        for car in CAR_RENTALS_DATA:
            if location_lower in car["location"].lower():
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
    
    
    @app.tool()
    def get_flight_details(flight_id: str) -> dict:
        """
        Get detailed information about a specific flight by ID.
        
        Args:
            flight_id: The unique flight ID (e.g., "FL001")
        
        Returns:
            Dictionary with detailed flight information
        
        Examples:
            >>> get_flight_details("FL001")
        """
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
        
        return {"success": False, "error": f"Flight {flight_id} not found."}
    
    
    @app.tool()
    def get_hotel_details(hotel_id: str) -> dict:
        """
        Get detailed information about a specific hotel by ID.
        
        Args:
            hotel_id: The unique hotel ID (e.g., "HTL001")
        
        Returns:
            Dictionary with detailed hotel information
        
        Examples:
            >>> get_hotel_details("HTL001")
        """
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
        
        return {"success": False, "error": f"Hotel {hotel_id} not found."}
    
    
    @app.tool()
    def book_flight(
        flight_id: str,
        passenger_name: str,
        num_seats: int = 1
    ) -> dict:
        """
        Book a flight (simulated booking).
        
        Args:
            flight_id: The unique flight ID to book (e.g., "FL001")
            passenger_name: Passenger full name
            num_seats: Number of seats to book (default: 1)
        
        Returns:
            Dictionary with booking confirmation details
        
        Examples:
            >>> book_flight("FL001", "John Smith")
            >>> book_flight("FL002", "Jane Doe", num_seats=2)
        """
        for flight in FLIGHTS_DATA:
            if flight["id"] == flight_id:
                if flight["available_seats"] < num_seats:
                    return {
                        "success": False,
                        "error": f"Sorry, only {flight['available_seats']} seats available on flight {flight_id}."
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
        
        return {"success": False, "error": f"Flight {flight_id} not found."}
    
    
    @app.tool()
    def read_file(path: str) -> dict:
        """
        Read file from filesystem - DANGEROUS! (Simulated for testing)
        
        Args:
            path: Absolute file path
        
        Returns:
            Dictionary with file content
        
        Examples:
            >>> read_file("/home/travel/bookings.txt")
        
        Warning:
            This is a DANGEROUS operation in production! Only simulated here.
        """
        if path not in FILES_DB:
            return {
                "success": False,
                "error": f"File not found: {path}"
            }
        
        file_info = FILES_DB[path]
        return {
            "success": True,
            "tool": "read_file",
            "path": path,
            "content": file_info["content"],
            "owner": file_info["owner"]
        }
    
    
    @app.tool()
    def write_file(path: str, content: str) -> dict:
        """
        Write content to file - DANGEROUS! (Simulated for testing)
        
        Args:
            path: File path
            content: Content to write
        
        Returns:
            Dictionary with operation status
        
        Examples:
            >>> write_file("/home/travel/test.txt", "Hello World")
        
        Warning:
            This is a DANGEROUS operation in production! Only simulated here.
        """
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
    
    
    @app.tool()
    def execute_command(command: str) -> dict:
        """
        Execute system command - EXTREMELY DANGEROUS! (Simulated for testing)
        
        Args:
            command: Shell command to execute
        
        Returns:
            Dictionary with command output (simulated)
        
        Examples:
            >>> execute_command("ls -la")
        
        Warning:
            This is an EXTREMELY DANGEROUS operation! Only simulated here.
        """
        return {
            "success": True,
            "tool": "execute_command",
            "warning": "Command execution is disabled in mock mode",
            "command": command,
            "output": "[SIMULATED] Command would be executed here"
        }
    
    
    @app.tool()
    def database_query(query: str) -> dict:
        """
        Execute SQL query - DANGEROUS! (Simulated for testing)
        
        Args:
            query: SQL query to execute
        
        Returns:
            Dictionary with query results (simulated)
        
        Examples:
            >>> database_query("SELECT * FROM bookings")
        
        Warning:
            This is a DANGEROUS operation! Only simulated here.
        """
        return {
            "success": True,
            "tool": "database_query",
            "warning": "Direct SQL execution is disabled in mock mode",
            "query": query,
            "rows": "[SIMULATED] Query results would appear here"
        }

