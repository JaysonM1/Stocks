# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 03:24:27 2020

@author: jayson
"""

# Using plotly.express
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"
from plotly.offline import plot
from pandas_datareader import data
from datetime import date
from dateutil.relativedelta import relativedelta
import chart_studio
chart_studio.tools.set_credentials_file(username = 'jaysonm1', api_key ='f0PQQCZMf2S9To6Tt3yc')
import chart_studio.plotly as py
import chart_studio.tools as tls
import pandas as pd


today = date.today()
oneYears = date.today() + relativedelta(weeks=-8)
currentDate = today.strftime("%Y/%m/%d")
oneYears = oneYears.strftime("%Y/%m/%d")

def makeIndexGraphs(df, stockInfo):
    figure = go.Figure(
            data = [
                go.Candlestick(
                    x = df.index,
                    low = df['Low'],
                    high = df['High'],
                    close = df['Adj Close'],    
                    open = df['Open'],
                    increasing_line_color = 'green',
                    decreasing_line_color = 'red')])
    figure.update_layout(
            title = stockInfo[1],
            yaxis_title = 'Price $',
            xaxis_title = 'Date')
    temp = py.plot(figure, filename= stockInfo[1],auto_open = False)
    
def makeGraph(df, loc, name):
     figure = go.Figure(
            data = [
                go.Candlestick(
                    x = df.index,
                    low = df['Low'],
                    high = df['High'],
                    close = df['Adj Close'],    
                    open = df['Open'],
                    increasing_line_color = 'green',
                    decreasing_line_color = 'red')])
     figure.update_layout(
            title = name,
            yaxis_title = 'Price $',
            xaxis_title = 'Date')
     print(loc)
     temp = py.plot(figure, filename= loc,auto_open = True)



ind = [["^dji", "Dow Jones"],['^ixic','NASDAQ'],['^rut',"Russell 2000"], ['^gspc',"S&P 500"]]
def graphIndexes():
    indexes = []
    for i in ind:
        df = data.DataReader(i[0], start = oneYears, end = currentDate, data_source = "yahoo")
        makeIndexGraphs(df, i)
    return indexes



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

def graphGainers():
    gainers = getGainers()
    location = ["Gainer1", "Gainer2", "Gainer3"]
    i = 0
    for gainer in gainers:
        df = data.DataReader(gainer[0], start= oneYears, end= currentDate, data_source='yahoo')
        makeGraph(df, location[i], gainer[1])
        i = i + 1
        
def getLosers():
    losers = pd.read_html('https://finance.yahoo.com/losers')
    losers = losers[0]
    return makeList(losers)     
def graphLosers():
    losers = getLosers()
    location = ["Loser1", "Loser2", "Loser3"]
    i = 0
    for loser in losers:
        df = data.DataReader(loser[0], start= oneYears, end= currentDate, data_source='yahoo')
        makeGraph(df, location[i], loser[1])
        i = i +1
def run():
    graphLosers()
    graphGainers()
    graphIndexes()




