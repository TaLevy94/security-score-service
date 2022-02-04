import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGE", ["javascript"])

TEMPDIR_PREFIX=  os.getenv("TEMPDIR_PREFIX", "repoScanner-")