import json
import os
import pprint

addr = raw_input("Enter a BTC Address: ")

os.system("clear")
print("Updating Data...")
os.system("curl -o .addrdata.json -s http://blockchain.info/address/" + addr + "?format=json")
os.system("curl -o .currency.json -s http://blockchain.info/ticker")
os.system("clear")
a = open(".addrdata.json")
b = json.load(a)
c = open(".currency.json")
d = json.load(c)

balance = float(b['final_balance']) / 10**8
usd_currency = float(d['USD']['15m'])
usd_balance = "{0:.2f}".format(usd_currency * balance)
eur_currency = float(d['EUR']['15m'])
eur_balance = "{0:.2f}".format(eur_currency * balance)

print("Address: " + str(addr))
print("Balance: " + str(balance) + " ** $" + str(usd_balance) + " ** " + str(eur_balance) + " EUR")
print("Number of Transactions: " + str(b['n_tx']))
print("Total amount received: " + str(float(b['total_received'])/10**8) + " BTC")
print("Total amount sent: " + str(float(b['total_sent'])/10**8) + " BTC")