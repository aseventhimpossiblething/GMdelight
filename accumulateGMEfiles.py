
"""
 
Your dedicated access key is: 70YMNXM4BZWGEGOA
Please record this API key at a safe place for future data access.
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=demo

"""
# all IEX supported symbols https://cloud.iexapis.com/beta/ref-data/symbols?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
# working example 1 quote current price https://cloud.iexapis.com/stable/stock/XOM/quote?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
#zetapk_2a5af8857a7940d4b361bc2b4a14d0adf 
#zetask_20d88bd4d61b4e92b2ae7b22d8f8f0aef
#https://cloud.iexapis.com/stable/
#https://cloud.iexapis.com/v1/
#zeta/stock/{symbol}/batch
#https://cloud.iexapis.com/stable/stock/aapl/batch?types=quote,news,chart&range=1m&last=10
"""
https://cloud.iexapis.com/stable/stock/aapl/batch?types=quote,news,chart&range=1m&last=10?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf 
https://cloud.iexapis.com/stable/stock/IBM/batch
https://cloud.iexapis.com/stable/stock/market/batch?symbols=aapl,fb&types=quote,news,chart&range=1m&last=5
https://cloud.iexapis.com/stable/stock/market/batch?symbols=aapl,fb&types=quote&range=1m&last=5
#pip install iex-api-python 
"""
 

import requests
import os
from datetime import datetime
import pandas


#print(os.getcwd())
#print(os.listdir())

def pullNasdaqAbbreves():
    os.chdir('Sheets/rememberGME/NasdaqAbbreviations');
    mglob=str(os.listdir());
    ActivendqAdd=mglob.find("ActivendqAbbrev");
    if ActivendqAdd>-1:
       os.system('rm ActivendqAbbrev');
    
    nasdaqNativeAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"   
    nasdaqAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
    filedate=str(datetime.now().date())
    
    ndqNativeAbbrecords=str('curl '+nasdaqNativeAbbreviations+' -o nasdaqNativeAbbreviations-'+filedate)
    ActNativendqAbbrv=str('curl '+nasdaqNativeAbbreviations+' -o ActiveNativendqAbbrev')
    
    ndqAbbrecords=str('curl '+nasdaqAbbreviations+' -o nasdaqAbbreviations-'+filedate)
    ActndqAbbrv=str('curl '+nasdaqAbbreviations+' -o ActivendqAbbrev')
    
    os.system(ndqNativeAbbrecords)
    os.system(ActNativendqAbbrv)
    os.system(ndqAbbrecords)
    os.system(ActndqAbbrv)
    
    print("accumilateGMEfiles ran")
    print("accumilateGMEfiles ran")
"""    
pullNasdaqAbbreves();
NasdaqNativeAbbreviations=pandas.read_csv('ActiveNativendqAbbrev','|');
NasdaqAbbreviations=pandas.read_csv('ActivendqAbbrev','|');


print(NasdaqAbbreviations)
print(NasdaqNativeAbbreviations)
print(os.getcwd())
print(str(os.listdir())
"""

#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=70YMNXM4BZWGEGOA"

#AlphaVantageAbbreviations="https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=70YMNXM4BZWGEGOA"

#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbol=AMD&apikey=70YMNXM4BZWGEGOA"
#response1=requests.get(AlphaVantageEndPoint)
#response2=requests.get(AlphaVantageAbbreviations)
#print(response1.json())
#print(response2.json())



chartiexdata="https://cloud.iexapis.com/stable/stock/XOM/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"


#https://sandbox.iexapis.com/stable/stock/AMD/dividends/1y?token=Tpk_ae999384a70348b3855e8904d4c46e5e

#https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e
expChart=requests.get(chartiexdata)
print(expChart)
print(expChart.json()[0])
print("-------------------")
print(expChart.json()[1])
print("-------------------")
print(expChart.json()[2])

print("-------------------")
print("-------------------")
print(type(expChart.json()[0]))
#print(expChart.json()[0][0])
print(expChart.json()[0][1])
print(expChart.json()[0][2])



