from mesfonctions import db


def read_user():
    results = read_albums()
    print(results)
    return results


async def read_albums():
    # payload is not needed, because we take all records
    query = "Select * from albums INNER JOIN artists on artists.ArtistId = albums.Artistid"

    return await db.sql_read_query(query)


async def read_artists():
    # payload is not needed, because we take all records
    query = "Select * from artists"

    return await db.sql_read_query(query)


async def create_albums(payload):
    # We need a payload
    # to test : {"Title": "hello", "ArtistId": 2}

    values_in_json_format = await payload.json()
    query = "INSERT INTO albums(Title, ArtistId) VALUES (:Title, :ArtistId)"

    return await db.sql_write_query(query, values_in_json_format)


async def create_artist(payload):
    # We need a payload
    # to test : {"Name": "Dirken"}

    values_in_json_format = await payload.json()
    query = "INSERT INTO artists(Name) VALUES (:Name)"

    return await db.sql_write_query(query, values_in_json_format)
