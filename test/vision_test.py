import os

from google.cloud.vision_v1 import ImageAnnotatorClient

from app.vision_service import vision_client

def test_vision_client():
    example_creds_filepath = os.path.join(os.path.dirname(__file__), "..", "auth", "mock_creds.json")
    client = vision_client(example_creds_filepath)
    assert isinstance(client, ImageAnnotatorClient)
