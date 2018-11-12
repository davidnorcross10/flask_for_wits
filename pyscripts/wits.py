import re
import regex
from requests_html import HTMLSession
import time
import random
import sqlite3
import json
import matplotlib.pyplot as plt

session = HTMLSession()

def url_formatter(reporter,year,partner,product,indicator):
    base = "http://wits.worldbank.org/API/V1/SDMX/V21/datasource/tradestats-trade/"
    reporter = "reporter/{}/".format(reporter)
    year = "year/{}/".format(year)
    partner = "partner/{}/".format(partner)
    product = "product/{}/".format(product)
    indicator = "indicator/{}/".format(indicator)
    url = base + reporter + year + partner + product + indicator + "?format=JSON"
    sessionData = session.get(url)
    data = json.loads(sessionData.html.full_text)
    return data, url

#data = url_formatter("usa","2000","wld","all","XPRT-TRD-VL")
'''for i in data:
    print(i)
    print(data[i])
    print("")'''
#print(len(data["dataSets"][0]['series']))
def get_observations(data):
    keys = []
    values = []
    for i in data["dataSets"][0]['series']:
        values.append(data["dataSets"][0]['series'][i]['observations']['0'][0])
    for i in data["structure"]["dimensions"]['series'][3]['values']:
        keys.append(i['name'])
    for i in data['structure']['dimensions']['series']:
        print(i)
        #print(data["structure"]["dimensions"][i])
        print('')
    #print(len(data['structure']['dimensions']['series']))
    observation_dict = dict(zip(keys,values))

    return observation_dict

def returnJSON(path):
    fileString = open(path).read()
    fileJSON = json.loads(fileString)
    return(fileJSON)

#print(returnJSON('/home/david/Documents/Flask_test/static/country_codes_json.txt'))

'''for i in data["structure"]["dimensions"]:
    print(i)
    print(data["structure"]["dimensions"][i])
    print('')'''
#print(len(data["structure"]["dimensions"]['observation']))
#print(len(data["structure"]["dimensions"]['series']))
'''print(get_observations(data))'''
    #print(data["structure"]["dimensions"]['series'][0][i])
    #print('')
#print(data["dataSets"][0]['series'])
