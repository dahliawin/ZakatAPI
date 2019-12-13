#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from requests.models import PreparedRequest
import requests
import json
import urllib.parse
import os.path
import time
import register as reg

HOST_NAME = 'zakatapi.org'
#PORT_NUMBER = 9000

class MyHandler(BaseHTTPRequestHandler):
    
    def generate_sections_of_url(self, url):
        path = urllib.parse.urlsplit(url).path
        print(path)
        sections = urllib.parse.parse_qs(path)
        return sections
        
    def respond_reg(self, status_code, name, token):
        print(status_code, token)
        self.send_response(status_code)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        content = {
            'username': name,
            'password': 'xxxxxx',
            'key': token
        }
        self.wfile.write(json.dumps(content).encode())
        
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
        self.t = self.generate_sections_of_url(url)
        print(self.t)
        if self.t['/register/user'] != "" :
            name = self.t['/register/user'][0]
            token = reg.input_user(url)
            self.respond_reg(200, name, token)
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




