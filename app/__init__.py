#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging;logging.basicConfig(level=logging.INFO)

app=Flask(__name__)
app.config['SECRET_KEY']='yclooper'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:chen@localhost:3306/blog'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)


def log(name,msg):
    logging.info('%s:%s'%(name,msg))

from app import views