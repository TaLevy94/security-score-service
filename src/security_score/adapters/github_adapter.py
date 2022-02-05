
import os
from threading import local
from github import Github, GithubException
from github.GithubException import BadCredentialsException, RateLimitExceededException
from git import Repo

import config
from security_score import utils
from errors import GitHubAuthenticationError, GitHubCloneRepoFailedError, GitHubRateLimitExceededError

class GithubAdapter:
    def __init__(self, supported_languages: list): 
        self.supported_languages_query = self._create_languages_query_parameters(supported_languages)

    async def get_trending_repos(self, access_token: str, count: int):
        # TODO identify top trending parameters
        try:
            client = Github(access_token, per_page=count)
            repos = client.search_repositories(self.supported_languages_query).get_page(1)
            return repos
        except BadCredentialsException as e:
            # ToDo: add logger here
            raise GitHubAuthenticationError(str(e))
        except RateLimitExceededException as e:
            raise GitHubRateLimitExceededError(str(e))

    async def clone_repo(self, remote_url, local_path):
        try:
            with Repo.clone_from(remote_url, local_path) as repo_clone:
                return local_path
        except Exception as e:
            GitHubCloneRepoFailedError(str(e))
            
    def _create_languages_query_parameters(self, supported_languages:list):
        query = 'q='
        for language in supported_languages:
            query += f'language:{language}'
        return query