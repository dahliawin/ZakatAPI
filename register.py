#!/usr/bin/env python
# coding: utf-8

# In[54]:


import mysql.connector
import secrets
import string
import urllib

def db_connection():
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user_db",
        )
    return db_conn
    
def generate_sections_of_url(url):
        path = urllib.parse.urlsplit(url).path
        print(path)
        sections = urllib.parse.parse_qs(path)
        return sections

def generate_token():
        alphabet = string.ascii_letters + string.digits 
        token = ''.join(secrets.choice(alphabet) for i in range(10))
        return token

def input_user(url):
        db_conn = db_connection()
        cursor = db_conn.cursor()
        t = generate_sections_of_url(url)
        name = t['/register/user'][0]
        password = t['password'][0]
        token = generate_token()
        values = (name, password, token)
        query = "INSERT INTO user (name, password, token) VALUES (%s, %s, %s)"
        cursor.execute(query, values)
        db_conn.commit()
        print(values)
        print(cursor.rowcount, "record inserted")
        return token

def cek_user(url):
        db_conn = db_connection()
        cursor = db_conn.cursor(buffered=True)
        t = generate_sections_of_url(url)
        key = t['key'][0]
        exist = 0
        query = "SELECT * FROM user WHERE token = %s"
        value = (key, )
        cursor.execute(query, value)
        result = cursor.fetchall()
        db_conn.commit()
        arr = {}
        for x in result:
            arr = x
        if len(arr) != 0:
            exist = 1
        else:
            exist = 0
        return exist

    






