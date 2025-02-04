import json
import re
import requests

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d ** length for d in digits) == n

def digit_sum(n):
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math?json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("text", "No fun fact available.")
    except requests.RequestException:
        return "No fun fact available."

def lambda_handler(event, context):
    try:
        # Safely get query parameters
        query_params = event.get("queryStringParameters", {}) or {}
        if "number" not in query_params:
            raise ValueError("Missing 'number' parameter")
        
        number_str = query_params["number"]
        # Validate input with regex (non-negative integer)
        if not re.fullmatch(r'^\d+$', number_str):
            raise ValueError("Invalid input: not a number")
        
        number = int(number_str)

        # Calculate properties
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("even" if number % 2 == 0 else "odd")

        # Build response
        response = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": get_fun_fact(number)
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps(response)
        }

    except ValueError as e:
        # Handle invalid input
        return {
            "statusCode": 400,
            "body": json.dumps({
                "number": event.get("queryStringParameters", {}).get("number", "invalid"),
                "error": True,
                "message": str(e)
            }, indent=4),
            "headers": {"Content-Type": "application/json"}
        }
    except Exception as e:
        # Catch-all for unexpected errors
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": True,
                "message": "Internal server error"
            }),
            "headers": {"Content-Type": "application/json"}
        }
