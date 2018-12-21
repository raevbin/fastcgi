import sys
import cgi
import pprint
import json
sys.path.append('/var/www/fastcgi')
import toolslib
import logging

def application(environ, start_response):
  #import codecs

  #sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
  #reload(sys)
  #sys.setdefaultencoding('utf-8')
  out=''
  #dt=1
  #for k in environ.keys():
    #toolslib.line_wr(k,dt,0)
    #toolslib.line_wr(environ[k],0,1)
    #dt=0
  logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'/home/evgeniy/temp/test/mylog.log')
  logging.warning( u'OPPS___SSS' )

#  if environ['REQUEST_METHOD'] == 'POST':
#1       outlib = cgi.parse_qs(environ['wsgi.input'].read())
        #baut = pprint.pformat(environ['wsgi.input'].read())
        #out = baut
        #out = baut.decode('utf-8')
#2        recv = environ['wsgi.input'].read()
#2        out = recv.decode('utf-8')                                            
#1       for k in outlib.keys():
#1           a = outlib[k]
#1           b = a[0].decode('utf-8')
#1           out += b+', '
  #out = pprint.pformat(environ['wsgi.input'].read())

  #out = environ['wsgi.input'].read()

#  if environ['REQUEST_METHOD'] == 'GET':
#    d = parse_qsl(environ['QUERY_STRING'])

#    for ch in d:
#      out += ' = '.join(ch)
#      out += '</br>'


  #a = outlib[b'submit']
  #out = json.dumps(a)
  #b = a[0].decode('utf-8')
  #out = b+ '  '+ str(len(a))
  #a.encode('utf-8')

  out.encode('utf-8')
  status = '200 OK'
  ##output = 'йцук'.encode('utf-8')
  #'Content-Type', 'text/html; charset=utf-8'
  #'Content-type', 'text/plain'
  response_headers = [('Content-Type', 'text/html; charset=utf-8'),
                      ('Content-Length', str(len(out))),
                      ('Set-cookie','session=hello!')]
  start_response(status, response_headers)

  return [out]
