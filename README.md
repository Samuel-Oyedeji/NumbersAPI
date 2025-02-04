# Number Classification API

## Overview
The **Number Classification API** is a serverless application hosted on AWS Lambda and exposed via API Gateway. It takes a number as a query parameter and returns interesting mathematical properties, including whether the number is prime, perfect, an Armstrong number, and a fun fact.

## Prerequisites
- An AWS account
- Basic knowledge of AWS Lambda and API Gateway

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
This guide walks you through deploying the **Number Classification API** on AWS using **AWS Lambda** and **API Gateway (REST API)**.

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
3. **Set Handler**    - Ensure the handler name matches your main function (e.g., `lambda_function.lambda_handler` if your file is `lambda_function.py`)
4.    - Click **Deploy**

### **3. Set Up API Gateway (REST API)**
1. **Navigate to API Gateway**
   - Go to the AWS Management Console
   - Search for **API Gateway** and open the service

2. **Create a New API**
   - Click **Create API**
   - Select **REST API** (not HTTP or WebSocket)
   - Choose **Build**
   - Set an **API name** (e.g., `NumberClassificationAPI`)
   - Click **Create API**

3. **Create a New Resource**
   - In the **Resources** section, click **Actions → Create Resource**
   - Set **Resource Name**: `classify-number`
   - Click **Create Resource**

4. **Create a Method (GET)**
   - Select the `classify-number` resource
   - Click **Actions → Create Method**
   - Choose **GET** and click the checkmark
   - In the **Integration Type**, select **Lambda Function**
   - Enter the name of your Lambda function (e.g., `NumberClassificationAPI`)
   - Click **Save** and confirm the permissions

5. **Enable Lambda Proxy Integration**
   - Select the **GET method**
   - Check **Use Lambda Proxy Integration**
   - Click **Save**

### **4. Enable CORS in API Gateway**
1. In API Gateway, navigate to your API and go to **CORS settings**.
2. Set allowed origins to `*`.
3. Set allowed methods to `GET`.
4. Add response headers:
   - `Access-Control-Allow-Headers`: `Content-Type`
   - `Access-Control-Allow-Methods`: `GET`
   - `Access-Control-Allow-Origin`: `*`
5. Save
6. **Create a Deployment Stage**
   - Click **Actions → Deploy API**
   - Create a new stage (e.g., `prod`)
   - Click **Deploy**

7. **Get the Invoke URL**
   - After deployment, copy the **Invoke URL** from the **Stages** section
   - Your API will be accessible at:
     ```
     https://your-api-id.execute-api.your-region.amazonaws.com/prod/api/classify-number?number=371
     ```

### **5. Test the API**
1. Copy your **Invoke URL** from API Gateway.
2. Test the API using a browser, Postman, or curl:
   ```sh
   curl -X GET "<your-api-url>/api/classify-number?number=371"
   ```
3. Ensure you receive a valid JSON response.


---

## Conclusion
Your **Number Classification API** is now fully deployed and accessible. 🚀 Test your endpoint, validate responses, and share your API URL.

Happy coding! 🎉

