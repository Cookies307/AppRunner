from wsgiref.simple_server import make server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
  name os.environ.get('NAME')
  If name None or len(name) :
    name "world"
  message "Hello, +name+"\n"
  return Response(message)

if_name_main':
  port int(os.environ.get("PORT"))
  with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name 'hello')
    app config.make_wsgi_app()
  server make server('0.0.0.0', port, app)
  server.serve_forever()
