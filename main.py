from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Sample App (degraded test branch)")


# Intentional 5xx on the root route so the post-deploy application_check
# fails as "reachable but erroring". The app still binds the port and stays
# up (uvicorn keeps serving), so this exercises the degraded-preview flow:
# on a non-production env the deploy should be published live-but-degraded
# rather than torn down. /health stays 200 so the container looks alive.
@app.get("/")
def root():
    return JSONResponse(
        status_code=500,
        content={
            "error": "Intentional HTTP 500 from the 'degraded' test branch "
                     "to verify degraded-preview deploys.",
        },
    )


@app.get("/health")
def health():
    return {"status": "ok"}
