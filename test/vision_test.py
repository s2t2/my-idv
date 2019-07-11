import os

from google.cloud.vision_v1 import ImageAnnotatorClient, types
from google.cloud.vision_v1.types import AnnotateImageResponse

from app.vision_service import vision_client, recognize_text

def test_vision_client():
    mock_creds_filepath = os.path.join(os.path.dirname(__file__), "..", "auth", "mock_creds.json")
    mock_client = vision_client(mock_creds_filepath)
    assert isinstance(mock_client, ImageAnnotatorClient)
    assert "text_detection" in dir(mock_client)

@pytest.mark.skipif(CI, reason="requires real credentials, which aren't on the CI server"
def test_text_recognition():
    client = vision_client()
    image_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "sally.png")
    response = recognize_text(client, image_filepath)
    assert isinstance(response, AnnotateImageResponse)
    assert response.locale == "en"
    assert response.text_annotations[0].description == "NEW YORK STATE\nCommission\nof Motor Vehicles\nDRIVER LICENSE\nID: 000 000 000\nCLASS DM\nSAMPLE,SALLY\n1010 ANYPLACE ST\nYOURCITY NY 12121\nDOB: 07-18-83\nSEX: F EYES: BL HT: 5-09\nE: NONE\nR: NONE\nISSUED: 07-18-05 EXPIRES: 07-18-13\nSety Somple\nCELSIOR\n83145522\n"
