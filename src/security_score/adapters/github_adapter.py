import os
from threading import local
from github import Github
from git import Repo

import config
from security_score import utils

class GithubAdapter:
    def __init__(self, supported_languages: list): 
        self.supported_languages_query = self._create_languages_query_parameters(supported_languages)

    async def get_trending_repos(self, access_token: str, count: int):
        # TODO identify top trending parameters
        client = Github(access_token, per_page=count)
        repos = client.search_repositories(self.supported_languages_query).get_page(1)
        return repos

    async def clone_repo(self, remote_url, local_path):
        # for test usage
        return f"C:\\Users\\talev\\AppData\\Local\\Temp\\repoScanner-lj_wdgsu"

        # with Repo.clone_from(remote_url, local_path) as repo_clone:
        #     return local_path
  
    def _create_languages_query_parameters(self, supported_languages:list):
        query = 'q='
        for language in supported_languages:
            query += f'language:{language}'
        return query