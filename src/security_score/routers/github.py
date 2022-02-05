from fastapi import APIRouter, status, HTTPException
from typing import List
import logging

import config
from security_score.service import scan_trending_repos
from security_score.models import RepoReport
from errors import GitHubAuthenticationError, GitHubCloneRepoFailedError, GitHubRateLimitExceededError

router = APIRouter(tags=['GitHub AppSec Scan'])

@router.get("/v1/repos/trending",status_code=status.HTTP_200_OK, response_model= List[RepoReport])
async def get_trending_repos_risk_score(access_token: str ,count:int = config.DEFAULT_REPOS_COUNT):
    try:
        logging.info(f"trending repos request started for {count} repositories")
        repos_report = await scan_trending_repos(access_token=access_token, count=count)
        return repos_report
    except GitHubAuthenticationError:
        raise HTTPException(status_code=401, detail="access token invalid")
    except GitHubRateLimitExceededError:
        raise HTTPException(status_code=500, detail="Github rate limit exceeded")
    except GitHubCloneRepoFailedError:
            raise HTTPException(status_code=500, detail="Github rate limit exceeded")