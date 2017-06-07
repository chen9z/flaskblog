#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

from flask import Flask
from flask import render_template
app=Flask(__name__)

from app import views

