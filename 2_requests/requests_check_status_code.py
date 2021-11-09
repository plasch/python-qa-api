import requests

response = requests.get('https://httpbin.org/get')
if response.status_code == 200:
    print('OK!')

"""Returns True if status_code is less than 400, otherwise False."""
if response.ok:
    print('OK!')

"""Raises HTTPError`, if one occurred: 4XX-6XX."""
response.raise_for_status()
