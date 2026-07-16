from tempdir import TempDir
from os import environ, getcwd

# Where should we download from? (Populated at runtime.)
YOUTUBE_LINK = None

# Where should intermediary downloads be stored as they are processed?
DOWNLOAD_LOCATION = TempDir().name

# Where should completed files be output to?
OUTPUT_LOCATION = environ.get("OUTPUT_LOCATION", getcwd())

# Should we move the completed file into jellyfin? (default=no)
JELLYFIN_LIBRARY = environ.get("JELLYFIN_LIBRARY", None)

# Get one from here: https://acoustid.org/new-application
ACOUSTID_API_KEY = environ.get("ACOUSID_API_KEY", "<insert-api-key-here>")

