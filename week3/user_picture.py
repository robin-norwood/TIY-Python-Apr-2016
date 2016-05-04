import requests
from PIL import Image
from io import BytesIO

# Open a user's photo

base_url =  'http://jsonplaceholder.typicode.com'

photo_url = base_url + "/photos/1"
resp = requests.get(photo_url)
resp.status_code
photo = resp.json()
print(photo)

photo_image = requests.get(photo['url'])
img = Image.open(BytesIO(photo_image.content))

img.show()

# import requests
# from PIL import Image
# from io import BytesIO
#
# events = requests.get('https://api.github.com/events')
# avatar = requests.get(events.json()[0]['actor']['avatar_url'])
# img = Image.open(BytesIO(avatar.content))
#
# img.show()
