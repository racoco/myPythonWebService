
# To run this with the uWSGI binary:
#    uwsgi --http :9090 --wsgi-file uwsgiHelloWorldExample.py
# See: https://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html
#
# NOTE: The above command must be run in the same directory in which uwsgi was built. Why?

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Hello World"]
    
