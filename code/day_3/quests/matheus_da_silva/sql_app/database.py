from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={
                       "cehck_same_thread": False})

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


base = declarative_base()
