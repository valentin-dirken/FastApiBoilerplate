# For your information, this code is quite "complex".
# In your project, you don't have to edit this part.
# Contact : Valentin Dirken
# Solvay Brussels School of Economics & Management - Brussels

from databases import Database
from fastapi import FastAPI, HTTPException

database = Database("sqlite:///chinook.db")


async def sql_read_query(query):
    try:
        database.connect()
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
    database.disconnect()


async def sql_write_query(query, values_in_json_format):
    try:
        database.connect()
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
    database.disconnect()