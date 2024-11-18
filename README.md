# Microservices
 

## Overview
This Is flask based microservice that uses REST API to provide endpoint that allows users to retrive Student information from MySQL Database based on student ID 



## How to Programmatically REQUEST Data

To request Data we need to send HTTP GET request to the endpoint with desired student ID. We can do this with any HTTP client library. 

### Example code using python request

```

import requests

# Define the base URL of the microservice
BASE_URL = "http://127.0.0.1:5000"

# Define the student ID to retrieve
student_id = 1

# Make the GET request
response = requests.get(f"{BASE_URL}/get-student/{student_id}")

```

## How to Programmatically Recive Data

After sending Get request We can check HTTP status , if everything went well status code will be 200 and and we would have recived student data as response in JSON format. 
Now we can print this and use as is or we can Parse JSON file for any specific data we want. 

### example code of reciving response

```
response = requests.get(f"{BASE_URL}/get-student/{student_id}")
    if response.status_code == 200:
        print("Student Information JSON Format: ", response.json())
        student_data = response.json()
        print("Student Information:")
        print(f"ID: {student_data['id']}")
        print(f"Name: {student_data['name']}")
        print(f"Email: {student_data['email']}")
        print(f"Major: {student_data['major']}")
        print(f"Graduation Date: {student_data['graduation_date']}")
        print(f"Phone Number: {student_data['phone_number']}")

```

this code we recived response after GET request and if code is 200 we can print JSON file or parse it for specific data.

