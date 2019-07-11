import io # necessary?
import os
from pprint import pprint

#from dotenv import load_dotenv
from google.cloud import vision
from google.cloud.vision import types

#from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account

#load_dotenv() # load implicit creds GOOGLE_APPLICATION_CREDENTIALS

if __name__ == "__main__":
    CREDS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "credentials.json")
    print("CREDS FILE:", os.path.isfile(CREDS_FILEPATH), os.path.abspath(CREDS_FILEPATH))

    #client = vision.ImageAnnotatorClient()

    #creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILEPATH)
    creds = service_account.Credentials.from_service_account_file(CREDS_FILEPATH)
    print("CREDS", type(creds))
    client = vision.ImageAnnotatorClient(credentials=creds)

    print("VISION CLIENT:", type(client))
    pprint(dir(client))
    print("------------")

    img_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "sally.png")
    print("IMG FILE:", os.path.isfile(img_filepath), os.path.abspath(img_filepath))

    with io.open(img_filepath, "rb") as image_file:
        content = image_file.read()
    img = types.Image(content=content) #> <class 'google.cloud.vision_v1.types.Image'>
    print("IMG", type(img))

    response = client.text_detection(image=img) #> <class 'google.cloud.vision_v1.types.AnnotateImageResponse'>
    print("RESPONSE", type(response))
    pprint(dir(response))
    print("------------")

    #breakpoint()

    texts = response.text_annotations
    #for text in texts:
    #    print(type(text))
    #    print(text.description)
    #    #print("------------------")

    text = texts[0]
    print(type(text)) #> <class 'google.cloud.vision_v1.types.EntityAnnotation'>
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
