import json
import asyncio

from fastapi import FastAPI, WebSocket


"""
Code from:
https://stribny.name/blog/2020/07/real-time-data-streaming-using-fastapi-and-websockets

If you get the error message: "Unsupported upgrade request"
    you probably need to install Uvicorn with websocket support:
        pip3 install uvicorn[standard]
            or
        pip3 install websockets

This script opens the measurements.json file and saves it's contents
    to a variable (measurements). When a client connects to the websocket
    route (/ws) the contents of the measurements variable are sent to the
    client with a 0.1 second delay between values.

Basically, this script reads a file and sends each item in the file over
    a websocket connection to a client.
"""


api = FastAPI()

# open the measurements.json file and save it's contents
#   in a variable named 'measurements'
with open("measurements.json", "r") as file:
    measurements = iter(json.loads(file.read()))


# create the websocket ('ws') endpoint, asynchronously
@api.websocket("/ws")
# Define a variable called 'websocket' of type 'WebSocket' (type hinting)
async def websocket_endpoint(websocket: WebSocket):
    # asynchronously accept new connections
    await websocket.accept()
    try:
        while True:
            """
            iterate through the 'measurements' list and send each
                JSON entry ( websocket.send_json(data_to_send) )
                over the websocket connection
            """
            await asyncio.sleep(0.1)
            # set the 'payload' variable to the next item in
            #   the 'measurements' list
            payload = next(measurements)
            await websocket.send_json(payload)
    # catch the 'StopIteration' exception that will be thrown when the
    #   'payload = next(measurements)' line hits the end of the
    #   'measurements' list (duh, there's no "next" item) and then send
    #   a message to the client telling them there's no more data, then
    #   close the websocket connection.
    except StopIteration:
        await websocket.send_json("End of data")
        print("Closing connection...")
        await websocket.close()
