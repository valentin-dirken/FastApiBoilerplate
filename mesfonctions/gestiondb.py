from fastapi import FastAPI, HTTPException
from mesfonctions import db
database = db.db_connect()


def read_user():
    results = read_albums()
    print(results)
    return results


async def read_albums():
    # payload is not needed, because we take all records
    query = "Select * from albums INNER JOIN artists on artists.ArtistId = albums.Artistid"

    try:
        results = await database.fetch_all(query=query)
        return HTTPException(
            status_code=200,
            detail=results
        )
    # if we have a problem in the database.fetchall(), a 404 Error will be raised
    except Exception as e:
        return HTTPException(
            status_code=404,
            detail=str(e)
        )


async def read_artists():
    # payload is not needed, because we take all records
    query = "Select * from artists"

    try:
        results = await database.fetch_all(query=query)
        return HTTPException(
            status_code=200,
            detail=results
        )
    # if we have a problem in the database.fetchall(), a 404 Error will be raised
    except Exception as e:
        return HTTPException(
            status_code=404,
            detail=str(e)
        )


async def create_albums(payload):
    # We need a payload
    # to test : {"Title": "hello", "ArtistId": 2}

    values_in_json_format = await payload.json()
    query = "INSERT INTO albums(Title, ArtistId) VALUES (:Title, :ArtistId)"

    try:
        await database.execute(
            query=query,
            values=values_in_json_format
        )
        # Success if  database.execute() is correctly executed.
        return HTTPException(
            status_code=200,
            detail=values_in_json_format
        )

    # if we have a problem in the database.execute(), a 404 Error will be raised
    except Exception as e:
        return HTTPException(
            status_code=404,
            detail=str(e)
        )


async def create_artist(payload):
    # We need a payload
    # to test : {"Name": "VALOU"}

    values_in_json_format = await payload.json()
    query = "INSERT INTO artists(Name) VALUES (:Name)"

    # Start - Don't Touch
    try:
        await database.execute(
            query=query,
            values=values_in_json_format
        )
        # Success if  database.execute() is correctly executed.
        return HTTPException(
            status_code=200,
            detail=values_in_json_format
        )

    # if we have a problem in the database.execute(), a 404 Error will be raised
    except Exception as e:
        return HTTPException(
            status_code=404,
            detail=str(e)
        )
    # END - Don't Touch
