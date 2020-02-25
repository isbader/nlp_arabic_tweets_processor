import sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite
#import pysqlite
#assert sqlite3.sqlite_version_info < (3, 10, 0)

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'

    name = Column(String(80),nullable = False)
    id = Column(Integer, primary_key = True)

class DataSet(Base):
    __tablename__ = 'dataset'

    id = Column(Integer,primary_key = True)
    tweet = Column(String(250),nullable=False)
    time = Column(String(50))
    label = Column(String(15),nullable = True)
    data_id = Column(ForeignKey('data.id'))
    data = relationship(Data)

###

engine = create_engine('sqlite:////Users/isbader/Desktop/projects/nlp_arabic_tweets_processor/data_distribution_sys/aby_2.0/aby.db')
Base.metadata.create_all(engine)
