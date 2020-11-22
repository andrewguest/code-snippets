# import the FastAPI test client
from fastapi.testclient import TestClient

# import the 'api' variable from the api.py file
from api import api


def test_websocket():
    # instantiate the TestClient using our 'api' FastAPI instance
    test_client = TestClient(api)
    # connect to the websocket route from the api.py file
    with test_client.websocket_connect("/ws") as websocket:
        # receive JSON data (because that's what our websocket route sends)
        data = websocket.receive_json()
        # assert that we should receive a 'dict' type (JSON is dict in Python)
        assert type(data) == dict
        # for each key/value pair that we receive as a response, assert that
        #   each 'key' should be a string and each 'value' should be an int type
        for key, value in data.items():
            assert type(key) == str
            assert type(value) == int
