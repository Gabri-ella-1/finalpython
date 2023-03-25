from flask import Flask
import databases

app = Flask(__name__)


def make_db():
    con = databases.connect()
    databases.make_tables(con)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

answer=input("Do you want to create the database? (y/n): ")
if answer == 'y':
    make_db()

if __name__ == '__main__':
    app.run()
