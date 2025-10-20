import requests
import json

# Fetch JSON data from the URL
url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    comments = response.json()
    
    # Filter and print comments where author email ends with .com
    for comment in comments:
        if comment['email'].endswith('.com'):
            print(f"Comment: {comment['body']}")
            print(f"Author: {comment['name']} ({comment['email']})")
            print("-" * 100)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
