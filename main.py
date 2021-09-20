from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

all_post = requests.get("https://api.npoint.io/fabd37754ba9e2aa994c").json()
print(all_post)
post_object = []
for post in all_post:
    post_obj = Post(post["id"], post['title'], post["subtitle"], post["body"])
    post_object.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_object)


@app.route("/blog/<int:index>")
def blog(index):
    requested_post = None
    for blog_post in post_object:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post = requested_post)


if __name__ == "__main__":
    app.run(debug=True)
