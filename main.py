# Start - Don't touch
from fastapi import FastAPI
from mesfonctions import gestiondb
from starlette.requests import Request
from mesfonctions import db
database = db.db_connect()
app = FastAPI()
@app.on_event("startup")
async def database_connect():
    await database.connect()
@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

# End - Don't touch


# Router
@app.get("/")
def root():
    return {"message": "It works !"}


# GET - ALBUMS
@app.get("/albums")
async def read_albums_router():
    results = await gestiondb.read_albums()
    return results


# POST - ALBUMS
@app.post("/albums")
async def create_albums_router(payload: Request):
    # The payload contains data to be inserted in the table.
    results = await gestiondb.create_albums(payload)
    return results


# POST - ARTISTS
@app.post("/artists")
async def create_artists_router(payload: Request):
    # The payload contains data to be inserted in the table.
    results = await gestiondb.create_artist(payload)
    return results


# GET - artists
@app.get("/artists")
async def read_artists_router():
    results = await gestiondb.read_artists()
    return results


# TODO  $ pip install -r requirements.txt

# TODO OK ! create a record with the POST & Body.
# TODO read an element
# TODO OK !  test si bien enregistré dans la DB ...
# TODO Database import correctement
#uvicorn.run(app, host="0.0.0.0", port=8000)
