import os

import bw
import dotenv
import fastapi
import psycopg

dotenv.load_dotenv()

app = fastapi.FastAPI()


@app.get("/")
async def root() -> tuple[str] | None:
    user = bw.get_secret(os.environ["POSTGRES_USER"])
    password = bw.get_secret(os.environ["POSTGRES_PASSWORD"])
    connection_string = f"host=postgres user={user} password={password}"

    with psycopg.connect(connection_string) as conn:
        cur = conn.cursor()

        return cur.execute("SELECT 'hello world'").fetchone()
