import os
from nineapi.client import Client, APIException
from nineapi.client import Post, APIException
from nineapi.client import Group, APIException

client = Client()
client.username = os.environ['NINEGAG_USERNAME']
client.password = os.environ['NINEGAG_PASSWORD']

group = int(os.environ.get('TARGET_GROUP', 1))
type = os.environ.get('TARGET_TYPE', 'hot')
count = int(os.environ.get('TARGET_COUNT', 10))

try:
    client.log_in(client.username, client.password)
except APIException as e:
    print('Failed to log in:', e)
else:
    posts = client.get_posts(group,type,count,['animated','video'], None)
    client.write_posts_to_json(posts)
