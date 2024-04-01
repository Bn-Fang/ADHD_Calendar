import requests

API_URL = 'https://umich.instructure.com'
ACCESS_TOKEN = '1770~J0C9UF2351Ul7N9LyT0Tx9dAQDRTzV8L7upIXegJTsPXaXjvcUcUnCzI6Xu9Prvo'

# Construct the request headers with the access token
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# Make the GET request to the API endpoint
response = requests.get(f'{API_URL}/courses', headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Handle the data returned from the API
    print(data)
else:
    # Print an error message if the request was unsuccessful
    print(f'Error: {response.status_code}')

