import io
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# create a 'static files' directory
# create a '/static' prefix for all files
# serve files from the 'media/' directory under the '/static/' route
#   /Big_Buck_Bunny_1080p.avi becomes '/static/Big_Buck_Bunny_1080p.avi'
# name='static' is used internally by FastAPI
app.mount("/static", StaticFiles(directory="media"), name="static")


@app.get("/")
async def main():
    # open the movie file to stream it
    movie = open("media/Big_Buck_Bunny_1080p.avi", "rb")
    # return a stream response with the movie and a MIME type of 'video/avi'
    return StreamingResponse(movie, media_type="video/avi")
