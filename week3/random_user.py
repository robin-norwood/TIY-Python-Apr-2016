import requests
import random

base_url =  'http://jsonplaceholder.typicode.com'

# Print the email address, phone number, latitude, and longitude for a random user.

users_url = base_url + '/users'
resp = requests.get(users_url)
template = "EMAIL: {email}, PHONE: {phone}, LAT: {lat}, LONG: {lng}"

if resp.status_code in [200, 201]:
    users = resp.json() # FIXME: Could we just get a user instead?
    rand_user = random.choice(users)
    user_data = {'email': rand_user['email'],
                 'phone': rand_user['phone'],
                 'lat': rand_user['address']['geo']['lat'],
                 'lng': rand_user['address']['geo']['lng']}
    print(template.format(**user_data))
    print("EMAIL: " + rand_user['email'])
    print("PHONE: " + rand_user['phone'])
    print("LAT: " + rand_user['address']['geo']['lat'])
    print("LONG: " + rand_user['address']['geo']['lng'])
else:
    print("ERROR: {}".format(resp.status_code) )
