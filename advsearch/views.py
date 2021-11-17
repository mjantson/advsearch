# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 martin jantson.
#
# Advanced-Search is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""advanced search page repo"""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from flask import Blueprint, render_template
from flask_babelex import gettext as _

blueprint = Blueprint(
    'advsearch',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route("/")
def index():
    """Render a basic view."""
    return render_template(
        "advsearch/index.html",
        module_name=_('Advanced-Search'))
