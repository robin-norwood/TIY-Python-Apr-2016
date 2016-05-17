# Via the URL path
# /students/5 ## Specifying a "resource"

# BAD Example:
# /students/search/name/bob # Terrible!
#{ 'name': 'bob',#  'id': 5}

# Via URL parameters (arguments)
# /students/search?name=bob
# key/value arguments define behavior
# /students/search?q=

# /students/5?all_scores=yes
# GET /students?limit=50&offset=100
# students[100:151]

# PUT or POST data (json or xml, or csv, or 'whatever')

# POST form data (form encoding)
