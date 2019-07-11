# Credits, Notes, and References

  + [Example NY Driver's Licenses - OFFICIAL](https://dmv.ny.gov/id-card/sample-photo-documents)
  + [Google Auth Credentials - From Keyfile](https://google-auth.readthedocs.io/en/latest/user-guide.html#service-account-private-key-files)
  + [Mock Google Auth Credentials](https://github.com/googleapis/google-cloud-python/blob/75277847ea68d228be4c3e91bb228236489f19f5/storage/tests/unit/url_signer_v4_test_account.json) - because for some reason any substituted values in the private key string would throw an error during test. but this one is used in the google package and it passes tests so great!
