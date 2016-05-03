import requests
post = requests.get('http://jsonplaceholder.typicode.com/posts/1')
type(post)
post.json
post.json()
pdata = post.json()
type(pdata)
pdata.keys()
pdata['body']
pdata['title']
