import sqlite3

db = sqlite3.connect("skibs.db")
db.execute("DROP TABLE IF EXISTS posts")
db.execute("CREATE TABLE posts(author_id INTEGER, title TEXT, content TEXT, tags TEXT, likes INTEGER)")

db.execute("INSERT INTO posts (author_id, title, content, tags, likes) VALUES ('1', 'Brainrot', 'Dop Dop Yes Yes', 'Dumah', 10000), ('1', 'Brainrot', 'Dop Dop Yes Yes', 'Dumah', 10000)")
db.execute("INSERT INTO posts (author_id, title, content, tags, likes) VALUES ('2', 'Australian', 'Brainrot', 'AutCreatures', 20000), ('3', 'MadnessGrunt1000', 'Noob', 'AnimeGuy', 30000)")

result = db.execute("SELECT rowid, title, author_id, content, tags, likes FROM posts").fetchall()
print(result)

result = db.execute("SELECT title, likes FROM posts WHERE likes <= 10000").fetchall()
print(result)

result = db.execute("SELECT sum(likes), avg(likes), count(likes) FROM posts").fetchall()
print(result)


db.execute("CREATE TABLE accounts(first TEXT, last TEXT, age INTEGER)")
db.execute('''INSERT INTO accounts (first, last, age) VALUES 
           ('a','A', 1), 
           ('b','B', 2), 
           ('c', 'C', 3),
           ('d', 'D', 4),
           ('e', 'E', 7)''')

#result = db.execute("SELECT first, title, content FROM accounts JOIN posts ON author_id = accounts.rowid").fetchall()
#print(result)
result = db.execute("SELECT count(author_id) FROM accounts JOIN posts ON author_id = accounts.rowid WHERE author_id = 1").fetchall()
print(result)
"""
result = db.execute("SELECT avg(postcount) FROM accounts").fetchall()
print(result)
res2 = db.execute("SELECT sum(postcount) FROM accounts").fetchall()
print(res2)
res3 = db.execute("SELECT max(age) FROM accounts").fetchall()
print(res3)
res4 = db.execute("SELECT min(age) FROM accounts").fetchall()
print(res4)"""

db.execute("CREATE TABLE comments(author_id INTEGER, content TEXT, likes INTEGER)")
db.execute('''INSERT INTO comments(author_id, content, likes) VALUES 
            (1, 'Hieroplant Green', 69),
            (2, 'Silver Chariot', 69420),
            (3, 'STAR PLATINUM! ORA', 696969),
            (4, 'Hermit Purple', -1),
            (5, 'Magician RED', 1) ''')

result = db.execute("SELECT first, content FROM comments JOIN accounts ON author_id = accounts.rowid").fetchall()
print(result)
