#!/usr/bin/env python

from flask import Blueprint, current_app, render_template, g
from pitchfork.adminbp.decorators import check_perms


bp = Blueprint(
    'manage_globals',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/manage'
)


import pymongo
import api_globals
