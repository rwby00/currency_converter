# write your code here!
import requests
import json

currency_exchange = input()
url = f'http://www.floatrates.com/daily/{currency_exchange.lower()}.json'
request = requests.get(url).json()
cache = {}

if currency_exchange.lower() != 'usd':
    cache['usd'] = float(request['usd']['rate'])
if currency_exchange.lower() != 'eur':
    cache['eur'] = float(request['eur']['rate'])

while True:
    currency_receive = input()
    if currency_receive == '':
        exit()
    money = float(input())
    print('Checking the cache...')
    rate = float(request[currency_receive.lower()]['rate'])
    if currency_receive.lower() in cache.keys():
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache[currency_receive.lower()] = rate

    outcome = round(money * rate, 2)
    print(f'You received {outcome} {currency_receive.upper()}.')
