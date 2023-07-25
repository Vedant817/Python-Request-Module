import requests
from PIL import Image
from io import BytesIO

r = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFx1pD-5y61mO3S-e1grpCuf24c6zMIGanYrbzcIwB&s')
i = Image.open(BytesIO(r.content))
fp = open('img.jpg', 'wb')
i.save(fp)
fp.close()
