from fastapi import FastAPI
from routers import summarize

app = FastAPI(title="Shosei-sha Summarization API")
app.include_router(summarize.router, prefix="/api/summarize")