import os
from datetime import datetime
import pandas

print(os.cwd())
print(os.listdir())

def pullNasdaqAbbreves():
    nasdaqAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
    print(nasdaqAbbreviations)
    filedate=str(datetime.now().date())
    ndqAbbrecords=str('curl '+nasdaqAbbreviations+' -o Sheets/nasdaqAbbreviations-'+filedate)
    ActndqAbbrv=str('curl '+nasdaqAbbreviations+' -o Sheets/ActivendqAbbrev')
    @print(ndq)
    os.system(ndqAbbrecords)
    os.system(ActndqAbbrv)
    print("accumilateGMEfiles ran")
    print("accumilateGMEfiles ran")
    
pullNasdaqAbbreves();
print(os.listdir());
#os.chdir();


