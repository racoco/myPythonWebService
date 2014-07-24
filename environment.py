#! /usr/bin/env python

# The environment dictionary will contain CGI like variables and will be populated 
# by the server at each request from the client. 
# This script will output the whole dictionary.
# To run this script save it as environment.py, open the terminal, 
# navigate to the directory where it was saved and type python 
# environment.py at the command line.

# If in Windows it is necessary first to add the path to python.exe to the system 
# environment variable Path. By the way if you can use Linux in instead of Windows 
# then do it. It will save some pain.

# Now go to the browser and type at the address bar:  http://localhost:8051/


# Our tutorial's WSGI server
from wsgiref.simple_server import make_server

def application(environ, start_response):

   # Sorting and stringifying the environment key, value pairs
   response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
   response_body = '\n'.join(response_body)

   # response body has more than one string
   response_body = ['The Beggining\n',
                    '*' * 30 + '\n',
                    response_body,
                    '\n' + '*' * 30 ,
                    '\nThe End']
   # So the content lenght is the sum of all string lenghts
   content_length = 0
   for s in response_body:
      content_length += len(s)
      
   
   status = '200 OK'
   response_headers = [('Content-Type', 'text/plain'),
                  ('Content-Length', str(content_lenght))]
                  
   start_response(status, response_headers)

   return [response_body]

# Instantiate the WSGI server.
# It will receive the request, pass it to the application
# and send the application's response to the client
httpd = make_server(
   'localhost', # The host name.
   8051, # A port number where to wait for the request.
   application # Our application object name, in this case a function.
   )

# Wait for a single request, serve it and quit.
httpd.handle_request()
