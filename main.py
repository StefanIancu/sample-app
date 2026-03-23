from fastapi import FastAPI

app = FastAPI(title="Sample App")


@app.get("/")
def root():
    return {"message": "Hello from dev branch of Sample App - Deployment v2.5!"}


@app.get("/health")
def health():
    return {"status": "ok"}
