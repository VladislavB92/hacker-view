#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import logging
from flask import Blueprint, request, url_for, redirect, render_template
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

blueprint = Blueprint("lookups", __name__)


@blueprint.route("/articles", methods=["GET"])
def all_articles():
    """Lists all scrapped articles."""
    source_page = "https://news.ycombinator.com"
    raw_scrap = BeautifulSoup(source_page, "html.parser")

