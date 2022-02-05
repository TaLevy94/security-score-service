from pydantic import BaseModel
from typing import List

import security_score

class BaseSourceCode(BaseModel):
    name: str
    languge: str

class ScurityScoreParameters(BaseModel):
    security_score: int
    unused_deps: List[str]

class RepoReport(BaseSourceCode):
    url: str
    security_info: ScurityScoreParameters
