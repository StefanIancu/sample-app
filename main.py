from fastapi import FastAPI

app = FastAPI(title="Sample App")


@app.get("/")
def root():
    return {"message": "Hello from stg branch of Sample App - Staging Branch!"}


@app.get("/health")
def health():
    return {"status": "ok"}
