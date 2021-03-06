# -*- coding:utf-8 -*-
'''
Created on 2013-3-26

@author: zhuhua
'''
import sys
import tornado.httpserver
import tornado.ioloop
from tornado import options

from simpletor import application
import settings
         
if __name__ == '__main__':
    
    port = settings.port
    if len(sys.argv) == 2:
        port = sys.argv[1]
    
    options.options.logging = "debug"
    options.parse_command_line()

    server = tornado.httpserver.HTTPServer(application.Application())
    server.listen(port)
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()