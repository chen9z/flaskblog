#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

from app import app
from app import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='博客')

