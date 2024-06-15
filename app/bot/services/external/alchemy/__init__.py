"""
the database engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.bot.settings.internal.conf import DB_URL


engine = create_engine(
    url=DB_URL,
)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = sessionmaker(bind=engine)
