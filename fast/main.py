from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

count = 0

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def test():
    global count
    count += 1
    return count
