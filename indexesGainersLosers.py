from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta
def getTicks():
    date_list = [(date.today() + relativedelta(days=-x)) for x in range(9)]
    ticks = [None] * 9
    i = 8
    for x in date_list:
        ticks[i] = x.strftime('%m/%d')
        i= i - 1
    return ticks

def graphIndexes(indexes, currentDate, oneWeekAgo):
    for index in indexes:
        prices = data.DataReader(index[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Adj Close']
        volume = data.DataReader(index[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Volume']
        plt.figure()
        plt.title(index[1], loc = 'center')
        plt.xlabel("Date")
        plt.ylabel("Adjusted Close")
        plt.plot(prices)
        #plt.plot(volume)
        plt.show()

def getGainers():
    gainers = pd.read_html('https://finance.yahoo.com/gainers')
    gainers = gainers[0]
    s = 0
    topGainers = []
    for i in range(3):
        row = []
        for j in range(1):
            row.append(gainers.iloc[s].Symbol)
            row.append(gainers.iloc[s].Name)
        topGainers.append(row)
        s += 1
    return topGainers

def graphGainers(topGainers,currentDate,oneWeekAgo):
    for gainer in topGainers:
        prices = data.DataReader(gainer[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Adj Close']
        volume = data.DataReader(gainer[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Volume']
        plt.figure()
        plt.title(gainer[1], loc = 'center')
        plt.xlabel("Date")
        plt.ylabel("Adjusted Close")
        plt.plot(prices)
        #plt.plot(volume)
        plt.show()
    
    
def getLosers():
    losers = pd.read_html('https://finance.yahoo.com/losers')
    losers = losers[0]
    s = 0
    topLosers = []
    for i in range(3):
        row = []
        for j in range(1):
            row.append(losers.iloc[s].Symbol)
            row.append(losers.iloc[s].Name)
        topLosers.append(row)
        s += 1
    return topLosers
    

def graphLosers(topLosers,currentDate,oneWeekAgo):
    print(topLosers)
    for loser in topLosers:
        prices = data.DataReader(loser[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Adj Close']
        #volume = data.DataReader(loser[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Volume']
        plt.figure()
        plt.title(loser[1], loc = 'center')
        plt.xlabel("Date")
        plt.ylabel("Adjusted Close")
        plt.plot(prices)
        #plt.plot(volume)
        plt.show()
    
    
    
def main():
    today = date.today()
    oneWeek = date.today() + relativedelta(weeks=-1)
    currentDate = today.strftime("%Y/%m/%d")
    oneWeekAgo = oneWeek.strftime("%Y/%m/%d")
    indexes = [["^dji", "Dow Jones"],['^ixic','NASDAQ'],['^rut',"Russell 2000"], ['^gspc',"S&P 500"]]
    graphIndexes(indexes,currentDate,oneWeekAgo)
    
    graphGainers(getGainers(),currentDate,oneWeekAgo)
    
    graphLosers(getLosers(), currentDate, oneWeekAgo)  
    

if __name__ == "__main__":
    main()