__author__ = 'Sam'

import BitcoinChartsAPI
import Database
import time
from operator import itemgetter

db = Database
api = BitcoinChartsAPI
SLEEP = 0 #seconds

class BitcoinCharts():

    def BitcoinChartsData(self, thisExchange):          #'thisExchange' is the 'exchangeCode' we've passed to this method

        print("RUNNING: ", thisExchange)                #compare this exchange code to the exchange codes in the..
        exchangeID = db.getExchangeID(thisExchange)     #..database and get the corresponding exchange ID
        lastTrade = db.getLastTrade(exchangeID)         #get the most recent trade stored for that exchange
        print(lastTrade[0])
        if lastTrade[0] == "None":                      #if there is no trade data, initialise variables to 0
            lastTime = 0
            lastPrice = 0
            lastAmount = 0
        else:                                           #else, store the recent trade data into the 3 variables
            lastTime = int(lastTrade[0])
            lastPrice = float(lastTrade[1])             #float means a number with a decimal place
            lastAmount = float(lastTrade[2])

        newTrades = api.getTradesSince(lastTime, thisExchange) #use the timestamp we retrieved from the most..
        print("newTrades: ",newTrades)                         #..recent trade and retrieve all trade data since then
        if newTrades != ['']:                                #if the returned trade data isn't empty, continue
            tradeList = sorted(newTrades, key=itemgetter(0)) #sort by timestamp
            for i in range(len(tradeList)):
                parsedTrade = tradeList[i].split("\n")              #split by line
                for x in range (len(parsedTrade)):
                    parsedTrade2 = parsedTrade[x].split(",")        #seperate element in each line at every comma
                    timestamp = int(parsedTrade2[0])                #store this trade's timestamp
                    price = float(parsedTrade2[1])                  #store this trade's price
                    amount = float(parsedTrade2[2])                 #store this trade's amount
                    if timestamp == lastTime and price == lastPrice and amount == lastAmount:
                        print(thisExchange+" SAME ENTRY")           #if timestamp AND price AND amount are the same..
                                                                    #..then don't save anything to database (duplicate)
                        print(thisExchange+": (timestamp: "+str(timestamp)+" lastTime: "+str(lastTime)+") (price: "+str(price)+" lastPrice: "+str(lastPrice)+") (amount: "+str(amount)+" lastAmount: "+str(lastAmount)+")")
                    else:
                        db.storeTrades(price, amount, timestamp, exchangeID)   #if not the same, save to database
                        print(thisExchange+" Saved: ", parsedTrade2)
                        print(thisExchange+": (timestamp: "+str(timestamp)+" lastTime: "+str(lastTime)+") (price: "+str(price)+" lastPrice: "+str(lastPrice)+") (amount: "+str(amount)+" lastAmount: "+str(lastAmount)+")")
            print(thisExchange+" FINISHED")
            time.sleep(SLEEP)
        else:
            print(thisExchange+" HAS NO DATA AVAILABLE")     #if the returned trade data was empty, print this
                                                             #usually because of a BitcoinCharts.com error
