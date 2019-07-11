# My Identity Verification Service

My Proof of Concept IDV Service.

## Setup

### Installation

Install from source:

```sh
git clone git@github.com:s2t2/my-idv.git
cd my-idv/
```

### Creds

[Get credentials](https://console.cloud.google.com/apis/credentials) for a project with access to the Google Cloud Vision API. Store the credentials in "auth/credentials.json".

### Env

```sh
conda create -n idv-env python=3.7 # (first time only)
conda activate idv-env
```

### Packages

```sh
pip install -r requirements.txt # # (first time only)
```

## Usage

Recognize text from a driver's license photo (see "img" directory):

```sh
python app/vision_service.py
```
