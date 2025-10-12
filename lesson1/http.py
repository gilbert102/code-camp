def http(url):
    """Convert HTTP protocol to HTTPS (handles both upper and lowercase)"""
    return url.replace("http://", "https://").replace("HTTP://", "HTTPS://")

url = http("http://www.example.com")  # Convert test URL https://www.example.com
print(url)  # Expected: https://www.example.com
