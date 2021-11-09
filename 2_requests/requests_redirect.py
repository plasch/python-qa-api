import requests

url = 'https://httpbin.org/absolute-redirect/3'

response = requests.get(url)
print(response.status_code)

# Отслеживать историю редиректов
print(response.history)

# Отключить обработку редиректа
response = requests.get(url, allow_redirects=False)
print(response.status_code)

# Прекратить ожидать ответ после определенного количества секунд
response = requests.get(url, allow_redirects=False, timeout=0.001)
