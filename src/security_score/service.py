import logging

import config
from security_score.adapters.github_adapter import GithubAdapter
from security_score import utils

# Initialize Clients
github_client = GithubAdapter(config.SUPPORTED_LANGUAGES)

async def scan_trending_repos(access_token:str, count:int):
    repos = await github_client.get_trending_repos(access_token=access_token, count=count) 
    for repo in repos:
        await scan_repo(repo.git_url, repo.language)
    print("bye")

async def scan_repo(remote_url, language):
    temp_dir = await utils.create_tmp_dir()
    try:
        logging.info(f"cloning {language} repository {remote_url} to {temp_dir}")
        local_code_path = await github_client.clone_repo(remote_url, temp_dir)
        await scan_source_code(local_code_path, language)
    finally:
        # delete function gets access denied error (folder readonly)
        await utils.delete_directory(local_code_path)

async def scan_source_code(local_code_path, language):
    pass
