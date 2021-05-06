
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

"""

#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=70YMNXM4BZWGEGOA"

#AlphaVantageAbbreviations="https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=70YMNXM4BZWGEGOA"

#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbol=AMD&apikey=70YMNXM4BZWGEGOA"




chartIEXdata="https://cloud.iexapis.com/stable/stock/XOM/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
#chartIEXdata="https://cloud.iexapis.com/stable/stock/XOM/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
#chartIEXdata="https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e"



#https://sandbox.iexapis.com/stable/stock/AMD/dividends/1y?token=Tpk_ae999384a70348b3855e8904d4c46e5e

#https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e

workingChartData=requests.get(chartIEXdata).json()
#print(workingChartData[0]);
#print(len(workingChartData));
#requests.get(chartIEXdata)
"""
print(expChart)
print(expChart.json()[0])
print("-------------------")
print(expChart.json()[1])
print("-------------------")
print(expChart.json()[2])
h=str(expChart.json()[0])
print(h)

print("-------------------")
print("-------------------")
print(expChart.json()[0].keys())
print(expChart.json()[0]['open'])
print(expChart.json()[0]['close'])

#print(expChart.json()[0][0])

"""
"""
columnNames=workingChartData[0].keys()
print(type(columnNames))
print(columnNames)
#columnNames=str(columnNames)
print("------------------------")
columnNames=list(columnNames)
print(type(columnNames))
print(columnNames)
print(columnNames[0])
"""
def columnMaker(columndata,columnName):
    newCol=[];
    x=columndata;
    y=columnName;
    #labels=list(x[0].keys())
    #label=list(x[0].keys())[y];
    newCol.append(y);
    #print("New label")
    #print(label+" label")
    #print(len(x)); 
    #count=0;
    for days in x:
        print(str(type(days[y]))+"-"+str(days[y])) ;
        if type(days[y])='int' or 'float':
           newCol.append(days[y]);
        else:
           newCol.append(0.0); 
        """
        print(str(count)+" in new function "+str(days[label]));
        print("----------------------") 
        print("----------------------")
        """
        #count=count+1;
    newCol=pandas.DataFrame(newCol, columns=[y]);
    #print(y+" column done"); 
    
    #print(newCol);  
    
    return newCol;                        
        


def MonthTableMaker(chartData):
    NewFrame=[]; 
    x=chartData;
    #print("x[0] "+str(x[0]));
    #print("len(x[0]) "+str(len(x[0])));
    names=list(x[0].keys());
    #count=0;
    for columns in list(x[0]):
        #print(str(count)+" "+columns);
        #count=count+1 
        NewFrame.append(columnMaker(x,columns));
    NewFrame=pandas.DataFrame(NewFrame,columns=[names]); 
    print("------------------------------")
    print("------------------------------")
    #print(NewFrame); 
    #print(NewFrame)
    print("len of Frame "+str(len(NewFrame)));
    #NewFrame=pandas.DataFrame(NewFrame[0], columns=[names[0]])
    #print(NewFrame)
    print(names)
MonthTableMaker(workingChartData);    
    
     
     





#https://sandbox.iexapis.com/v1/stock/ market/batch?types=chart,splits,news&symbols=aapl,goog,fb&range=5y%20&token=pk_2a5af8857a7940d4b361bc2b4a14d0ad
#chartIEXdata="https://cloud.iexapis.com/stable/stock/market/market/batch?types=chart,splits,news&symbols=aapl,goog,fb&range=5y%20&token=pk_2a5af8857a7940d4b361bc2b4a14d0ad


