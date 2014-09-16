import pymysql

#connect to database  #host is currently localhost  #default user/passwd    #database name 'bitcoin'
conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='', db='bitcoin', autocommit=True)
cur = conn.cursor()   #allows us to execute SQL code
print("Connected")

def storeTrades(price, amount, timestamp, exchangeID):
    print("STORE TRADE TIMES FOR: "+exchangeID)
    values = (exchangeID, price, amount, timestamp)     #store data into a single variable 'values'

                #we want to insert data into the table 'trades', in to these particular fields:
                #'trade_exchangeid', 'trade_price', 'trade_volume', 'trade_timestamp'.
    cur.execute("INSERT INTO trades (trade_exchangeid, trade_price, trade_volume, trade_timestamp) "
                "VALUES (%s, %s, %s, %s)", values)      #input the 4 values into SQL string

def getExchangeID(exchange):    #get the exchange_id of the provided exchange code
    cur.execute("SELECT exchange_id FROM exchanges "
                "WHERE exchange_name='"+exchange+"'")
    exchangeID = str(cur.fetchone())
    exchangeID = exchangeID.strip("(,)")                #cleaning up the returned data
    print("exchangeId: ", exchangeID)
    return exchangeID

def getLastTrade(exchangeID):
    print("GET LAST TRADE TIME FOR: "+exchangeID)
    cur.execute("SELECT trade_timestamp, trade_price, trade_volume FROM trades "    #select trade data
                "WHERE trade_exchangeid='"+exchangeID+"' "                          #from given exchangeID
                "ORDER BY trade_uid "                   #trades are ordered by timestamp before being stored so..
                "DESC LIMIT 1")                         #..the highest trade_uid is also the most recent timestamp

    trade = str(cur.fetchone())
    print("tradeBefore: ", trade)
    if trade != None:
        trade = trade.strip("(,)")                  #cleaning up the returned data
        trade = trade.split(", ")                   #split the results at every comma
    print("tradeAfter: ", trade)
    return trade

def getExchangeList():
    cur.execute("SELECT exchange_name FROM exchanges ") #get all exchange names from the table exchanges
    exchangeList = str(cur.fetchall())
    print("exchangeListBefore: ",exchangeList)
    if exchangeList != None:
        exchangeList = exchangeList.split(", ")               #split the results at every comma
        for i in range(len(exchangeList)):
            exchangeList[i] = exchangeList[i].strip("((',')") #cleaning up the returned data
    print("exchangeListAfter: ", exchangeList)
    return exchangeList

def updateExchangeList(exchangeName): #add another exchange code (i.e. zyadoEUR) to the exchanges table
    cur.execute("INSERT INTO exchanges(exchange_name) VALUES (%s)", exchangeName)



