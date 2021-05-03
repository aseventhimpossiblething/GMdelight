import os
from datetime import datetime
import pandas


print(os.getcwd())
print(os.listdir())

def pullNasdaqAbbreves():
    os.chdir('Sheets');
    print(os.listdir());
    mglob=str(os.listdir());
    findit=mglob.find("BidOp")
    print(findit)
    print("glob Data Type "+str(type(mglob)))
    #os.system('rm ActivendqAbbrev')
    print(os.listdir());
    nasdaqAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
    print(nasdaqAbbreviations)
    filedate=str(datetime.now().date())
    ndqAbbrecords=str('curl '+nasdaqAbbreviations+' -o nasdaqAbbreviations-'+filedate)
    #ActndqAbbrv=str('curl '+nasdaqAbbreviations+' -o ActivendqAbbrev')
    #print(ndq)
    #os.system(ndqAbbrecords)
    #os.system(ActndqAbbrv)
    print("ac#cumilateGMEfiles ran")
    print("accumilateGMEfiles ran")
    
pullNasdaqAbbreves();
#print(os.listdir());
#os.chdir('Sheets');
print(os.getcwd());
print(os.listdir());
#pandas.read_csv('ActivendqAbbrev')


