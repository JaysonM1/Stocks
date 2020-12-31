from pandas_datareader import data
import pandas as pd
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta
import os
import glob


def getTicks():
    date_list = [(date.today() + relativedelta(days=-x)) for x in range(7)]
    ticks = [None] * 7
    i = 6
    for x in date_list:
        ticks[i] = x.strftime('%m/%d')
        i= i - 1
    return ticks



today = date.today()
twoYearsAgo = date.today() + relativedelta(years=-1)
currentDate = today.strftime("%Y/%m/%d")
twoYears = twoYearsAgo.strftime("%Y/%m/%d")
indexes = [["^dji", "Dow Jones"],['^ixic','NASDAQ'],['^rut',"Russell 2000"], ['^gspc',"S&P 500"]]


def makeGraph(prices, stock,file):
    plt.figure()
    plt.title(stock, loc = 'center')
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close")
    plt.plot(prices)
    plt.savefig(file + stock.replace(".",""))
    
    
def graphIndexes():
  graphs =[]
  for index in indexes:
        prices = data.DataReader(index[0], start = twoYears, end = currentDate, data_source = "yahoo")['Adj Close']

        # all_weekdays = pd.date_range(start=currentDate, end=oneWeekAgo, freq='B')
        # prices = prices.reindex(all_weekdays)
        # prices = prices.fillna(method='ffill')

        graphs.append(makeGraph(prices, index[1],"indexes/"))
  return graphs

def makeList(stocks):
    s = 0
    top3 = []
    for i in range(3):
        row = []
        for j in range(1):
            row.append(stocks.iloc[s].Symbol)
            row.append(stocks.iloc[s].Name)
        top3.append(row)
        s += 1
    return top3
def getGainers():
    gainers = pd.read_html('https://finance.yahoo.com/gainers')
    gainers = gainers[0]
    return makeList(gainers)

def graphGainers(topGainers):
    gainers = []
    files = glob.glob('gainers/*.png')
    for f in files:
        os.remove(f)
    for gainer in topGainers:
        prices = data.DataReader(gainer[0], start= twoYears, end= currentDate, data_source='yahoo')['Adj Close']
        gainers.append(makeGraph(prices, gainer[1],"gainers/"))
    return gainers
    
def getLosers():
    losers = pd.read_html('https://finance.yahoo.com/losers')
    losers = losers[0]
    return makeList(losers)
    

def graphLosers(topLosers):
    losers = []
    files = glob.glob('losers/*.png')
    for f in files:
        os.remove(f)
    for loser in topLosers:
        prices = data.DataReader(loser[0], start= twoYears, end= currentDate, data_source='yahoo')['Adj Close']
        losers.append(makeGraph(prices, loser[1],"losers/"))
    return losers
def run():
    graphIndexes()
    graphGainers(getGainers())
    graphLosers(getLosers())
    
