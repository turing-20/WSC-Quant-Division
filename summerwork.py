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

stock_list = ['BHEL.NS', 'ITC.NS', 'LUPIN.NS', 'RELIANCE.NS' ]

for stock in stock_list:
    nstocks+=1

def readData(ticker, n):
    stocks.append(web.DataReader(ticker , 'yahoo', start='1/1/2015'))

i=0
stocks = []
for ticker in stock_list:
    readData(ticker,i)


