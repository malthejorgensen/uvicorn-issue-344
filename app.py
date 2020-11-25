import urllib

from quart import json, Quart, redirect, request

app = Quart(__name__)

@app.route('/')
async def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
