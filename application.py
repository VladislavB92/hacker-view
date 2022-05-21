#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import os
import scraper
from connector import create_connection
from app_factory import create_app

application = create_app()

if __name__ == "__main__":
    application.debug = True
    engine = create_connection()
    scraper.fetch_data()
    application.run(
        host=os.getenv("FLASK_HOST", "localhost"),
        port=int(os.getenv("FLASK_PORT", 5005))
    )
