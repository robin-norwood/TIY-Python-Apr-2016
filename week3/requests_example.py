import requests
events = requests.get('https://api.github.com/events')
type(events)
requests.models.Response?
events
events.status_code
events.headers
events.headers['ETag']
events.text
type(events.text)
type(events.text)
events.text[0:100]
import json
ev = json.dumps(events.text)
type(ev)
ev = json.loads(events.text)
type(ev)
ev[0]
ev[0].keys()
ev[0]['actor']
ev[0]['actor']['url']
from PIL import Image
from io import BytesIO
avatar = requests.get(ev[0]['actor']['avatar_url'])
avatar.status_code
img = Image.open(BytesIO(avatar.content))
img.show()
type(img)
img.show()
