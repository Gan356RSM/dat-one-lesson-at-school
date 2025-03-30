import sqlite3

db = sqlite3.connect("skibs.db")
db.execute("DROP TABLE IF EXISTS posts")
db.execute("CREATE TABLE posts(author TEXT, title TEXT, content TEXT, tags TEXT, likes INTEGER)")

db.execute("INSERT INTO posts (author, title, content, tags, likes) VALUES ('Khang', 'Brainrot', 'Dop Dop Yes Yes', 'Dumah', 10000)")
db.execute("INSERT INTO posts (author, title, content, tags, likes) VALUES ('Koala', 'Australian', 'Brainrot', 'AutCreatures', 20000), ('Ken', 'MadnessGrunt1000', 'Noob', 'AnimeGuy', 30000)")

result = db.execute("SELECT rowid, title, author, content, tags, likes FROM posts").fetchall()
print(result)

result = db.execute("SELECT title, likes FROM posts WHERE likes <= 10000").fetchall()
print(result)

result = db.execute("SELECT sum(likes), avg(likes), count(likes) FROM posts").fetchall()
print(result)

db.execute("CREATE TABLE accounts(first TEXT, last TEXT, age INTEGER, postcount INTEGER)")
db.execute('''INSERT INTO accounts (first, last, age, postcount) VALUES 
           ('a','A', 1, 1), 
           ('b','B', 2, 2), 
           ('c', 'C', 3, 3),
           ('d', 'D', 4, 4),
           ('e', 'E', 7, 7)''')

result = db.execute("SELECT avg(postcount) FROM accounts").fetchall()
print(result)
res2 = db.execute("SELECT sum(postcount) FROM accounts").fetchall()
print(res2)
res3 = db.execute("SELECT max(age) FROM accounts").fetchall()
print(res3)
res4 = db.execute("SELECT min(age) FROM accounts").fetchall()
print(res4)