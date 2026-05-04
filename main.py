import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Sample App")

if os.getenv("FORCE_CRASH") == "true":
    raise RuntimeError("FORCE_CRASH is set — intentional startup failure for deploy testing")


@app.get("/")
def root():
    return {"message": "Hello from Sample App - Deployment test sample app version 1!"}


@app.get("/health")
def health():
    return {"status": "ok"}
