#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import os
import commands
import utils
import views.articles
from flask import Flask


logger = utils.configure_logging()


def create_app() -> Flask:
    """Creates a Flask app instance."""
    app = Flask(__name__)
    app.name = "Hacker-view"
    app.secret_key = "super secret key"
    app.version = get_version()
    app.debug = True
    register_blueprints(app)
    return app


def get_version():
    """Gets the version number from the file."""
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
            "Failed to get version number from file.",
            exc_info=err
        )
        return None


def register_blueprints(app):
    """Registers Flask blueprints."""
    app.register_blueprint(views.articles.blueprint)
    app.register_blueprint(commands.cli_commands)
    logger.info("Blueprints registered.")
