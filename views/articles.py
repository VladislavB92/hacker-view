#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import logging
from flask import Blueprint, render_template

import scraper
from models.article import Article

logger = logging.getLogger(__name__)

blueprint = Blueprint("lookups", __name__)

session = scraper.session


@blueprint.route("/", methods=["GET"])
def all_articles():
    """Lists all scrapped articles."""
    scraper.fetch_data()
    articles = session.query(Article).all()
    context = {
        "articles": articles
    }
    return render_template("index.html", **context)

