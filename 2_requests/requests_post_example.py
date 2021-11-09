import requests

headers = {
    'User-Agent': 'Anonymous'
}
response = requests.post('https://httpbin.org/post',
                         headers=headers,
                         params={'key1': 'value1', 'key2': 'value2'},
                         json={'username': 'superuser'})
print(response.text)
