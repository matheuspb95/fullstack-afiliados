from environs import Env

env = Env()
env.read_env()

POSTGRES_USER = env.str("POSTGRES_USER")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
POSTGRES_DB = env.str("POSTGRES_DB")
POSTGRES_PORT = env.str("POSTGRES_PORT")
POSTGRES_HOST = env.str("POSTGRES_HOST")

ENV = env.str("ENVIRONMENT", "")
if not ENV:
    POSTGRES_HOST = f"localhost:{POSTGRES_PORT}"

DATABASE_URL = env.str("DATABASE_URL", f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")