from flask import Flask, render_template, request
import databases
import random
from databases import *
import sqlite3 as sql
import json

app = Flask(__name__)


def make_db():
    con = databases.connect()
    databases.make_tables(con)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('login.html')

@app.route('/NewUser')
def NewUser():  # put application's code here
    return render_template('NewUser.html')


@app.route('/NewMovie')
def NewMovie():  # put application's code here
    return render_template('MoviePage.html')

@app.route('/Profile')
def Profile():  # put application's code here
    return render_template('Profile.html')

@app.route('/newlog', methods =['POST', 'GET'])
def newlog():
    if request.method == 'POST':
            name = request.form['Name']
            passw = request.form['Password']
    return render_template('Profile.html')

@app.route('/adduser', methods =['POST', 'GET'])
def adduser():
    if request.method == 'POST':
            name = request.form['Name']
            passw = request.form['Password']
            pref= request.form['Preferences']
            cont = request.form['Contact']
            Idnum = random.randint(1,300)

            with sql.connect("TinMovie.db") as con:
                add_user(con, name, passw, Idnum, pref, cont)
            return render_template('Profile.html')




answer=input("Do you want to create the database? (y/n): ")
if answer == 'y':
    make_db()

if __name__ == '__main__':
    app.run()
