from pandas_datareader import data
import matplotlib
matplotlib.use("agg")
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
today = date.today()
oneWeek = date.today() + relativedelta(weeks=-1)
currentDate = today.strftime("%Y/%m/%d")
oneWeekAgo = oneWeek.strftime("%Y/%m/%d")
indexes = [["^dji", "Dow Jones"],['^ixic','NASDAQ'],['^rut',"Russell 2000"], ['^gspc',"S&P 500"]]


def makeGraph(prices, stock):
    plt.figure()
    plt.title(stock, loc = 'center')
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close")
    plt.plot(prices)
    plt.savefig("indexes/"+stock)
    
    
def graphIndexes():
  graphs =[]
  for index in indexes:
        prices = data.DataReader(index[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Adj Close']
        volume = data.DataReader(index[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Volume']
        graphs.append(makeGraph(prices, index[1]))
  

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
    for gainer in topGainers:
        prices = data.DataReader(gainer[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Adj Close']
        volume = data.DataReader(gainer[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Volume']
        makeGraph(prices, gainer[1])
    
def getLosers():
    losers = pd.read_html('https://finance.yahoo.com/losers')
    losers = losers[0]
    return makeList(losers)
    

def graphLosers(topLosers,currentDate,oneWeekAgo):
    for loser in topLosers:
        prices = data.DataReader(loser[0], start= oneWeekAgo, end= currentDate, data_source='yahoo')['Adj Close']
        makeGraph(prices, loser[1])
    
def main():
    indexes = [["^dji", "Dow Jones"],['^ixic','NASDAQ'],['^rut',"Russell 2000"], ['^gspc',"S&P 500"]]
    for index in graphIndexes():
        plt.show()
    
    #graphGainers(getGainers(),currentDate,oneWeekAgo)
    
    #graphLosers(getLosers(), currentDate, oneWeekAgo)  
    

if __name__ == "__main__":
    main()