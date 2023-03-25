import sqlite3

NEW_MOVIE = "INSERT INTO MovieData(MovieUrl, MovieID) VALUES (?,?);"
NEW_USER ="INSERT INTO UserInfo(Name, Password, UserID, Preferences, Contact) VALUES (?,?,?,?,?);"
NEW_MATCH ="INSERT INTO Matches(UserID_One, UserID_Two, MovieID) VALUES (?,?,?);"

def connect():
    return sqlite3.connect("TinMovie.db")


def make_tables(con):
    with con:
        con.execute(
            "CREATE TABLE MovieData( MovieUrl TEXT, MovieID INTEGER, PRIMARY KEY(MovieID));"
        )
        con.execute(
            "CREATE TABLE UserInfo(Name TEXT, Password TEXT, UserID INTEGER PRIMARY KEY, Preferences TEXT, Contact TEXT);"
        )
        con.execute(
            "CREATE TABLE Matches(UserID_One INTEGER, UserID_Two INTEGER, MovieID INTEGER, Agree BOOLEAN, FOREIGN KEY(MovieID) REFERENCES MovieData(MovieID));"
        )


def add_movie(con, url, movie_id):
    with con:
        con.execute(NEW_MOVIE, (url, movie_id))

def add_user(con, name, password, user_id, preferences, contact):
    with con:
        con.execute(NEW_USER, (name, password, user_id, preferences, contact))

def add_match(con, user_one, user_two, movie_id):
    with con:
        con.execute(NEW_MATCH, (user_one, user_two, movie_id))

