from flask import Flask, render_template, request, redirect, session, flash, g
import sqlite3
import os

def open_db():
    if not 'db' in g:
        g.db = sqlite3.connect("blog.db")
    return g.db

'''
users = [ {"uid": 0, "name": "Mahito", "password": "Idle_Transfigure" }]

blog_posts = [
              {"pid": 0,
               "title": "Nanami",
               "content": "I can't allow this fight to go overtime."
              },
              {"pid": 1,
               "title": "Mahito",
               "content": "I'm- I'M TRULY- A CURSE!!! BLACK FLASH."
              }
             ]
'''

def index():
    return render_template("index.html")

def show_posts():
    value = request.args.get("pid")
    if value == None:
        #localhost:5000/show_posts
        db = open_db()
        post = db.execute("SELECT title, content FROM posts").fetchall()
        return render_template("show_posts.html", blog_posts=post)
    else:
        #localhost:5000/show_posts?pid=0
        #localhost:5000/show_posts?pid=1
        #...
        db = open_db()
        post = db.execute("SELECT rowid, title, content FROM posts").fetchall()
        
        for p in post:
            if p[0] == db.execute("SELECT rowid FROM posts").fetchall()[0][0]:
                main_post = db.execute("SELECT rowid, title, content FROM posts").fetchall()[p[0]-1]
                print(type(main_post))
                print(main_post)
                print("WTF")
                return render_template("post.html", blog_data=main_post)
        return render_template("show_posts.html", blog_posts=post)
        

def create_post():
    pass
    '''
    if request.method == "POST":
        db = open_db()
        post = db.execute("SELECT title, content FROM posts")
        title = request.form["title"]
        content = request.form["content"]

        
        blog_post = { "pid": rowid, "content": content, "title": title }
        blog_posts.append(blog_post)
        return redirect("/show_posts?pid=" + str(blog_post["pid"]))
    else:
        return render_template("create_post.html")
    '''

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
        
        error = "Error Idioto"
        uid = -1
        db = open_db()
        results = db.execute("SELECT rowid, username, password FROM accounts").fetchall()
        for row in results:
            if row[1] == name and row[2] == password:
                error = None
                uid = int(row[0])
        if error == None:
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
