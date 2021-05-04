import os
from datetime import datetime
import pandas


print(os.getcwd())
print(os.listdir())

def pullNasdaqAbbreves():
    os.chdir('Sheets/rememberGME');
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
    
pullNasdaqAbbreves();
NasdaqNativeAbbreviations=pandas.read_csv('ActiveNativendqAbbrev','|');
NasdaqAbbreviations=pandas.read_csv('ActivendqAbbrev','|');

print(NasdaqAbbreviations)
print(NasdaqNativeAbbreviations)
print(str(os.listdir());)


