from os import environ

DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", environ["TMPDIR"])

# Get one from here: https://acoustid.org/new-application
ACOUSTID_API_KEY = environ.get("ACOUSID_API_KEY", "insert_api_key_here") 
