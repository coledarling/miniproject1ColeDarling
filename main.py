### INF601 - Advanced Programming in Python
### Cole Darling
### Mini Project 1
import pprint
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import copy
import os

os.makedirs("charts", exist_ok=True)

mytickers = ["MSFT", "AAPL", "META", "GME", "AMC"]

mydata={}

mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(period="10d")
    last10days = []
    for date in hist['Close']:
        last10days.append(date)
    if len(last10days) == 10:
        #maxlist = copy.copy(last10days)
        #maxlist.sort()
        #max_price = maxlist[-1]+10
        #min_price = maxlist[0]-10
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")

# get historical market data
#hist = msft.history(period="1mo")

#pprint.pprint(hist)