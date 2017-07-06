#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

import time
from datetime import datetime

def datetime_filter(t):
    deld=int(time.time()-t)
    if deld<60:
        return '1分钟前'
    elif deld<3600:
        return '%s分钟前'%(t//60)
    elif deld<86400:
        return '%s小时前'%(t//3600)
    elif deld<604800:
        return '%s天钱'%(t//86400)
    else:
        dt=datetime.fromtimestamp(t)
        return '%s年%s月%s天'%(dt.year,dt.month,dt.day)
