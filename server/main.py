from fastapi import FastAPI

app = FastAPI()

# health checking


@app.get("/")
def root():
    return {
        "hello": "world"
    }
