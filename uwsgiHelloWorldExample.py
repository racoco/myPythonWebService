
# To run this with the uWSGI binary:
#    uwsgi --http :9090 --wsgi-file uwsgiHelloWorldExample.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Hello World"]
    
