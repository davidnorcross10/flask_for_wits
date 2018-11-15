import re
import regex
from requests_html import HTMLSession
import time
import random
import sqlite3
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

session = HTMLSession()
base_path = '/home/david/Documents/COMTRADE/'
Turkey_tomato_path = base_path + 'EU_Turkey_Tomato_Imports_2008_2012.csv'
Turkey_total_path = base_path + 'EU_Turkey_Total_Imports_2008_2012.csv'
Morocco_tomato_path = base_path + 'EU_Morocco_Tomato_Imports_2008_2012.csv'
Morocco_total_path = base_path + 'EU_Morocco_Total_Imports_2008_2012.csv'

def calculate_RCA(years,XiB_path,XB_path,XiA_path,XA_path):
    trade_value_H3 = "Trade Value (US$)"
    trade_value_H4 = "CIF Trade Value (US$)"

    XiB_df = pd.read_csv(XiB_path)
    XB_df = pd.read_csv(XB_path)
    XiA_df = pd.read_csv(XiA_path)
    XA_df = pd.read_csv(XA_path)

    XiB = trade_value_dict(years,XiB_df)
    XB = trade_value_dict(years,XB_df)
    XiA = trade_value_dict(years,XiA_df)
    XA = trade_value_dict(years,XA_df)

    RCA = {}

    for year in years:
        RCA[year] = np.log((XiB[year]/XB[year])/(XiA[year]/XA[year]))
    print(RCA)

def trade_value_dict(years,df):
    trade_value_H3 = "Trade Value (US$)"
    trade_value_H4 = "CIF Trade Value (US$)"

    value_dict = {}

    for year in years:
        if df[df["Year"]==year][trade_value_H3].values[0] >= 0:
            value_dict[year] = df[df["Year"]==year][trade_value_H3].values[0]
        else:
            value_dict[year] = df[df["Year"]==year][trade_value_H4].values[0]

    return value_dict

years = list(range(2008,2013))
calculate_RCA(years,Turkey_tomato_path,Turkey_total_path,Morocco_tomato_path,Morocco_total_path)

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
