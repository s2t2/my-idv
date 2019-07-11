# Credits, Notes, and References

  + [Example NY Driver's Licenses - OFFICIAL](https://dmv.ny.gov/id-card/sample-photo-documents)
  + [Google Auth Credentials - From Keyfile](https://google-auth.readthedocs.io/en/latest/user-guide.html#service-account-private-key-files)
  + [Mock Google Auth Credentials](https://github.com/googleapis/google-cloud-python/blob/75277847ea68d228be4c3e91bb228236489f19f5/storage/tests/unit/url_signer_v4_test_account.json) - because for some reason any substituted values in the private key string would throw an error during test. but this one is used in the google package and it passes tests so great!

## Image Comparison

Wide search:

  + https://stackoverflow.com/questions/5730631/image-similarity-comparison
  + https://stackoverflow.com/questions/843972/image-comparison-fast-algorithm
  + http://phash.org/
  + https://github.com/Netflix/vmaf
  + https://www.ethanrosenthal.com/2016/12/05/recasketch-keras/ -- LOOKS PROMISING, BUT I WONDER IF IT IS GRANULAR ENOUGH TO DISTINGUISH BETWEEN FACES
  + https://erikbern.com/2015/09/24/nearest-neighbor-methods-vector-models-part-1.html
  + https://aws.amazon.com/rekognition/
  + https://stackoverflow.com/questions/39768788/api-to-compare-similarity-between-two-images
  + https://github.com/scikit-image/scikit-image
  + https://github.com/spotify/annoy
  + https://www.clarifai.com/custom-face-recognition
  + https://github.com/Clarifai/clarifai-python
  + http://cbonnett.github.io/Insight.html
  + https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

Following up, maybe getting somewhere with Amazon:

  + https://aws.amazon.com/rekognition/image-features/

> FACE COMPARISON ... Rekognition Image lets you measure the likelihood that faces in two images are of the same person. With Rekognition, you can use the similarity score to verify a user against a reference photo in near real time.

  + https://tutorialsdojo.com/amazon-rekognition/
  + https://docs.aws.amazon.com/rekognition/latest/dg/API_CompareFaces.html
  + https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html
  + https://aws.amazon.com/getting-started/tutorials/detect-analyze-compare-faces-rekognition/
  + https://cloudacademy.com/blog/google-vision-vs-amazon-rekognition/
  + https://us-east-2.console.aws.amazon.com/rekognition/home?region=us-east-2#/face-comparison

Yeah, definitely on to something :-D
