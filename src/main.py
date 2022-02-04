import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

import config
from security_score.utils import get_log_level

app = FastAPI(title="Security Score Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

async def init_logger():
    formatter = "%(levelname)s - %(asctime)s | %(message)s"
    logging.basicConfig(level=get_log_level(config.LOG_LEVEL), format=formatter)

@app.on_event('startup')
async def before_server_start():
    await init_logger()

if __name__ == '__main__':  # For Debugging
    uvicorn.run(app, host='0.0.0.0', port=5000)
