# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:23:32 2021

@author: 12533
"""

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time 


#extracting data for a single ticker
ts = TimeSeries(key='70SOSIDGCGON6PCF', output_format='pandas')
data=ts.get_daily(symbol='MSFT', outputsize='full')[0]
data.columns=['open', 'high', 'low', 'close', 'volume']
data=data.iloc[::-1]

#extracting stock data (historical close price) for the stocks identified
all_tickers=['AAPL', 'MSFT', 'CSCO', 'AMZN', 'GOOG', 'FB']
close_prices=pd.DataFrame()
api_call_count=0
start_time=time.time()
for ticker in all_tickers:
    starttime=time.time()
    ts=TimeSeries(key='70SOSIDGCGON6PCF', output_format='pandas')
    api_call_count+=1
    data=ts.get_intraday(symbol=ticker, interval='1min', outputsize='full')[0]
    data.columns=["open", 'high', 'low', 'close', 'volume']
    close_prices[ticker]=data['close']
    if api_call_count==5:
        api_call_count=0
        time.sleep(60-(time.time()-start_time))
        
    
    
    
    

    
     
    
 
    
    
    

    








