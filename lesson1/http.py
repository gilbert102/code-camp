def http(url):
    return url.replace("http://", "https://").replace("HTTP://", "HTTPS://")

url = http("http://www.example.com")
print(url)
