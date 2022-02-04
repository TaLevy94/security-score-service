from fastapi import APIRouter, status
import logging

from security_score.service import scan_trending_repos
router = APIRouter(tags=['GitHub AppSec Scanner'])


@router.get("/repos/trending",status_code=status.HTTP_200_OK)
async def get_trending_repos_risk_score(access_token: str ,count:int = 5):
    logging.info(f"trending repos request started for {count} repositories")
    security_score = await scan_trending_repos(access_token=access_token, count=count)