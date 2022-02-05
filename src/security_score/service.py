import logging
import json

import config
from security_score.adapters.github_adapter import GithubAdapter
from security_score.models import RepoReport,ScurityScoreParameters
from security_score import utils


# Initialize Clients
github_client = GithubAdapter(config.SUPPORTED_LANGUAGES)


async def scan_trending_repos(access_token:str, count:int):
    repos = await github_client.get_trending_repos(access_token=access_token, count=count) 
    repos_report = []
    for repo in repos:
        repos_report.append(await scan_repo(repo))
    return repos_report


async def scan_repo(repo):
    remote_url = repo.git_url
    language = repo.language
    try:
        temp_dir = await utils.create_tmp_dir()
        logging.info(f"cloning {language} repository {remote_url} to {temp_dir}")
        code_path = await github_client.clone_repo(remote_url, temp_dir)
        security_props = await scan_source_code(code_path, language)
    finally:
        await utils.delete_directory(code_path)
    repo_report = RepoReport(name = repo.name, languge=language, url=remote_url, security_info=security_props)
    return repo_report

async def scan_source_code(code_path:str, language:str):
    unused_packages = await detect_unused_dependencies(code_path, language)
    secure_score = await calculate_secure_score(unused_packages)
    securiy_props = ScurityScoreParameters(unused_deps=unused_packages, security_score=secure_score)
    return securiy_props

# TODO implement secure score calculation 
async def calculate_secure_score(unused_packages):
    return len(unused_packages)

async def detect_unused_dependencies(code_path: str, language:str):
    if(language.lower() == "javascript"):
        deps = await get_unused_dependencies_js(code_path)
    return deps
    
async def get_unused_dependencies_js(code_path: str, include_dev=True):
    js_command = f"depcheck {code_path} --json"
    try:
            result = await utils.execute_os_command(js_command)
            output = json.loads(result.stdout)
            unused_dep = output['dependencies']
            if(include_dev):
                unused_dep.extend(output['devDependencies'])
            return unused_dep
    except Exception as e:
        logging.error("error while using js depcheck")
        return None

