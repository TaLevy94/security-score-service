import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGE", ["javascript"])

TEMPDIR_PREFIX=  os.getenv("TEMPDIR_PREFIX", "repoScanner-")

DEFAULT_REPOS_COUNT= os.getenv("DEFAULT_REPOS_COUNT", 1)