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

def local_image(img_filepath):
    with io.open(img_filepath, "rb") as img_file:
        img_contents = img_file.read()
    img = types.Image(content=img_contents)
    return img

def recognize_text(client, img_filepath):
    img = local_image(img_filepath)
    response = client.text_detection(image=img) #> <class 'google.cloud.vision_v1.types.AnnotateImageResponse'>
    texts = response.text_annotations
    text = texts[0].description
    return text

def recognize_face(client, img_filepath):
    img = local_image(img_filepath)
    response = client.face_detection(image=img) #> <class 'google.cloud.vision_v1.types.AnnotateImageResponse'>
    faces = response.face_annotations
    face = faces[0]
    return face

if __name__ == "__main__":

    names = ["matthew", "michael", "michelle", "sally"] # TODO: get all files in img dir
    print("NAMES:", names)

    name = input("Select a name (e.g. 'sally'): ")
    if name not in names:
        name = random.choice(names)
    print("NAME:", name)

    img_filepath = os.path.join(os.path.dirname(__file__), "..", "img", f"{name}.png")
    print("IMG FILE:", os.path.isfile(img_filepath), os.path.abspath(img_filepath))

    client = vision_client()

    print("----------------")
    print("TEXT RECOGNITION...")
    print("----------------")

    license_text = recognize_text(client, img_filepath)
    print(license_text)

    print("----------------")
    print("FACIAL RECOGNITION...")
    print("----------------")

    face = recognize_face(client, img_filepath)

    print("CONFIDENCE:", face.detection_confidence, face.landmarking_confidence)
    print("ANGLES:", face.roll_angle, face.pan_angle, face.tilt_angle)
    print("ASPECTS:")
    print("... UNDEREXPOSED:", face.under_exposed_likelihood)
    print("... BLURRED:", face.blurred_likelihood)
    print("... HEADWEAR:", face.headwear_likelihood)

    print("EMOTIONS:")
    print("... JOY:", face.joy_likelihood)
    print("... SORROW:", face.sorrow_likelihood)
    print("... ANGER:", face.anger_likelihood)
    print("... SURPRISE:", face.surprise_likelihood)

    print("LANDMARKS:")
    for landmark in face.landmarks:
        #print("...", landmark.type) # for some reason looks like "LEFT_EYE" but evaluates as 1, 2, 3, etc.
        print(landmark)
