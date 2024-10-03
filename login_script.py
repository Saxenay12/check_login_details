import os
import requests

# Function to process login and save successful attempts
def process_login(url, username, password):
    try:
        # Prepare the payload for POST request (adjust if needed based on the login form structure)
        payload = {
            'username': username,
            'password': password
        }
        
        # Make the POST request
        response = requests.post(url, data=payload)
        
        # Check for success in the response (adjust if needed based on how success is identified)
        if response.status_code == 200 and "dashboard" in response.text.lower():  # assuming 'dashboard' is in successful login response
            print(f"Success: {url} | Username: {username} | Password: {password}")
            save_successful_login(url, username, password)
        else:
            print(f"Failed: {url} | Username: {username} | Password: {password}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

# Function to save successful login attempts to a file
def save_successful_login(url, username, password):
    if not os.path.exists("successful_logins"):
        os.mkdir("successful_logins")
    
    with open("successful_logins/successful_logins.txt", "a") as file:
        file.write(f"{url} | Username: {username} | Password: {password}\n")

# Function to read from data.txt and process each line
def process_data_file():
    try:
        with open('data.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    # Split the line into URL, username, and password
                    url, username, password = line.split(':')
                    
                    # Process the login
                    print(f"Attempting to login: {url} | Username: {username} | Password: {password}")
                    process_login(url, username, password)
    
    except FileNotFoundError:
        print("The file 'data.txt' was not found.")

# Main function to run the program
if __name__ == "__main__":
    process_data_file()
