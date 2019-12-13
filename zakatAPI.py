#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
    params = {}
    tipe = ""
    num1 = 0
    zakat = 0
    nisab = 0
    t = []
    
    with open("db.json") as data_file:
        data = json.load(data_file)
    
    def generate_sections_of_url(self, url):
        path = urllib.parse.urlsplit(url).path
        print(path)
        sections = urllib.parse.parse_qs(path)
        return sections
    
    def handle_http(self, status_code, zakat, tipe):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        content = {
            'jenis': tipe,
            'nisab': self.nisab,
            'zakat': zakat
        }
        self.wfile.write(json.dumps(content).encode())

    def respond(self, status_code, tipe):
        print(status_code, tipe)
        response = self.handle_http(status_code, self.zakat, tipe)
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
    
    def penghasilan(self, num1, num2): 
        self.nisab = 520*12500
        if (num1-num2)*12 >= self.nisab:
            self.zakat = (num1-num2)*2.5/100
        else:
            self.zakat = 0
        return self.respond(200, "Zakat penghasilan") 
        

    def maal(self, num1): 
        self.nisab = 85*658774
        if (num1>=self.nisab):
            self.zakat = num1*2.5/100   
        else:
            self.zakat = 0
        return self.respond(200, "Zakat maal")                     
    
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
        if reg.cek_user(url)==1:
            self.tipe = self.t['/zakat'][0]
            self.pilih(self.tipe)
        else:
            self.no_respond(404)
        
    def pilih(self, tipe):
        if tipe == 'maal':
            x = self.t['harta'][0]
            num1 = float(x)
            print(num1)
            self.maal(num1)
        elif tipe == 'penghasilan':
            x = self.t['pendapatan'][0]
            num1 = float(x)
            y = self.t['pengeluaran'][0]
            num2 = float(y)
            print(num2)
            self.penghasilan(num1,num2) 
        elif tipe == 'lokasi':
            self.respond('lokasi')
        else:
            print(404)


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




