import os
import random
import sqlalchemy
from dotenv import load_dotenv
import os
import sqlalchemy.orm
from faker import Faker
from geoalchemy2 import Geometry
load_dotenv()


db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    port=os.getenv("POSTGRES_PORT")
)

engine = sqlalchemy.create_engine(db_params)
print("ZDOBYTE WŁOŚCI")
connection = engine.connect()


Base = sqlalchemy.orm.declarative_base()

class User(Base):
    __tablename__ = 'main_table'

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True) ##serial
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location =sqlalchemy.Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

Base.metadata.create_all(engine)


### Create/insert

Session = sqlalchemy.orm.sessionmaker(bing=engine)
session = Session()

lista_userow: list = []



fake = Faker()

for item in range(100):
    lista_userow.append(
        User(
        name=fake.name(),
        location=f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
        )
    )

session.add_all(lista_userow)
session.commit()


session.flush()
connection.close()
engine.dispose()

if__name__ == __main__:
    main()