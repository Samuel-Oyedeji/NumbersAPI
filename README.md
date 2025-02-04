# Number Classification API

## Overview
The **Number Classification API** is a serverless application hosted on AWS Lambda and exposed via API Gateway. It takes a number as a query parameter and returns interesting mathematical properties, including whether the number is prime, perfect, an Armstrong number, and a fun fact.

## Features
- Determines if a number is **prime** and **perfect**.
- Identifies special properties like **Armstrong** and **odd/even**.
- Computes the **sum of digits**.
- Fetches a **fun fact** about the number from Numbers API.
- Handles **CORS** for cross-origin requests.
- Returns **JSON responses** with appropriate HTTP status codes.

## API Specification
**Endpoint:**
```
GET <your-api-url>/api/classify-number?number=371
```

**Response Example (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Response Example (400 Bad Request):**
```json
{
    "number": "invalid_input",
    "error": true
}
```

---

## Deployment Guide
This guide walks you through deploying the Number Classification API using AWS Lambda and API Gateway.

### **1. Create an AWS Lambda Function**
1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to **AWS Lambda** and click **Create function**.
3. Select **Author from scratch** and enter:
   - **Function name**: `NumberClassificationAPI`
   - **Runtime**: Python 3.x
   - **Execution role**: Create a new role with basic Lambda permissions.
4. Click **Create function**.

### **2. Upload the Lambda Code**
1. In the Lambda function page, go to **Code** and click **Upload from** → `.zip file`.
2. Upload the ZIP file containing your function code and dependencies (ensure `requests` is included).
3. Click **Deploy**.

### **3. Set Up API Gateway**
1. Navigate to **API Gateway** in AWS Console.
2. Click **Create API** → **HTTP API** → **Build**.
3. Set API name to `NumberClassificationAPI` and click **Next**.
4. **Add Integration:**
   - Choose **Lambda Function**.
   - Select the Lambda function `NumberClassificationAPI`.
   - Click **Next**.
5. **Configure Routes:**
   - Set **Method**: `GET`
   - Set **Resource Path**: `/api/classify-number`
   - Click **Next**.
6. **Review and Create API**, then **Deploy**.

### **4. Enable CORS in API Gateway**
1. In API Gateway, navigate to your API and go to **CORS settings**.
2. Set allowed origins to `*`.
3. Set allowed methods to `GET`.
4. Add response headers:
   - `Access-Control-Allow-Headers`: `Content-Type`
   - `Access-Control-Allow-Methods`: `GET`
   - `Access-Control-Allow-Origin`: `*`
5. Save and redeploy the API.

### **5. Test the API**
1. Copy your **Invoke URL** from API Gateway.
2. Test the API using a browser, Postman, or curl:
   ```sh
   curl -X GET "<your-api-url>/api/classify-number?number=371"
   ```
3. Ensure you receive a valid JSON response.

### **6. Update IAM Role (If Needed)**
If you encounter permission errors, update the IAM role attached to the Lambda function:
1. Go to **IAM** → **Roles**.
2. Find the role associated with your Lambda function.
3. Attach policies for **AWSLambdaBasicExecutionRole** and **AmazonAPIGatewayInvokeFullAccess**.

---

## Version Control & Repository Structure
Ensure your code is hosted on **GitHub** with a well-structured repository:
```bash
NumberClassificationAPI/
│-- lambda_function.py  # Main API logic
│-- requirements.txt    # Dependencies
│-- README.md           # Documentation
│-- deploy.sh           # Deployment script (optional)
│-- tests/              # Test cases
```

### **GitHub Setup Steps**
1. Create a GitHub repository.
2. Clone the repo locally:
   ```sh
   git clone https://github.com/yourusername/NumberClassificationAPI.git
   ```
3. Add your project files and commit:
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

---

## Conclusion
Your **Number Classification API** is now fully deployed and accessible. 🚀 Test your endpoint, validate responses, and share your API URL.

If you run into issues, check **CloudWatch Logs** in AWS Lambda for debugging. Happy coding! 🎉

