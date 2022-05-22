#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import logging
import os
import commands
import views.articles
from typing import Union
from flask import Flask

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """
    Creates a Flask app instance.
    :return: Flask app instance
    """
    app = Flask(__name__)
    app.name = "Hacker-view"
    app.version = get_version()
    register_blueprints(app)
    return app


def get_version() -> Union[str, None]:
    """
    Gets the version number from the file.
    :return: A string with the version number or None
    """
    try:
        file = "VERSION.txt"
        with open(
                os.path.join(
                    os.path.dirname(__file__),
                    file
                )
        ) as f:
            version = f.read().strip()
            logger.info(f"Current app version: {version}")
            return version
    except Exception as err:
        logger.exception(
            "Failed to get version number from file",
            exc_info=err
        )
        return None


def register_blueprints(app):
    app.register_blueprint(views.articles.blueprint)
    app.register_blueprint(commands.cli_commands)
