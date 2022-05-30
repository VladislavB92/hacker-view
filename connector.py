#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.article import Base
from utils import configure_logging


logger = configure_logging()


def create_connection():
    """Creates a connection engine."""
    engine = create_engine(
        "sqlite+pysqlite:///hacker-view.db",
        future=True,
        connect_args={
            "check_same_thread": False
        }
    )
    Base.metadata.create_all(engine)
    logger.info("Database engine created.")
    return engine


def create_session():
    """Creates a database connection session."""
    Session = sessionmaker()
    Session.configure(
        bind=create_connection()
    )
    session = Session()
    logger.info("Database session created.")
    return session
