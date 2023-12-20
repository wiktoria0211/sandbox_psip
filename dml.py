## nalezy dodac ectation

import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String
# from utils import get_coords
# from dane import users_list

load_dotenv()

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    port=os.getenv('POSTGRES_PORT')
)

engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

