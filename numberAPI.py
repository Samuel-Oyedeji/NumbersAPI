import json
import urllib.request

def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

def lambda_handler(event, context):
    # Safely extract queryStringParameters
    query_params = event.get("queryStringParameters", {})

    # Ensure the 'number' parameter exists
    if not query_params or "number" not in query_params:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": True, "message": "Missing 'number' query parameter"})
        }

    number_str = query_params["number"]

    # Ensure the input is a valid integer
    try:
        number = int(number_str)
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": True, "message": "Invalid number format"})
        }

    # Calculate properties
    is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
    is_perfect = sum(i for i in range(1, number) if number % i == 0) == number
    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.insert(0, "armstrong")

    digit_sum = sum(int(d) for d in str(number))

    # Get fun fact from Numbers API
    try:
        fun_fact = urllib.request.urlopen(f"http://numbersapi.com/{number}/math").read().decode('utf-8')
    except:
        fun_fact = "No fun fact available."

    # Return response
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # CORS support
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })
    }
