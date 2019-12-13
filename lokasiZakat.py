#!/usr/bin/env python
# coding: utf-8

# In[6]:


from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from requests.models import PreparedRequest
import requests
import json
import urllib.parse
import os.path
import time
import register as reg
import googleAPI 
from googleAPI import GooglePlaces as ga

HOST_NAME = 'zakatapi.org'
#PORT_NUMBER = 9000

class MyHandler(BaseHTTPRequestHandler):
      
    def generate_sections_of_url(self, url):
        path = urllib.parse.urlsplit(url).path
        print(path)
        sections = urllib.parse.parse_qs(path)
        return sections
    
    def handle_http(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        content = ga.get_lokasi()
        self.wfile.write(json.dumps(content).encode())

    def respond(self, status_code):
        print(status_code)
        response = self.handle_http(status_code)
        self.wfile.write(response)
        
    def no_respond(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content = '''
        <html>
        <body><p>url not found</p>
        </body></html>
        '''
        self.wfile.write(bytes(content, 'UTF-8'))        
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp
        
    def do_GET(self):
        url = self.path
        t = self.generate_sections_of_url(url)
        print(t)
        if reg.cek_user(url)==1:
            self.respond(200)
        else:
            self.no_respond(404)
        


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))


# In[ ]:




