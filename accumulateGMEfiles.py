import os
from datetime import datetime
import pandas


print(os.getcwd())
print(os.listdir())

def pullNasdaqAbbreves():
    os.chdir('Sheets');
    #print(os.listdir());
    mglob=str(os.listdir());
    ActivendqAdd=mglob.find("ActivendqAbbrev");
    if ActivendqAdd>-1:
       os.system('rm ActivendqAbbrev');
       
    
    
    #print(ActivendqAdd)
    #print("glob Data Type "+str(type(mglob)))
   
    print(os.listdir());
    nasdaqAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
    #print(nasdaqAbbreviations)
    filedate=str(datetime.now().date())
    ndqAbbrecords=str('curl '+nasdaqAbbreviations+' -o nasdaqAbbreviations-'+filedate)
    ActndqAbbrv=str('curl '+nasdaqAbbreviations+' -o ActivendqAbbrev')
    #print(ndq)
    os.system(ndqAbbrecords)
    os.system(ActndqAbbrv)
    print("accumilateGMEfiles ran")
    print("accumilateGMEfiles ran")
    
pullNasdaqAbbreves();
#print(os.listdir());
#os.chdir('Sheets');
print(os.getcwd());
print(os.listdir());
#pandas.read_csv('ActivendqAbbrev')


