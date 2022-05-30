#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import scraper
from flask import Blueprint, render_template, request
from models.article import Article


blueprint = Blueprint("articles_index", __name__)

session = scraper.session


@blueprint.route("/", methods=("GET", "POST"))
def all_articles():
    """Lists all scrapped articles."""
    if request.method == "POST":
        scraper.fetch_data()

    articles = session.query(Article).order_by(
        Article.points.desc()
    ).limit(
        30
    ).all()

    context = {
        "articles": articles
    }
    return render_template("index.html", **context)
