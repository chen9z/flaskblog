#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, abort, url_for, jsonify, make_response
from app import app, log
from app.models import User, Blog, Comment
import hashlib, json
from app.apis import APIValueError

__author__ = 'yclooper'


def check_empty(**kw):
    for k, v in kw.items():
        if not v or not v.strip():
            abort(400, '%s can not empty.' % k)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/tt')
def tt():
    render_template('<h>hah</h1>')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.json.get('email')
        passwd = request.json.get('passwd')
        check_empty(email=email, passwd=passwd)
        user = User.query.filter_by(email=email).first()
        if user:
            passwd = hashlib.sha1((user.id + ':' + passwd).encode('utf-8')).hexdigest()
            log('passwd', passwd)
            if user.passwd == passwd:
                return jsonify(user.ob2dict())
            else:
                return abort(400, '密码错误')
        else:
            abort(400, '找不到此用户')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def server_not_found(e):
    render_template('500.html')
