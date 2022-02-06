#!/usr/bin/python
# Run as: ./price2.py USDT EUR 2022-01-20 13:05
# + Info: https://www.coinapi.io
import requests, sys, datetime

url = 'https://rest.coinapi.io/v1/exchangerate/$1/$2/history?period_id=1MIN&time_start=$3T$4:00&time_end=$3T$4:59'

def par(coin_from, coin_to, date, time):
    url_api = url.replace('$1', coin_from).replace('$2', coin_to).replace('$3', date).replace('$4', time)
    headers = {'X-CoinAPI-Key' : '<your_api_key_from_coinapi.io_here>'}
    
    data = requests.get(url_api, headers=headers).json()
    return(data[0]['rate_close'])

print(par(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
