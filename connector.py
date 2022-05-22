#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.article import Base


def create_connection():
    """
    Creates a connection engine.
    """
    engine = create_engine(
        "sqlite+pysqlite:////Users/vlad/Desktop/hacker-view/hacker-view.db",
        echo=True,
        future=True
    )
    Base.metadata.create_all(engine)
    return engine


def create_session():
    """
    Creates a database connection session.
    """
    Session = sessionmaker()
    Session.configure(
        bind=create_connection()
    )
    session = Session()
    return session
