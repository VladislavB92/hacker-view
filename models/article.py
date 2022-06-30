#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Article(Base):
    """Article module."""
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    points = Column(Integer)
    article_date = Column(String)
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=True,
        onupdate=datetime.datetime.now()
    )
