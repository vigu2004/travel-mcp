"""
Simple test script to verify the refactored FastMCP travel server
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_server_health():
    """Test if server is running"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print("✅ Server is running!")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Text: {response.text[:200]}")
        return True
    except Exception as e:
        print(f"❌ Server not running: {e}")
        return False

def test_search_flights():
    """Test search_flights tool"""
    try:
        # Note: FastMCP uses JSON-RPC format
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "search_flights",
                "arguments": {
                    "origin": "New York",
                    "destination": "London"
                }
            },
            "id": 1
        }
        response = requests.post(f"{BASE_URL}/api/mcp", json=payload)
        result = response.json()
        print("\n✅ search_flights tool works!")
        if "result" in result:
            flights = result["result"].get("flights", [])
            print(f"   Found {len(flights)} flights")
        return True
    except Exception as e:
        print(f"\n❌ search_flights failed: {e}")
        return False

def test_search_hotels():
    """Test search_hotels tool"""
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "search_hotels",
                "arguments": {
                    "location": "London"
                }
            },
            "id": 2
        }
        response = requests.post(f"{BASE_URL}/api/mcp", json=payload)
        result = response.json()
        print("\n✅ search_hotels tool works!")
        if "result" in result:
            hotels = result["result"].get("hotels", [])
            print(f"   Found {len(hotels)} hotels")
        return True
    except Exception as e:
        print(f"\n❌ search_hotels failed: {e}")
        return False

def test_tools_list():
    """Test listing all available tools"""
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/list",
            "params": {},
            "id": 3
        }
        response = requests.post(f"{BASE_URL}/api/mcp", json=payload)
        result = response.json()
        print("\n✅ Tools list endpoint works!")
        if "result" in result and "tools" in result["result"]:
            tools = result["result"]["tools"]
            print(f"   Available tools: {len(tools)}")
            for tool in tools:
                print(f"   - {tool['name']}")
        return True
    except Exception as e:
        print(f"\n❌ Tools list failed: {e}")
        return False

if __name__ == "__main__":
    print("="*70)
    print("🧪 Testing Refactored FastMCP Travel Server")
    print("="*70)
    
    # Run tests
    if test_server_health():
        test_tools_list()
        test_search_flights()
        test_search_hotels()
    
    print("\n" + "="*70)
    print("✅ All tests completed!")
    print("="*70 + "\n")

