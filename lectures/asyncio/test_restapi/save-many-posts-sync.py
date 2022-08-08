import json
import requests


def save_post(post_info):
    print("saving...")
    print("post_id " +str(post_info['id']))
    file = open('posts-sync/post-' + str(post_info['id']) + ".json", 'w')
    file.write(json.dumps(post_info))
    file.close()
    print('EndSaving')


file = open('posts.json', 'r')
posts = json.loads(file.read())
file.close()
for post in posts:
    info = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(post['id'])).json()
    save_post(info)
