import requests

ya = 'https://ya.ru'
image = 'https://jooinn.com/images/big-ben-44.jpg'
upload = 'https://httpbin.org/anything'

# Загрузка информации по частям (chunk) в потоковом режиме
response = requests.get(image, stream=True)

with open('index.jpg', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        print('CHUNK!')
        f.write(response.content)

# Отправка файла на сервер
with open('index.jpg', 'rb') as f:
    requests.post(upload, data=f)
