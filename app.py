#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flup.server.fcgi import WSGIServer
#import flup


def app(environ, start_response):
     start_response('200 OK', [('Content-Type', 'text/html')])
     return('''<html>
     <head>
          <title>Hello World!</title>
     </head>
     <body>
          <h1>Hello world!</h1>
     </body>
</html>''')

WSGIServer(app, bindAddress = '/tmp/fcgi.sock').run()
#WSGIServer(app).run()
#WSGIServer(app, bindAddress = ('0.0.0.0', 10000)).run()