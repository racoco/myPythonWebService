myPythonWebService
==================

Learn Python, WSGI, uWSGI

Make simple web service.
Use python, apache2, and mod_wsgi to understand how this works.
Maybe use uWSGI (mod_proxy_uwsgi) instead? If so, document how used, etc.

Apache
------

  To start/stop apache:
    * sudo apachectl start / stop / restart
    
  To enable PHP:
    * sudo vim /etc/apache2/httpd.conf
    * Uncomment the line "LoadModule php5_module  libexec/apache2/libphp5.so
    
  To host files in SItes, create OSX users, etc see:
    * http://machiine.com/2013/how-to-install-apache-and-php-on-a-mac-with-osx-10-8-mamp-part-1/
    


