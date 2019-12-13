#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import json
import time
import csv

class GooglePlaces(object):
    name = ""
    address = ""
    website = ""
    phone_number = ""
    
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey
        
    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places
    
    def search_places_by_query(self, query):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        places = []
        params = {
            'query': query,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details
    
    def get_nameplace_details(self, keyword, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/keyword/details/json"
        params = {
            'keyword':keyword,
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details
    
    def get_lokasi():
        api = GooglePlaces("AIzaSyCTaCzFlmJen9R3JUx5vl1UGzTVa4MVHO4")
        places = api.search_places_by_query("Zakat")
        fields = ['name', 'formatted_address', 'international_phone_number', 'website']
        alist = []
        for place in places: 
            details = api.get_place_details(place['place_id'], fields) 
            try:
                name = details['result']['name']
            except KeyError:
                name = ""
            try:
                address = details['result']['formatted_address']
            except KeyError:
                address = ""
            try:
                website = details['result']['website']
            except KeyError:
                website = ""
            try:
                phone_number = details['result']['international_phone_number']
            except KeyError:
                phone_number = ""
            data = {'name': name, 'address': address, 'website': website, 'phone_number': phone_number}
            if data['name'] != "":
                alist.append(data)

        clist = {'Alamat':alist}
        return clist
        


# In[ ]:




