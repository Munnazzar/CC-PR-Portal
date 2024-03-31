import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_NAME = os.environ["DATABASE_NAME"]