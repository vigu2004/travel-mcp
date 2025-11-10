#!/usr/bin/env python3
"""
Test script for Travel MCP Server vulnerabilities
Tests all the new vulnerable tools to ensure they work correctly
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_tool(tool_name, params):
    """Test a specific MCP tool"""
    print(f"\n{'='*70}")
    print(f"Testing: {tool_name}")
    print(f"{'='*70}")
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": params
        }
    }
    
    try:
        response = requests.post(f"{BASE_URL}/mcp/v1", json=payload, timeout=10)
        result = response.json()
        
        print(f"Status: {response.status_code}")
        print(f"Result: {json.dumps(result, indent=2)}")
        
        if "result" in result:
            print(f"✅ Tool executed successfully")
            return True
        else:
            print(f"❌ Tool failed: {result.get('error', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"❌ Request failed: {str(e)}")
        return False


def main():
    print("\n" + "="*70)
    print("🧪 TRAVEL MCP VULNERABILITY TESTS")
    print("="*70)
    print("\nMake sure the Travel MCP Server is running on http://localhost:8000")
    print("Start it with: python travel_mcp_server.py")
    
    input("\nPress Enter to continue...")
    
    # Test 1: Calculate trip cost (eval injection)
    test_tool("calculate_trip_cost", {
        "base_price": 1000.0,
        "calculation_formula": "base_price * 1.15"
    })
    
    # Test 2: Apply discount code (eval injection)
    test_tool("apply_discount_code", {
        "price": 1000.0,
        "discount_code": "price * 0.8"
    })
    
    # Test 3: Generate booking confirmation (format string)
    test_tool("generate_booking_confirmation", {
        "passenger_name": "John Smith",
        "flight_id": "FL001",
        "template": "Dear {passenger_name}, your booking for {flight_id} is confirmed."
    })
    
    # Test 4: Search booking by name (SQL injection)
    test_tool("search_booking_by_name", {
        "passenger_name": "John Smith"
    })
    
    # Test 5: Download travel document (path traversal)
    # This will fail to actually read files but should show the vulnerability
    test_tool("download_travel_document", {
        "document_path": "tickets/FL001.pdf"
    })
    
    # Test 6: Fetch destination info (SSRF)
    test_tool("fetch_destination_info", {
        "api_url": "https://httpbin.org/json"
    })
    
    # Test 7: Read file (path traversal)
    test_tool("read_file", {
        "path": "travel_mcp_server.py"
    })
    
    # Test 8: Database query (SQL injection)
    test_tool("database_query", {
        "query": "SELECT * FROM users"
    })
    
    # Test 9: Execute command (command injection)
    test_tool("execute_command", {
        "command": "echo 'Hello from MCP!'"
    })
    
    print("\n" + "="*70)
    print("🏁 TEST SUITE COMPLETE")
    print("="*70)
    print("\n📊 Summary:")
    print("   All vulnerable tools have been tested")
    print("   Review the output above to verify functionality")
    print("   Now run your security scanner to detect these vulnerabilities!")
    print("\n⚠️  Remember: These vulnerabilities are intentional for testing!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()

