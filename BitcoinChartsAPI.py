__author__ = 'Sam'

import requests

global allTrades
URL = "http://api.bitcoincharts.com/v1/trades.csv?symbol="              #BitcoinCharts API URL

def getTradesSince(time, exchange):
    print("GET TRADES SINCE: "+str(time)+" FOR: "+exchange)
    print("time: ", time)
    print("URL: ", URL+str(exchange)+"&start="+str(time))

    response = requests.get(URL+str(exchange)+"&start="+str(time))  #enter the exchange code and timestamp into API URL
    data = response.text                                  #get the response as a String
    csvstr = str(data).strip("b'")                        #clean up the response
    lines = csvstr.split("\\n")                           #more cleaning. save in variable called 'lines'

    allTrades = []
    for line in lines:
        allTrades.append(line)                            #for each line of data, save it to a list 'allTrades'

    return allTrades











