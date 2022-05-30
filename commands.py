#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

from flask import Blueprint
from scraper import fetch_data


cli_commands = Blueprint("articles", __name__)


@cli_commands.cli.command("update-points")
def update_points():
    """Launches the article points update process."""
    fetch_data()
