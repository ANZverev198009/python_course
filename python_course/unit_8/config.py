from dotenv.main import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOSTNAME = os.environ['POSTGRES_HOSTNAME']
DATABASE_PORT = os.environ['DATABASE_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']


POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{DATABASE_PORT}"
