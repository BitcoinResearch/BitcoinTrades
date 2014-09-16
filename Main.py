# #REQUIREMENTS: [download XAMPP to run this locally, then run Apache, MySQL, and go to http://localhost/phpmyadmin]
# MySQL database -> database called 'bitcoin', tables called: 'exchanges', 'trades'
#'exchanges' fields: exchange_id (type: int, autoincrement, primary, unique)
#                    exchange_name (type: text, primary, unique)
#'trades' fields: trade_UID (type: bigint, autoincrement, primary)
#                 trade_exchangeID (type: int)
#                 trade_timestamp (type: int)
#                 trade_price (type: double)
#                 trade_volume (type: double)
#Can now run this program.
#If you're unsure what a variable or function is doing..
#..the best thing is to print it out after it occurs, e.g.: print(someVariable)

import BitcoinCharts  #BitcoinCharts.py
import Database  #Database.py
import time
import QuandlData

btcCharts = BitcoinCharts  #btcCharts = shortened variable name referring to BitcoinCharts.py
db = Database  #db = shortened variable name referring to Database.py
SLEEP = 30  #add a sleep delay in seconds

#List of exchanges and their currencies, listed as Bitcoinchart codes.
#Add additional Bitcoinchart codes as you wish - it won't break anything. (EUR, USD, GBP only)
exchanges = ["1coinUSD", "anxhkUSD", "anxhkEUR", "anxhkGBP", "bitbayUSD", "bitbayEUR", "btcdeEUR", "bitcurexEUR",
			 "bitfloorUSD", "bitfinexUSD", "bitstampUSD", "btceUSD", "btceEUR", "coinfloorGBP", "cotrUSD", "hitbtcUSD",
			 "hitbtcEUR", "itbitUSD", "itbitEUR", "krakenUSD", "krakenEUR", "lakeUSD", "localbtcUSD", "localbtcEUR",
			 "localbtcGBP", "rippleUSD", "rippleEUR", "zyadoEUR"]

#Program starts here
if __name__ == "__main__":
	print("Starting main")

    exchangeList = db.getExchangeList()         #get list of exchanges currently in database
    for x in range(len(exchanges)):
        if(exchanges[x] not in exchangeList):   #compare list of database exchanges to exchanges we have listed above
            print("Adding: ", exchanges[x])
            db.updateExchangeList(exchanges[x]) #if there's a new exchange listed above, add it to the database as well

    while True:
        for i in range(len(exchanges)):
            btcCharts.BitcoinCharts.BitcoinChartsData(exchanges[i])
            print("EXECUTING:", exchanges[i])
        print("SLEEPING "+str(SLEEP)+" SECONDS")
        time.sleep(SLEEP)
