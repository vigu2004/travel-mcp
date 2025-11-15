"""
Travel Tools for FastMCP Server
"""

from typing import Optional
from datetime import datetime

# NOTE: mcp will be passed into register_travel_tools() from main.py

# ------------------------
# In-memory data
# ------------------------

FLIGHTS_DATA = [...]
HOTELS_DATA = [...]
CAR_RENTALS_DATA = [...]


def register_travel_tools(mcp):
    """Register all travel tools on the MCP server"""

    # ---------------------------
    # 1. SEARCH FLIGHTS
    # ---------------------------
    @mcp.tool()
    def search_flights(
        origin: str,
        destination: str,
        date: Optional[str] = None,
        cabin_class: Optional[str] = None
    ) -> dict:

        origin_lower = origin.lower()
        destination_lower = destination.lower()
        results = []

        for flight in FLIGHTS_DATA:
            if origin_lower in flight["origin"].lower() and destination_lower in flight["destination"].lower():
                if cabin_class and flight["class"] != cabin_class:
                    continue
                if date:
                    if flight["departure_time"].split("T")[0] != date:
                        continue
                results.append(flight)

        if results:
            msg = f"Found {len(results)} flight(s):\n\n"
            for f in results:
                msg += (
                    f"🛫 {f['flight_number']} ({f['id']})\n"
                    f"   {f['origin']} → {f['destination']}\n"
                    f"   Depart: {f['departure_time']}\n"
                    f"   Arrive: {f['arrival_time']}\n"
                    f"   Duration: {f['duration']}\n"
                    f"   Class: {f['class']}\n"
                    f"   Price: ${f['price']}\n\n"
                )
        else:
            msg = f"No flights found from {origin} to {destination}"

        return {"success": True, "count": len(results), "message": msg, "flights": results}

    # ---------------------------
    # 2. SEARCH HOTELS
    # ---------------------------
    @mcp.tool()
    def search_hotels(
        location: str,
        check_in: Optional[str] = None,
        check_out: Optional[str] = None,
        min_rating: Optional[int] = None,
        max_price: Optional[float] = None
    ) -> dict:

        location_lower = location.lower()
        results = []

        for h in HOTELS_DATA:
            if location_lower in h["location"].lower():
                if min_rating and h["star_rating"] < min_rating:
                    continue
                if max_price and h["price_per_night"] > max_price:
                    continue
                results.append(h)

        if results:
            msg = f"Found {len(results)} hotels in {location}:\n\n"
            for h in results:
                msg += (
                    f"🏨 {h['name']} ({h['id']})\n"
                    f"   Rating: {h['star_rating']} stars\n"
                    f"   Price: ${h['price_per_night']} / night\n"
                    f"   Rooms: {h['available_rooms']}\n\n"
                )
        else:
            msg = f"No hotels found in {location}"

        return {"success": True, "count": len(results), "message": msg, "hotels": results}

    # ---------------------------
    # 3. SEARCH CAR RENTALS
    # ---------------------------
    @mcp.tool()
    def search_car_rentals(
        location: str,
        car_type: Optional[str] = None,
        max_price: Optional[float] = None
    ) -> dict:

        location_lower = location.lower()
        results = []

        for c in CAR_RENTALS_DATA:
            if location_lower in c["location"].lower():
                if car_type and c["car_type"] != car_type:
                    continue
                if max_price and c["price_per_day"] > max_price:
                    continue
                results.append(c)

        if results:
            msg = f"Found {len(results)} rentals in {location}:\n\n"
            for c in results:
                msg += (
                    f"🚗 {c['car_model']} ({c['id']})\n"
                    f"   Type: {c['car_type']}\n"
                    f"   Price: ${c['price_per_day']} / day\n\n"
                )
        else:
            msg = f"No car rentals found in {location}"

        return {"success": True, "count": len(results), "message": msg, "car_rentals": results}

    # ---------------------------
    # 4. GET FLIGHT DETAILS
    # ---------------------------
    @mcp.tool()
    def get_flight_details(flight_id: str) -> dict:

        for f in FLIGHTS_DATA:
            if f["id"] == flight_id:
                msg = (
                    f"✈️ Flight {flight_id}\n"
                    f"{f['origin']} → {f['destination']}\n"
                    f"Depart: {f['departure_time']}\n"
                    f"Arrive: {f['arrival_time']}\n"
                    f"Duration: {f['duration']}\n"
                    f"Class: {f['class']}\n"
                    f"Price: ${f['price']}\n"
                )
                return {"success": True, "message": msg, "flight": f}

        return {"success": False, "error": f"Flight {flight_id} not found"}

    # ---------------------------
    # 5. GET HOTEL DETAILS
    # ---------------------------
    @mcp.tool()
    def get_hotel_details(hotel_id: str) -> dict:

        for h in HOTELS_DATA:
            if h["id"] == hotel_id:
                msg = (
                    f"🏨 {h['name']}\n"
                    f"{h['location']}\n"
                    f"Price: ${h['price_per_night']} / night\n"
                    f"Rooms: {h['available_rooms']}\n"
                )
                return {"success": True, "message": msg, "hotel": h}

        return {"success": False, "error": f"Hotel {hotel_id} not found"}

    # ---------------------------
    # 6. BOOK FLIGHT
    # ---------------------------
    @mcp.tool()
    def book_flight(
        flight_id: str,
        passenger_name: str,
        num_seats: int = 1
    ) -> dict:

        for f in FLIGHTS_DATA:
            if f["id"] == flight_id:

                if f["available_seats"] < num_seats:
                    return {"success": False, "error": "Not enough seats"}

                f["available_seats"] -= num_seats
                ref = f"BK{flight_id}{datetime.now().strftime('%Y%m%d%H%M%S')}"

                msg = (
                    f"Booking Confirmed!\n"
                    f"Ref: {ref}\n"
                    f"Passenger: {passenger_name}\n"
                    f"Seats: {num_seats}\n"
                )

                return {
                    "success": True,
                    "message": msg,
                    "booking_reference": ref,
                    "flight": f,
                    "passenger": passenger_name,
                    "seats": num_seats
                }

        return {"success": False, "error": f"Flight {flight_id} not found"}
