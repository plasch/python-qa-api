import requests

headers = {
    'User-Agent': 'Anonymous'
}
response = requests.get('https://httpbin.org/get', headers=headers)

for key, value in response.headers.items():
    print(f'{key}: {value}')

"""Returns string content of the response, in unicode."""
body_str = response.text

"""Returns content of the response, in bytes."""
body_b_str = response.content

"""Returns dict() the json-encoded content of a response."""
body_json = response.json()
print('Headers:', body_json['headers'])
