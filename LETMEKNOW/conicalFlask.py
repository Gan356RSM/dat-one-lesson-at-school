from flask import Flask, render_template, request, redirect, session, flash
import os

users = [ {"uid": 0, "name": "Mahito", "password": "Idle_Transfigure" }]

blog_posts = [
              {"pid": 0,
               "title": "Nanami",
               "content": "I can't allow this fight to go overtime."
              },
              {"pid": 1,
               "title": "Mahito",
               "content": "I'm~ I'M TRULY- A CURSE!!! BLACK FLASH."
              }
             ]

def index():
    return render_template("index.html")

def show_posts():
    value = request.args.get("pid")
    if value == None:
        #localhost:5000/show_posts
        return render_template("show_posts.html", blog_posts=blog_posts)
    else:
        #localhost:5000/show_posts?pid=0
        #localhost:5000/show_posts?pid=1
        #...
        pid = int(value)
        for p in blog_posts:
            if p["pid"] == pid:
                return render_template("post.html", blog_data=p)

        return render_template("show_posts.html", blog_posts=blog_posts)

def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        blog_post = { "pid": len(blog_posts), "content": content, "title": title }
        blog_posts.append(blog_post)
        return redirect("/show_posts?pid=" + str(blog_post["pid"]))
    else:
        return render_template("create_post.html")

def account():
    return render_template("account.html")

def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        error = "Error Idioto"
        uid = -1
        for user in users:
            if user["name"] == name and user["password"] == password:
                error = None
                uid = user["uid"]
        if error is None:
            session.clear()
            session["uid"] = str(uid)
            return redirect("/")
        else:
            flash(error)
            return render_template("login.html")
    else:
        return render_template("login.html")

def logout():
    session.clear()
    return redirect("/")

app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())
app.config.from_mapping(SECRET_KEY="my_dev_key")

app.add_url_rule("/", "index", index)
app.add_url_rule("/show_posts", "show_posts", show_posts)
app.add_url_rule("/create_post", "create_post", create_post, methods=["GET", "POST"])
app.add_url_rule("/account", "account", account)
app.add_url_rule("/login", "login", login, methods=["GET","POST"])
app.add_url_rule("/logout", "logout", logout, methods=["POST"])

app.run()
