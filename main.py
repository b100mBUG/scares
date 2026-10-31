from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse, PlainTextResponse

BASE = Path(__file__).resolve().parent
INDEX = BASE / "static" / "index.html"

app = FastAPI(title="October 31", docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(GZipMiddleware, minimum_size=1024)

HEADERS = {
    "Cache-Control": "public, max-age=600",
    "X-Content-Type-Options": "nosniff",
}


@app.get("/healthz", response_class=PlainTextResponse)
def healthz():
    return "it is still october 31"


@app.get("/")
@app.get("/{path:path}")
def page(path: str = ""):
    return FileResponse(INDEX, media_type="text/html; charset=utf-8", headers=HEADERS)


if __name__ == "__main__":
    import os
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
