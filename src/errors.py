class GitHubAuthenticationError(Exception):
    def __init__(self, error):
        super().__init__(f"Failed authentication to github Error: {error}")

class GitHubRateLimitExceededError(Exception):
    def __init__(self, error):
        super().__init__(f"Failed fetching github, exceeded requests limit Error: {error}")

class GitHubCloneRepoFailedError(Exception):
    def __init__(self, error):
        super().__init__(f"Failed authentication github Error: {error}")

class FilesDeletionFailedError(Exception):
    def __init__(self, error, full_path):
        super().__init__(f"Failed Cleanup local files in {full_path} Error: {error}")
