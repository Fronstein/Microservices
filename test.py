import requests

# Base URL of the microservice
BASE_URL = "http://127.0.0.1:5000"

# Function to get a student by ID
def get_student(student_id):
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
    elif response.status_code == 404:
        print("Error:", response.json()['error'])
    else:
        print("Unexpected error:", response.json())

# Test the microservice
if __name__ == "__main__":
    student_id = int(input("Enter student ID to retrieve: "))
    get_student(student_id)
    