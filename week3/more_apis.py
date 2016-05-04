import requests
base_url =  'http://jsonplaceholder.typicode.com'

#requests.get(base_url + "/posts/1").json()

# Print all of the unique email addresses for comments for posts 12-30

comments_for_post_url = base_url + '/posts/{0}/comments'
emails = []

for postId in range(12, 31):
    resp = requests.get(comments_for_post_url.format(postId))

    if resp.status_code in [200, 201]:
        for c in resp.json():
            if c['email'] not in emails:
                emails.append(c['email'])
    else:
        print("ERROR: {} got {}".format(comments_for_post_url, resp.status_code))

#emails = list(set(emails))

print("EMAILS: " + str(emails))
