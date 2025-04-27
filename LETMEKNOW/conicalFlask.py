from flask import Flask, render_template, request, redirect, session, flash, g
import os
import sqlite3

def open_db():
    if not 'db' in g:
        g.db = sqlite3.connect("blog.db")
    return g.db

'''
users = [ {"uid": 0, "name": "tim", "password": "password1" }, 
          {"uid": 1, "name": "jim", "password": "password2" }]
'''

blog_posts = [
              {"pid": 0,
               "title": "A Post About Cats",
               "content": "Cats are cool.  I like cats"
              },
              {"pid": 1,
               "title": "A Post About Dogs",
               "content": "Dogs are cool.  I like dogs"
              },
              {"pid": 2,
               "title": "A Post About Birds",
               "content": "Birds are cool.  I like birds"
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
        if session.get('uid') == None:
            flash("Log in to make a post") 
            return redirect("/login")

        title = request.form["title"]
        content = request.form["content"]
        blog_post = { "pid": len(blog_posts), "content": content, "title": title }
        blog_posts.append(blog_post)
        return redirect("/show_posts?pid=" + str(blog_post["pid"]))
    else:
        return render_template("create_post.html")

#sign page
def account():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        db = open_db()
        db.execute("INSERT INTO accounts (username, password) VALUES('" + name + "', '" + password + "')")
        db.commit()

        results = db.execute("SELECT username, password FROM accounts").fetchall()
        print(results)

        return redirect

    return render_template("account.html")

def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        
        error = "Incorrect credentials"
        uid = -1
        db = open_db()
        results = db.execute("SELECT rowid, username, password FROM accounts").fetchall()
        for row in results:
            if row[1] == name and row[2] == password:
                error = None
                uid = row[0]

        if error is None:
            session.clear()
            session['uid'] = uid
            flash(error)
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
app.config.from_mapping(SECRET_KEY='my_dev_key')

app.add_url_rule("/", "index", index)
app.add_url_rule("/show_posts", "show_posts", show_posts)
app.add_url_rule("/create_post", "create_post", create_post, methods=["GET", "POST"])
app.add_url_rule("/account", "account", account)
app.add_url_rule("/login", "login", login, methods=["GET", "POST"])
app.add_url_rule("/logout", "logout", logout, methods=["POST"])
app.run()

