#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configs
import logging;logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
app.config.from_object(configs['default'])
db = SQLAlchemy(app)

def log(name,msg=''):
    logging.info('%s:%s'%(name,msg))

from app import views
