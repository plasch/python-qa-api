import requests

# Using mitmproxy, mitmweb
proxy = {
    'http': 'http://localhost:8080',
    'https': 'https://localhost:8080'
}

response = requests.get('https://httpbin.org/get', proxies=proxy, verify=False)
