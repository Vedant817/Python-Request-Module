import requests

r = requests.get('https://www.google.com')
print(r.text)  # Will give the source code of the page.
with open('index.html', 'w') as f:
    f.write(r.text)
