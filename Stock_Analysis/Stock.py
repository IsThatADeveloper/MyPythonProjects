import yfinance as yf
import pandas as pd
import datetime as dt

stock = yf.Ticker('NIO')
stockname = stock.info['shortName'].replace(' ', '_').replace(".", "")
# print('Stock_Analysis/' + stockname + '_History.csv')

hist = stock.history(period='12mo')
# print(hist)

stock.dividends
stock.splits

hist.to_csv('Stock_Analysis/' + stockname + '_History.csv', index=True)

# tt = dt.date.today()
# print(time)


# data = yf.download("SPY AAPL", period="1mo") #data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
# data


# msft.actions
# msft.splits
# msft.capital_gains  # only for mutual funds & etfs
