#/usr/bin/env python
import json
import urllib
import requests

def get_data():
    equity = "MSFT"
    apikey = "G6KNFJ4HI00PG3XZ"
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=compact&apikey={}".format(equity, apikey)
    req = urllib.request.Request(url)
    reader = urllib.request.urlopen(req).read()

    counter1 = 3
    counter2 = 5
    output_data = {}

    output = reader.decode()
    output = output.split('"')
    while counter2 < 22:
        output_data.update({output[counter1] : output[counter2]})
    
    for item in output_data:
        print(item)

if __name__ == "__main__":
    get_data()