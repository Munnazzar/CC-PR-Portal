from urllib.parse import quote_plus
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Use quote_plus to handle any special characters in the username and password
USERNAME = os.environ["MONGO_DATABASE_USERNAME"]
PASSWORD = os.environ["MONGO_DATABASE_PASSWORD"]
DATABASE_HOST = os.environ["MONGO_DATABASE_HOST"]
DATABASE_NAME = os.environ["MONGO_DATABASE_NAME"]