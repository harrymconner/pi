import fastapi

app = fastapi.FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"response": "hello world"}
