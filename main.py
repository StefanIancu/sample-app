from fastapi import FastAPI

app = FastAPI(title="Sample App")


@app.get("/")
def root():
    return {"message": "Hello from Sample App - Deployment test test test!"}


@app.get("/health")
def health():
    return {"status": "ok"}
