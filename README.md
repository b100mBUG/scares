# October 31 — created by King Kastro

## Run locally
```
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://localhost:8000

## Deploy to Vercel
1. Push this folder to a GitHub repo (keep `main.py`, `vercel.json`, `requirements.txt` and `static/` at the repo root).
2. In Vercel: Add New → Project → import the repo. Framework preset: **Other**. Leave build settings empty.
3. Deploy. Every URL serves the page.

## Deploy to Render / Railway
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT` (Procfile included)

Health check: `/healthz`
