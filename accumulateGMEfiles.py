
"""
Your dedicated access key is: 70YMNXM4BZWGEGOA
Please record this API key at a safe place for future data access.
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=demo
"""
# all IEX supported symbols https://cloud.iexapis.com/beta/ref-data/symbols?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
# working example 1 quote current price https://cloud.iexapis.com/stable/stock/XOM/quote?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
#zetapk_2a5af8857a7940d4b361bc2b4a14d0adf 
#zetask_20d88bd4d61b4e92b2ae7b22d8f8f0aef

#Below need testing
#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=70YMNXM4BZWGEGOA"
#AlphaVantageAbbreviations="https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=70YMNXM4BZWGEGOA"
#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbol=AMD&apikey=70YMNXM4BZWGEGOA"


import requests
import os
from datetime import datetime
import pandas


#Nasdaq Symbols
def pullNasdaqAbbreves():
  
    os.chdir("/GMDelight/GMDelight/Sheets/rememberGME/NasdaqAbbreviations")
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
    
  
def runNasdaq():
    pullNasdaqAbbreves();
    os.chdir("/GMDelight/GMDelight/Sheets/rememberGME/NasdaqAbbreviations");
    try:
       NasdaqNativeAbbreviations=pandas.read_csv('ActiveNativendqAbbrev','|');
       NasdaqAbbreviations=pandas.read_csv('ActivendqAbbrev','|');
    except:
       print("Nasdaq Symbol Update Failed - Archive in use") 
       NasdaqNativeAbbreviations=pandas.read_excel('NasdaqArcaneNative.xlsx');
       NasdaqAbbreviations=pandas.read_excel('NasdaqArcaneOther.xlsx');
        
        
    print("---------------------------------------------------------------------")
    print("---------------------------------------------------------------------")
    brokenlines=[];
    responseCode=[];
    columnsOfNasdaqNativeAbbreviation=NasdaqAbbreviations.columns
    NasdaqTesFrame=NasdaqAbbreviations['CQS Symbol'];
    lineItem=0;
    for nums in NasdaqAbbreviations['CQS Symbol']:
        test=str("https://cloud.iexapis.com/stable/stock/"+nums+"/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad")
        rtest=requests.get(test);
        brokenlines.append(lineItem);
        responseCode.append(rtest);
        lineItem=lineItem+1;
        print(str(rtest)+"   "+str(lineItem));
    print("---------------------------------------------------------------------")
    print("---------------------------------------------------------------------")
    NasdaqTesFrame['broken line numbers']=brokenlines;
    NasdaqTesFrame['response Code']=responseCode;
    print(NasdaqTestFrame)
    
    
    #print(NasdaqAbbreviations);
    
    #print(NasdaqNativeAbbreviations);
    #print(NasdaqAbbreviations['CQS Symbol'])
    #print("columnsOfNasdaqNativeAbbreviation "+str(columnsOfNasdaqNativeAbbreviation))
    
    return NasdaqNativeAbbreviations;


chartIEXdata="https://cloud.iexapis.com/stable/stock/XOM/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
#chartIEXdata="https://cloud.iexapis.com/stable/stock/XOM/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
#chartIEXdata="https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e"

#https://sandbox.iexapis.com/stable/stock/AMD/dividends/1y?token=Tpk_ae999384a70348b3855e8904d4c46e5e
#https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e

workingChartData=requests.get(chartIEXdata).json()
def columnMaker(columndata,columnName):
    newCol=[];
    x=columndata;
    y=columnName;
    newCol.append(y);
    for days in x:
        fi=str(type(days[y])).find('int');
        ff=str(type(days[y])).find('float');
        fff=ff+fi;
        if fff<=-2:
           newCol.append(0.0); 
        else:
           newCol.append(days[y]);
    newCol=pandas.DataFrame(newCol, columns=[y]);
    return newCol;                        
        


def MonthTableMaker(chartData):
    PreFrame=[]; 
    x=chartData;
    names=list(x[0].keys());
    for columns in list(x[0]):
        PreFrame.append(columnMaker(x,columns));
    NewFrame=pandas.DataFrame(PreFrame[0], columns=[names[0]])
    cnt=0;
    while cnt<len(PreFrame)-1:
        cnt=cnt+1;
        NewFrame[names[cnt]]=PreFrame[cnt];
    NewFrame=NewFrame.drop([0]);   
    print(NewFrame);
    return NewFrame;
 
#MonthTableMaker(workingChartData); 
def TableGen():
    print("TableGen Run")
    #MonthTableMaker(workingChartData);
    runNasdaq();
    ready=MonthTableMaker(workingChartData).to_html
    #return ready
TableGen();
    
    
     
     






