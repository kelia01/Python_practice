import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"
POSTS_URL = BASE_URL + "/posts"

# Retrieve one post ========================================================
response = requests.get(f"{POSTS_URL}/1")

print(f" Status Code: {response.status_code}")

post_data = response.json()
print(f" Post Title: {post_data['title']}")
print(f" Post Body: {post_data['body'][:50]}...")

# Retrieve all posts ========================================================
response = requests.get(POSTS_URL)
all_posts = response.json()

print(f" Retrieved {len(all_posts)} posts total")
print(f" First post title: {all_posts[0]['title']}")

# Create a new post =========================================================
new_post = {
    "title": "My API Learning Journey",
    "body": "Today I learned",
    "userId": 1
}

response = requests.post(POSTS_URL, json=new_post)
print(f" Status Code: {response.status_code}")

created_post = response.json()

# Delete a post ========================================================
response = requests.delete(f" {POSTS_URL}/1")
print(f" Status Code: {response.status_code}")
print()
