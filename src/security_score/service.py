import logging
import json
from tkinter import EXCEPTION

import config
from security_score.adapters.github_adapter import GithubAdapter
from security_score import utils


# Initialize Clients
github_client = GithubAdapter(config.SUPPORTED_LANGUAGES)


async def scan_trending_repos(access_token:str, count:int):
    repos = await github_client.get_trending_repos(access_token=access_token, count=count) 
    for repo in repos:
        await scan_repo(repo.git_url, repo.language)


async def scan_repo(remote_url, language):
    temp_dir = await utils.create_tmp_dir()
    try:
        logging.info(f"cloning {language} repository {remote_url} to {temp_dir}")
        local_code_path = await github_client.clone_repo(remote_url, temp_dir)
        await scan_source_code(local_code_path, language)
    finally:
        # delete function gets access denied error (folder readonly)
        await utils.delete_directory(local_code_path)

async def scan_source_code(local_code_path:str, language:str):
    unused_packages = await detect_unused_dependencies(local_code_path, language)
    pass


async def detect_unused_dependencies(local_code_path, language:str):
    js_command = f"depcheck {local_code_path} --json"
    if(language.lower() == "javascript"):
        cmd = js_command
    if cmd:
        try:
            result = await utils.execute_os_command(cmd)
            output = json.loads(result.stdout)
            unused_dep = len(output['dependencies']) + len(output['devDependencies'])
            return unused_dep
        except Exception as e:
            print("error")
    return -1
async def scan_code(local_code_path: str):
    logging.info(f"scanning project {local_code_path.stem}")

