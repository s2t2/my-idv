import io # necessary?
import os
from pprint import pprint
import random

#from dotenv import load_dotenv
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud.vision import types

#load_dotenv() # load implicit creds GOOGLE_APPLICATION_CREDENTIALS

CREDS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "credentials.json")

def vision_client(creds_filepath=CREDS_FILEPATH):
    #print("CREDS FILE:", os.path.isfile(creds_filepath), os.path.abspath(creds_filepath))

    creds = service_account.Credentials.from_service_account_file(CREDS_FILEPATH)
    #print("CREDS", type(creds))

    client = vision.ImageAnnotatorClient(credentials=creds)
    #print("VISION CLIENT:", type(client))
    #pprint(dir(client))
    #print("------------")

    return client

if __name__ == "__main__":

    names = ["matthew", "michael", "michelle", "sally"] # TODO: get all files in img dir
    print("NAMES:", names)

    name = input("Select a name (e.g. 'sally'): ")
    if name not in names:
        name = random.choice(names)
    print("NAME:", name)

    img_filepath = os.path.join(os.path.dirname(__file__), "..", "img", f"{name}.png")
    print("IMG FILE:", os.path.isfile(img_filepath), os.path.abspath(img_filepath))

    with io.open(img_filepath, "rb") as image_file:
        content = image_file.read()
    img = types.Image(content=content) #> <class 'google.cloud.vision_v1.types.Image'>
    #print("IMG:", type(img))

    client = vision_client()
    response = client.text_detection(image=img) #> <class 'google.cloud.vision_v1.types.AnnotateImageResponse'>
    #print("RESPONSE", type(response))
    #pprint(dir(response))
    print("------------")

    #breakpoint()

    texts = response.text_annotations
    #for text in texts:
    #    print(type(text))
    #    print(text.description)
    #    #print("------------------")

    text = texts[0]
    #print(type(text)) #> <class 'google.cloud.vision_v1.types.EntityAnnotation'>
    print(text.description)
    #> NEW YORK STATE
    #> Commission
    #> of Motor Vehicles
    #> DRIVER LICENSE
    #> ID: 000 000 000
    #> CLASS DM
    #> SAMPLE,SALLY
    #> 1010 ANYPLACE ST
    #> YOURCITY NY 12121
    #> DOB: 07-18-83
    #> SEX: F EYES: BL HT: 5-09
    #> E: NONE
    #> R: NONE
    #> ISSUED: 07-18-05 EXPIRES: 07-18-13
    #> Sety Somple
    #> CELSIOR
    #> 83145522
