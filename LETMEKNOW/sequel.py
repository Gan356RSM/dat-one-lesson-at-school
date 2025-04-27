import sqlite3

db = sqlite3.connect("blog.db")

db.execute("DROP TABLE IF EXISTS accounts")
db.execute("CREATE TABLE accounts (username TEXT, password TEXT)")

db.execute("INSERT INTO accounts (username, password) VALUES ('khang', 'idiot')")

#add blog_posts table

db.commit()
db.close()
