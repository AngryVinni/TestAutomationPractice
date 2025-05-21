import requests
import json
id = "4"
link = "https://jsonplaceholder.typicode.com/posts"
link2 = "https://api.restful-api.dev/objects"
headers = {'Content-Type': 'application/json; charset=UTF-8'}
from playwright.sync_api import Page, expect, sync_playwright
import time

enter_text_field = '//input[@class ="textinput textInput form-control"]'

def test_enter_text():
         with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("https://www.qa-practice.com/elements/input/simple")
                # You can add more actions/assertions here
                page.fill(enter_text_field, 'Hello, World!')
                # Verify the text was entered   
                expect(page.locator(enter_text_field)).to_have_value('Hello, World!')
                page.locator().click
                
body_new = json.dumps({
        "title": "newTitle",
        "body": "newestBody",
        "userId": 234
    })
body_update = json.dumps({
        "title": "update",
        "body": "updateBody",
        "userId": 98
    })
body_patch = json.dumps({
        "title": " Patch titleitle"
    })

def get_all_posts():
    ressponse = requests.get(link).json()
    for x in ressponse:
        print(x)

def get_one_post():
    ressponse = requests.get(link +"/10").json()
    print(ressponse)

def post_new_post():   
    response = requests.post(link, data=body_new, headers=headers).json()
    print(response)

def update_post():
    response = requests.put(link +"/23", data=body_update, headers=headers).json()
    print(response)

def patch_post():
    response = requests.patch(link +"/23",data=body_patch, headers=headers).json()
    print(response)


def delete_post():
    response = requests.delete(link+ "/1")
    print(response.json())
    print(response.status_code)


# get_all_posts()
# get_one_post()
# post_new_post()
# delete_post()
# update_post()
# patch_post()
# restful-api.dev

def list_of_all_objects():
    response = requests.get(link2).json()
    print(response)

def list_of_objects_by_ids():
    response = requests.get(link2 +"?id=" + id).json()
    print(response)

def add_object():
    headers = {"content-type": "application/json"}
    payload = json.dumps({ "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
    r = requests.put(link2, data=payload, headers=headers).json()
    print(r)

def put_update_object():
    headers = {"content-type": "application/json"}
    payload = json.dumps({ "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
    requestUrl = "https://api.restful-api.dev/objects/123"
    r = requests.put(requestUrl, data=payload, headers=headers)

    print(r.content)







# add_object()
put_update_object()
# list_of_objects_by_ids()
# lit_of_all_objects()