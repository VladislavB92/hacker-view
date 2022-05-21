#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import requests
from bs4 import BeautifulSoup
from connector import create_session
from models.article import Article

session = create_session()


def fetch_data():
    """
    Fills the table with initial article data.
    """
    source_page = "https://news.ycombinator.com"
    response = requests.get(source_page)
    raw_scrap = BeautifulSoup(response.text, "html.parser")
    title_rows = raw_scrap.find_all(
        "tr",
        "athing"
    )
    for row in title_rows:
        if row != "\n":
            sibling = row.next_sibling()
            general_content = row.contents[4].a

            new_article = Article()

            new_article.title = general_content.contents[0]
            new_article.link = general_content.get("href")
            new_article.points = sibling[2].get_text().split(" ", 1)[0]
            new_article.article_date = sibling[4].get("title")

            session.add(new_article)
    session.commit()


def update_data():
    pass
