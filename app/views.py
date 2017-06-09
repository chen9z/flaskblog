#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, abort, url_for
from app import app, log
from app.models import User, Blog, Comment
import hashlib
from app.apis import APIValueError

__author__ = 'yclooper'


def check_empty(**kw):
    for k, v in kw.items():
        if not v or not v.strip():
            abort(400, '%s can not empty.' % k)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='博客')

@app.route('/tt')
def tt():
    render_template('<h>hah</h1>')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='登录')
    else:
        email = request.json.get('email')
        passwd = request.json.get('passwd')
        check_empty(email=email, passwd=passwd)
        user = User.query.filter_by(email=email).first()
        if user:
            passwd = hashlib.sha1((user.id + ':' + passwd).encode('utf-8')).hexdigest()
            if user.passwd == passwd:
                log('重定向', '重定向')
                return redirect('/index')
            else:
                raise ValueError('账号或密码错误')
        else:
            raise APIValueError('服务器错误')