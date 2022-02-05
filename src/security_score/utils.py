import logging
import shutil
import subprocess
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

async def execute_os_command(command:str):
    ''' 
    Gets str command for better human usability 
    '''
    command_obj = command.split()
    ps_output = subprocess.run(command_obj, shell=True, capture_output=True)
    return ps_output


