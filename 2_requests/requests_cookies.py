import requests

url = 'https://httpbin.org/cookies'

test_cookies = {
    'cookie1': 'value1',
    'cookie2': 'value2',
}

# Если в запросе есть cookies, их можно получить по ключу response.cookies['cookie_name']:
response = requests.get(url)

# Отправить собственные cookies на сервер, используется параметр cookies:
response = requests.get(url, cookies=test_cookies)
print(response.text)

# Cookies возвращаются в RequestsCookieJar, который работает как dict
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
response = requests.get(url, cookies=jar)
print(response.text)
