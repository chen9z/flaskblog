#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

from app import db
import time, uuid


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.VARCHAR(50), primary_key=True, default=next_id())
    name = db.Column(db.VARCHAR(50))
    email = db.Column(db.VARCHAR(50))
    passwd = db.Column(db.VARCHAR(50))
    admin = db.Column(db.Boolean)
    image = db.Column(db.VARCHAR(500))
    created_at = db.Column(db.Float, default=time.time())

    def ob2dict(self):
        d = self.__dict__.copy()
        d['passwd'] = '******'
        d.pop('_sa_instance_state')
        return d

    def __repr__(self):
        return '<User %r>' % (self.name)


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.VARCHAR(50), primary_key=True, default=next_id())
    name = db.Column(db.VARCHAR(50))
    content = db.Column(db.TEXT)
    user_id = db.Column(db.VARCHAR(50))
    user_image = db.Column(db.VARCHAR(500))
    user_name = db.Column(db.VARCHAR(50))
    created_at = db.Column(db.Float, default=time.time())

    def __repr__(self):
        return '<Blog %r>' % (self.name)

    def ob2dict(self):
        d = self.__dict__.copy()
        d.pop('_sa_instance_state')
        return d


class Comment(db.Model):
    __tablename__ = 'Comments'
    id = db.Column(db.VARCHAR(50), primary_key=True, default=next_id())
    blog_id = db.Column(db.VARCHAR(50))
    user_id = db.Column(db.VARCHAR(50))
    user_name = db.Column(db.VARCHAR(50))
    user_image = db.Column(db.VARCHAR(500))
    content = db.Column(db.TEXT)
    created_at = db.Column(db.Float, default=time.time())

    def __repr__(self):
        return '<Comment %r>' % (self.content)
