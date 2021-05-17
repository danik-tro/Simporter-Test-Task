from sqlalchemy import create_engine, Integer, String, Column, TIMESTAMP, Table, MetaData
from sqlalchemy.types import Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQL_DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./data.db')

engine = create_engine(
    SQL_DATABASE_URL, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

meta = MetaData()

Data = Table('data', meta,
             Column("id", String, primary_key=True),
             Column("asin", String),
             Column("brand", String),
             Column("source", String),
             Column("stars", Integer),
             Column("timestamp", Integer)
             )
