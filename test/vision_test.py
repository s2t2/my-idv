from google.cloud.vision_v1 import ImageAnnotatorClient

from app.vision_service import vision_client

def test_vision_client():
    client = vision_client()
    assert isinstance(client, ImageAnnotatorClient)
