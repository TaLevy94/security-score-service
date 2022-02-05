import os
import stat
import shutil
import logging
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
    #TODO Fix acceess denied bug
    try:
        # for tests
        #shutil.rmtree(dir_path, onerror=_on_rm_error)
        pass
    except FileNotFoundError:
        pass
    

async def execute_os_command(command:str):
    ''' 
    Gets str command for better human usability 
    '''
    command_obj = command.split()
    ps_output = subprocess.run(command_obj, shell=True, capture_output=True)
    return ps_output

def _on_rm_error( func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod( path, stat.S_IWRITE )
    os.unlink( path )
