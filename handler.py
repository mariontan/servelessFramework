
import sys
# sys.path.insert(0, 'vendor')
import json
from fastapi import FastAPI
from magnum import Magnum

app = FastAPI()


@app.get('/')
async def testRoute():
    return {"message": "Hello world"}


handler = Magnum(app)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    # """
