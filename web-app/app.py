import os

import dotenv
import fastapi
import psycopg

dotenv.load_dotenv()

app = fastapi.FastAPI()


@app.get("/")
async def root() -> list[tuple[int, float]]:
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    host = os.environ["POSTGRES_HOST"]
    port = os.environ["POSTGRES_PORT"]
    database = os.environ["POSTGRES_DATABASE"]
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"

    with psycopg.connect(connection_string) as conn:
        cur = conn.cursor()

        return cur.execute("SELECT * FROM prod.transactions").fetchall()
