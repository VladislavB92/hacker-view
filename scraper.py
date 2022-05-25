#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import requests
from bs4 import BeautifulSoup
from connector import create_session
from models.article import Article

session = create_session()


def fetch_data():
    """Fills the table with initial article data."""
    source_page = "https://news.ycombinator.com"
    response = requests.get(source_page)
    raw_scrap = BeautifulSoup(response.text, "html.parser")
    title_rows = raw_scrap.find_all(
        "tr",
        "athing"
    )
    for row in title_rows:
        title = row.contents[4].a.contents[0]
        link = row.contents[4].a.get("href")
        if link.startswith("item?"):
            link = "https://news.ycombinator.com/" + link
        points = row.next_sibling()[2].get_text().split(" ", 1)[0]
        date = row.next_sibling()[4].get("title")

        if check_data_exists(title):
            existing_article = check_data_exists(title)
            existing_article.points = points
            session.add(existing_article)
            print("Points for the existing article updated!")
            continue

        new_article = Article()
        new_article.title = title
        new_article.link = link
        new_article.points = points
        new_article.article_date = date

        session.add(new_article)
        print("New article saved!")
    session.commit()


def update_data():
    """Updates article points."""
    fetch_data()


def check_data_exists(article_title):
    """Check if article exists."""
    all_articles = session.query(Article)
    match = all_articles.filter_by(title=article_title).first()
    return match
