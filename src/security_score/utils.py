import logging
import shutil
from tempfile import mkdtemp

def get_log_level(log_level):
    log_levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR
    }
    return log_levels.get(log_level, logging.DEBUG)

async def create_tmp_dir():
    return mkdtemp(prefix="repoScanner-")

async def delete_directory(dir_path):
    shutil.rmtree(dir_path)

