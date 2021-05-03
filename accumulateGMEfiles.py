

from datetime import datetime


nasdaqAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
print(nasdaqAbbreviations)
filedate=str(datetime.now().date())
ndq=str('curl '+nasdaqAbbreviations+' -o nasdaqAbbreviations-'+filedate)
print(ndq)
os.system(ndq)
print("accumilateGMEfiles ran")
print("accumilateGMEfiles ran")
