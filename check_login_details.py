import requests

def check_login_details(url, email, password):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            payload = {"email": email, "password": password}
            login_response = requests.post(url, data=payload)
            if login_response.status_code == 200:
                return True
            else:
                return False
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking {url}: {e}")
        return False

def process_data(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(':')
            if len(data) == 3:
                url, email, password = data
                if check_login_details(url, email, password):
                    print(f"Login successful for {url}")
                else:
                    print(f"Login failed for {url}")
            else:
                print(f"Invalid data format: {line}")

# Example usage
file_path = './data.txt'  # Replace with your file path
process_data(file_path)
