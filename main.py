import requests
import json

link = "https://jsonplaceholder.typicode.com/posts"

def get_all_posts():
    ressponse = requests.get(link).json()
    for x in ressponse:
        print(x)

def get_one_post():
    ressponse = requests.get(link +"/100").json()
    print(ressponse)

def post_new_post():
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    body = json.dumps({
        "title": "newTitle",
        "body": "newestBody",
        "userId": 234
    })
    response = requests.post(link, data=body, headers=headers).json()
    print(response)



# get_all_posts()
# get_one_post()
post_new_post()
get_one_post() 