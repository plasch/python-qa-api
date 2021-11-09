import requests

payload_one = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=payload_one)
print(response.url)

# Можно передать список параметров в качестве значения
payload_two = {'key1': 'value1', 'key2': ['value2', 'value3']}
response = requests.get('https://httpbin.org/get', params=payload_two)
print(response.url)
