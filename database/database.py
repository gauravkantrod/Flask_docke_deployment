import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv()

database_URL = \
    "mysql://" + os.getenv('MYSQL_USER') + ":" + os.environ['MYSQL_PASSWORD'] + \
    "@" + os.environ['MYSQL_HOST'] + ":" + os.environ['MYSQL_PORT'] + "/" + os.environ['MYSQL_DB']

engine = create_engine(database_URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)
