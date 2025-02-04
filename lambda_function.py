import json
import math
import requests

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number"""
    if n < 1:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

def digit_sum(n):
    """Calculate the sum of digits"""
    return sum(int(digit) for digit in str(abs(int(n))))  # Use abs() to handle negatives

def get_fun_fact(n):
    """Fetch fun fact from Numbers API"""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact found.")
        return "No fun fact available."
    except:
        return "Could not fetch fun fact."

def lambda_handler(event, context):
    try:
        # Get query parameter
        number_str = event.get("queryStringParameters", {}).get("number", None)

        # Validate input
        if number_str is None or not number_str.replace("-", "").replace(".", "").isdigit():
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"number": number_str, "error": True})
            }

        number = float(number_str) if "." in number_str else int(number_str)  # Handle floats

        # Determine properties
        properties = []
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        if number == sum(int(digit) ** len(str(number)) for digit in str(abs(int(number)))):  # Armstrong check
            properties.insert(0, "armstrong")

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
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
