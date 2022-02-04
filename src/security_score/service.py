import logging

from security_score.adapters.github_adapter import GithubAdapter
import config

# Initialize Clients
github_client = GithubAdapter(config.SUPPORTED_LANGUAGES)

async def scan_trending_repos(access_token:str, count:int):
    pass