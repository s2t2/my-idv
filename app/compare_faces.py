
# adapted from: https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html

import os
from pprint import pprint

import boto3

if __name__ == "__main__":

    AWS_REGION = os.getenv("AWS_REGION", default="us-east-1")
    client = boto3.client("rekognition", region_name=AWS_REGION)

    license_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "sally.png")
    licence_file = open(license_filepath, "rb")
    license_contents = licence_file.read()
    licence_file.close()

    selfie_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "sally.png")
    selfie_file = open(selfie_filepath, "rb")
    selfie_contents = selfie_file.read()
    selfie_file.close()

    response=client.compare_faces(
        SimilarityThreshold = 70,
        SourceImage = {"Bytes": license_contents},
        TargetImage = {"Bytes": selfie_contents}
    )

    #print(type(response))
    #pprint(response)
    matches = response["FaceMatches"]
    if matches:
        #print("FACE MATCHES!")
        for match in matches:
            bbox = match["Face"]["BoundingBox"]
            similarity = str(match["Similarity"])
            print(f"FACE MATCH {bbox['Left']} {bbox['Top']} ({similarity}% CONFIDENCE)")

    else:
        #print("NO MATCHES")
        nonmatches = response["UnmatchedFaces"]
        for nonmatch in nonmatches:
            #print(nonmatch)
            bbox = nonmatch["BoundingBox"]
            confidence = str(nonmatch["Confidence"])
            print(f"NO MATCH {bbox['Left']} {bbox['Top']} ({confidence}% confidence)")




#>{
#>    "matches": [{
#>        "Face": {
#>            "BoundingBox": {
#>                "Width": 0.5521978139877319,
#>                "Top": 0.1203877404332161,
#>                "Left": 0.23626373708248138,
#>                "Height": 0.3126954436302185
#>            },
#>            "Confidence": 99.98751068115234,
#>            "Pose": {
#>                "Yaw": -82.36799621582031,
#>                "Roll": -62.13221740722656,
#>                "Pitch": 0.8652129173278809
#>            },
#>            "Quality": {
#>                "Sharpness": 99.99880981445312,
#>                "Brightness": 54.49755096435547
#>            },
#>            "Landmarks": [{
#>                    "Y": 0.2996366024017334,
#>                    "X": 0.41685718297958374,
#>                    "Type": "eyeLeft"
#>                },
#>                {
#>                    "Y": 0.2658946216106415,
#>                    "X": 0.4414493441581726,
#>                    "Type": "eyeRight"
#>                },
#>                {
#>                    "Y": 0.3465650677680969,
#>                    "X": 0.48636093735694885,
#>                    "Type": "nose"
#>                },
#>                {
#>                    "Y": 0.30935320258140564,
#>                    "X": 0.6251809000968933,
#>                    "Type": "mouthLeft"
#>                },
#>                {
#>                    "Y": 0.26942989230155945,
#>                    "X": 0.6454493403434753,
#>                    "Type": "mouthRight"
#>                }
#>            ]
#>        },
#>        "Similarity": 100.0
#>    }]
#>
