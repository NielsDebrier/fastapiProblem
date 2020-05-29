from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

count = 0

app = FastAPI(
    title="Date api",
    description="The date api for TVH mail analysis.",
    version="0.2.5",
)

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
