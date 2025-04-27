import sqlite3

db = sqlite3.connect("blog.db")


db.execute("DROP TABLE IF EXISTS posts")
db.execute("DROP TABLE IF EXISTS accounts")
db.execute("CREATE TABLE accounts (username TEXT, password TEXT)")

db.execute('''INSERT INTO accounts(username, password) VALUES 
           ('Khang', 'Gae')
           ''')


db.execute("CREATE TABLE posts (accountid INTEGER, title TEXT, content TEXT)")
db.execute('''INSERT INTO posts (accountid, title, content) VALUES
           (1, 'A monkey in the zoo', 'His name is khang'),
           (2, 'A koala in the jungle', 'His name is Australian Monkey: Nam'),
           (3, 'Another monkey in the zoo', 'His name is Ken')''')

db.commit()
db.close()
