### INF601 - Advanced Programming in Python
### Cole Darling
### Mini Project 1
import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "META", "GME", "AMC"]

mydata={}

mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker: ticker,'
                      'dailyHigh': result.info['dailyHigh'],}
pprint.pprint(mydata)




# get historical market data
#hist = msft.history(period="1mo")

#pprint.pprint(hist)