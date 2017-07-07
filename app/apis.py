#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'yclooper'

class Page(object):
    def __init__(self,item_count,page_index=1,page_size=10):
        self.item_count=item_count
        self.page_size=page_size
        self.page_count=item_count//page_size+(1 if item_count%page_size>0 else 0)
        if(item_count==0 or page_size>item_count):
            self.limit=0
            self.offset=0
            self.page_index=1
        else:
            self.limit=page_size
            self.offset=page_size*(page_index-1)
            self.page_index=page_index
        self.has_previous=self.page_index>1
        self.has_next=self.page_index<self.page_count

    def ob2dict(self):
        return {
            'item_count':self.item_count,
            'page_size':self.page_size,
            'page_count': self.page_count,
            'limit': self.limit,
            'offset':self.offset,
            'page_index':self.page_index
        }

    def __str__(self):
        return 'item_count:%s,page_size:%s,page_count:%s,limit:%s,offset:%s,page_index:%s'%(self.item_count,self.page_size,self.page_count,self.limit,self.offset,self.page_index)

class ApiError(Exception):
    def __init__(self, error, data='', message=''):
        super(ApiError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(ApiError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(ApiError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''

    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(ApiError):
    '''
    Indicate the api has no permission.
    '''

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)
