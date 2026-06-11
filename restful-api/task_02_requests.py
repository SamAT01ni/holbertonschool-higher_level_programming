#!/usr/bin/python3

import requests
import csv
import json


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        jsondata = r.json()
        for post in jsondata:
            print(post)


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = []
    if r.status_code == 200:
        jsondata = r.json()
        data = [
            {
                "id": post["id"], "title": post["title"],
                "body": post["body"]
            } for post in jsondata]
    with open("posts.csv", "w", encoding="utf-8") as cf:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
