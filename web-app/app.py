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
    connection_string = f"postgresql://{user}:{password}@postgres:5432/dwh"

    with psycopg.connect(connection_string) as conn:
        cur = conn.cursor()

        return cur.execute("SELECT * FROM prod.transactions").fetchall()
