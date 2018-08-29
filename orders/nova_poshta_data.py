# -*- coding: UTF-8 -*-
import requests
import datetime

api_key = "44af01e2069a132543ab95299cb4ea7d"
url = "https://api.novaposhta.ua/v2.0/json/"
headers = {'content-type': 'application/json'}

default_cities = ["Харьков", "Киев"]


class HashInfo(object):
    current_date = None
    cities = default_cities

hash = HashInfo()

def get_cities():
    data = "{\r\n\"apiKey\": \"44af01e2069a132543ab95299cb4ea7d\",\r\n \"modelName\": \"Address\",\r\n \"calledMethod\": \"getCities\"}"
    if hash.current_date is None or datetime.datetime.now() - datetime.timedelta(days=7) > hash.current_date:
        req = requests.post(url, headers=headers, data=data, verify=False)
        if req.status_code == 200:
            req_json = req.json()
            if req_json["success"]:
                cities = [city["DescriptionRu"] for city in req_json["data"]]
                hash.cities = cities
    return hash.cities

