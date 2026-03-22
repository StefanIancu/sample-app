from fastapi import FastAPI

app = FastAPI(title="Sample App")


@app.get("/")
def root():
    return {"message": "Hello from Sample App - Deployment v2.4!"}


@app.get("/health")
def health():
    return {"status": "ok"}
