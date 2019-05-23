import pandas as pd
import numpy as np
import pandas_datareader.data as web
import requests
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

portfolio = 1e5
tscost = 0.05
nstocks = 0

tickers = ['BHEL.NS', 'ITC.NS', 'LUPIN.NS', 'RELIANCE.NS' ]

for ticker in tickers:
    nstocks+=1

def readData(ticker, n):
    stocks.append(web.DataReader(ticker , 'yahoo', start='1/1/2015'))
def macd(df1):
    short_ma=26
    long_ma=12
    signal_ma=9
    df1['rolling_ema_short']=df1['Adj Close'].ewm(span=short_ma, min_periods=short_ma).mean()
    df1['rolling_ema_long']=df1['Adj Close'].ewm(span=long_ma, min_periods=long_ma).mean()
    df1['macd']=df1['rolling_ema_long']-df1['rolling_ema_short']
    df1['rolling_ema_signal']=df1['macd'].ewm(span=signal_ma, min_periods=signal_ma).mean()

    df1['position']=0
    df1['zeros']=0
    df1.dropna(inplace=True)
    df1['macd_histogram']=df1['macd']-df1['rolling_ema_signal']
    ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
    # ax2 = plt.subplot2grid((6,1), (5,0), rowspan =5, colspan =1, sharex=ax1)

    ax1.xaxis_date()

    ax1.plot(df1[['macd','rolling_ema_signal','zeros']])
    # ax2.hist(df1['macd_histogram'],bins=1000)
    plt.title('Graph of MACD')
    plt.legend({'MACD','signal line',},loc='upper left')
    plt.show()

def macd_stratergy(df1):
    for row in range(len(df1)):
        if(df1['position'].iloc[row-1]==0):
            pass

i=0
stocks = []
for ticker in tickers[:1]:
    readData(ticker,i)
    macd(stocks[i])
    # print(stocks[i])


