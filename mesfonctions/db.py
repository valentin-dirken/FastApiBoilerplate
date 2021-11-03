from databases import Database


def db_connect():
    database = Database("sqlite:///chinook.db")
    return database
