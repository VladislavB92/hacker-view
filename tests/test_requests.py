#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Vladislavs Bužinskis"

import pytest
import requests
from app_factory import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hackernews(client):
    response = requests.get("https://news.ycombinator.com")
    assert response.status_code == 200


def test_main_page(client):
    response = client.get("/")
    assert response.status_code == 200
