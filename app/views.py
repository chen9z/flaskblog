#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, abort, url_for, jsonify, make_response, g
from app import app, log
from app.models import User, Blog, Comment
import hashlib, json, time
from config import Config
from app import db

__author__ = 'yclooper'


def check_empty(**kw):
    for k, v in kw.items():
        if not v or not v.strip():
            abort(400, '%s can not empty.' % k)

def check_admin(user):
    if(user.name!='yclooper'):
        abort(400,'no permission')

def user2cookie(user, max_age=86400):
    expires = str(int(time.time()) + max_age)
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, Config.COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


def cookie2user():
    cookies = request.cookies.get(Config.COOKIE_NAME)
    log('cookie', cookies)
    if not cookies:
        return None
    L = cookies.split('-')
    if len(L) != 3:
        return None
    uid, expires, sha1 = L
    if int(expires) < time.time():
        return None
    user = User.query.get(uid)
    if not user:
        return None
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, Config.COOKIE_KEY)
    if sha1 == hashlib.sha1(s.encode('utf-8')).hexdigest():
        log('验证成功', user.__str__())
        return user


@app.before_request
def before_request():
    g.user = cookie2user()


# @app.after_request
# def after_request(response):
#     print(response.json)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def server_not_found(e):
    render_template('500.html')


@app.route('/')
@app.route('/index')
def index():
    try:
        return render_template('index.html', user=g.user)
    except:
        return render_template('index.html')


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
                g.user = user
                respone = jsonify(user.ob2dict())
                respone.set_cookie(Config.COOKIE_NAME, user2cookie(user), max_age=86400, httponly=True)
                return respone
            else:
                return abort(400, '密码错误')
        else:
            abort(400, '找不到此用户')


@app.route('/signout', methods=['GET', 'POST'])
def sign_out():
    log('url', url_for('index'))
    resp = make_response(render_template('index.html'))
    resp.set_cookie(Config.COOKIE_NAME, '', max_age=86400, httponly=True)
    return resp


@app.route('/manage/blogs')
def manage_blogs():
    return render_template('manage_blogs.html')

@app.route('/manage/blogs/create')
def manage_blog():
    return render_template('manage_blog_edit.html', id='', action='/api/blogs/create')


@app.route('/api/blogs/create', methods=['GET','POST'])
def blog_create():
    name = request.json.get('name')
    content = request.json.get('content')
    check_empty(name=name,content=content)
    check_admin(g.user)
    blog = Blog(name=name, content=content, user_name=g.user.name,user_id=g.user.id, user_image=g.user.image)
    db.session.add(blog)
    db.session.commit()
    return jsonify(name=blog.name,content=blog.content)

