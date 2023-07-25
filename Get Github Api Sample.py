import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# This will not give ay particular result because it requires the username and password to be given as input.

r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
