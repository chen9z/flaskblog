#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    JSONIFY_MIMETYPE = 'application/json;charset=utf-8'
    COOKIE_NAME = 'blog_cookie'
    COOKIE_KEY = 'yclooper'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:chen@localhost:3306/blog'


class ProductionConfig(Config):
    DEBUG=False


configs = {
    'development': DevelopmentConfig,
    'producton': ProductionConfig,
    'default': DevelopmentConfig
}
