#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import render_template
from app import app

__author__ = 'yclooper'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='博客')

@app.route('/login')
def login():
    return render_template('login.html',title='登录')

@app.route('/')
