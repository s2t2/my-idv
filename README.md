# My Identity Verification Service

[![Build Status](https://travis-ci.com/s2t2/my-idv.svg?token=J3sGjFcxTXFQzbQJjiqb&branch=master)](https://travis-ci.com/s2t2/my-idv)

A proof of concept Identity Verification (IDV) Service.

Example Photo:

![](img/sally.png)

Example Output:

    NEW YORK STATE
    Commission
    of Motor Vehicles
    DRIVER LICENSE
    ID: 000 000 000
    CLASS DM
    SAMPLE,SALLY
    1010 ANYPLACE ST
    YOURCITY NY 12121
    DOB: 07-18-83
    SEX: F EYES: BL HT: 5-09
    E: NONE
    R: NONE
    ISSUED: 07-18-05 EXPIRES: 07-18-13
    Sety Somple
    CELSIOR
    83145522

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

## Testing

```sh
pip install pytest # (first time only)
```

Run tests:

```sh
pytest
```
