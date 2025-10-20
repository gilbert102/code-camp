import requests

# Fetch all posts and comments in just 2 API calls
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()

# Group comments by post ID
comments_by_post = {}
for comment in comments:
    post_id = comment['postId']
    if post_id not in comments_by_post:
        comments_by_post[post_id] = []
    comments_by_post[post_id].append(comment)

# Display each post with its comments
for post in posts:
    post_id = post['id']
    print(f"Title: {post['title']} ({post_id})")
    print(post['body'])
    
    if post_id in comments_by_post:
        print("\nComments:")
        for comment in comments_by_post[post_id]:
            print(f"- {comment['name']} ({comment['email']}): {comment['body']}")
    
    print("\n" + "-"*100 + "\n")
