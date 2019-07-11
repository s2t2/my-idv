import io # necessary?
import os
from pprint import pprint
import random

from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types

CREDS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "credentials.json")

def vision_client(creds_filepath=CREDS_FILEPATH):
    #print("CREDS FILE:", os.path.isfile(creds_filepath), os.path.abspath(creds_filepath))
    creds = service_account.Credentials.from_service_account_file(creds_filepath)
    #print("CREDS", type(creds))
    client = vision.ImageAnnotatorClient(credentials=creds)
    #print("VISION CLIENT:", type(client))
    return client

def recognize_text(client, img_filepath):
    with io.open(img_filepath, "rb") as img_file:
        img_contents = img_file.read()
    img = types.Image(content=img_contents) #> <class 'google.cloud.vision_v1.types.Image'>
    response = client.text_detection(image=img) #> <class 'google.cloud.vision_v1.types.AnnotateImageResponse'>
    #return response
    texts = response.text_annotations
    text = texts[0].description
    return text

if __name__ == "__main__":

    client = vision_client()

    names = ["matthew", "michael", "michelle", "sally"] # TODO: get all files in img dir
    print("NAMES:", names)
    name = input("Select a name (e.g. 'sally'): ")
    if name not in names:
        name = random.choice(names)
    print("NAME:", name)

    img_filepath = os.path.join(os.path.dirname(__file__), "..", "img", f"{name}.png")
    print("IMG FILE:", os.path.isfile(img_filepath), os.path.abspath(img_filepath))

    response_text = recognize_text(client, img_filepath)
    print(response_text)
