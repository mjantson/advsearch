# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 martin jantson.
#
# Advanced-Search is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from advsearch import AdvancedSearch


def test_version():
    """Test version import."""
    from advsearch import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = AdvancedSearch(app)
    assert 'advsearch' in app.extensions

    app = Flask('testapp')
    ext = AdvancedSearch()
    assert 'advsearch' not in app.extensions
    ext.init_app(app)
    assert 'advsearch' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to Advanced-Search' in str(res.data)
