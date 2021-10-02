
"""
Your dedicated access key is: 70YMNXM4BZWGEGOA
Please record this API key at a safe place for future data access.
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=demo
"""
# all IEX supported symbols https://cloud.iexapis.com/beta/ref-data/symbols?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
# workin0g example 1 quote current price https://cloud.iexapis.com/stable/stock/XOM/quote?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
#zetapk_2a5af8857a7940d4b361bc2b4a14d0adf 
#zetask_20d88bd4d61b4e92b2ae7b22d8f8f0aef

#Below need testing
#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=70YMNXM4BZWGEGOA"
#AlphaVantageAbbreviations="https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=70YMNXM4BZWGEGOA"
#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbol=AMD&apikey=70YMNXM4BZWGEGOA"
print("accumulateGMEfiles.py internal run");
import openpyxl
import threading
import requests
import os
from datetime import datetime, date, timedelta
#from datetime import timedelta
import pandas
import json
import numpy
import SQLLoad

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10)

from sklearn import linear_model
ols = linear_model.LinearRegression()

from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
#pca_breast = PCA(n_components=2)
#principalComponents_breast = pca_breast.fit_transform(x)


test="https://sandbox.iexapis.com/stable/stock/xTargetSymbolx/chart/1y?token=Tpk_ae999384a70348b3855e8904d4c46e5e"
def SinglestockIEXdict(x,y,z):
        innerarr=[];
        count=0;
        if z!=0:
           innerarr.append(z+y);
        else:
           innerarr.append(y);  
        while count<len(x):
              push=x[count][y];
              innerarr.append(push); 
              count=count+1;
        out=pandas.DataFrame(innerarr, columns=[y]);
        return innerarr;      
  
        
        
def projection(xlfarrvix):        
       
        LastChartRow=xlfarrvix.iloc[len(xlfarrvix['date'])-2:];
        print("type(LastChartRow.columns) ---- ",type(LastChartRow.columns))
        #LCR=list(LastChartRow.columns)
        def clear(frame,x,y):
            print(frame)    
            len(frame.columns)    
            LCR=list(frame.columns)
            count=0;
            while count<len(frame.columns):
                  string="-";      
                  print("len(frame.columns)  -- ",len(frame.columns));
                  name=LCR[count];
                  lcount=0;
                  while lcount<5:
                        print("count ",count)
                        print("lcount ",lcount)
                        print("frame[name] ",frame[name])
                        #print("type(frame[name][lcount].values) ",type(frame[name][lcount].values));
                        print("frame[name][lcount] ",frame[name][lcount])
                        print("type(frame[name][lcount]) ",type(frame[name][lcount]))
                        #print("frame[name][lcount] ",type(frame[name][lcount]))
                        print("type-type-type(frame[name][lcount]) ",type(type(frame[name][lcount])))
                        string=string+str(type(frame[name][lcount]))
                        lcount=lcount+1;
                  print("str -- ",str)              
                  print("str.find(str) - ",str.find("str"))     
                  
            for i in LCR:
                        
                j=i.find(x);
                k=i.find(y);
                if j > -1:
                   frame=frame.drop([x],axiz=1)
                if k > -1:
                  frame=frame.drop([y],axiz=1)        
            return frame;       
        #clear(LastChartRow,'Symbol','insertionDay');                
        #px=clear(xlfarrvix,'Symbol','insertionDay'); 


        #LastChartRow=clear(xlfarrvix,'Symbol','insertionDay') 
        #LastChartRow=LastChartRow.drop(['dayshiftedclose','date','Symbol','insertionDay'], axis=1);
        #LastChartRow=LastChartRow.drop(['dayshiftedclose','date'], axis=1);      
        px=xlfarrvix.drop(['dayshiftedclose','date'], axis=1)
        py=xlfarrvix['dayshiftedclose']; 
        
        def reorderDF(x):
            print("reorderDF")    
            print("start len -- ",len(x['index']));
            newtitle=[];
            newcols=[];    
            count=0;
            print("len(x.columns)  ",len(x.columns))    
            while count < len(x.columns):
                colnam=x.columns[count];
                col=x[colnam];
                print("colnam -- ",colnam)
                print("col    -- ",col)
                newtitle.append(colnam);
                newcols.append(col);
                if count==0:
                   NFrame=pandas.DataFrame(newcols, columns=[colnam]);
                   #print("NFrame")
                   #print(NFrame)     
                else:
                   NFrame[colnam]=newcols[count];
                count=count+1;
            return NFrame;    
           
        xlfarrvix=reorderDF(xlfarrvix);
        #px=xlfarrvix
        px=clear(xlfarrvix,'Symbol','insertionDay');
        LastChartRow=xlfarrvix.iloc[len(xlfarrvix['date'])-2:];
        py=LastChartRow
        #print(" len reorderDF(px)[0]--------------------------------------------------------- ",len(reorderDF(px)[0]));
        px=px.drop(['index','dayshiftedclose','date'], axis=1)
        LastChartRow=px.iloc[len(xlfarrvix['date'])-2:];
        py=LastChartRow
        pxco=xlfarrvix.drop(['index','dayshiftedclose','date'], axis=1)
        pxcor=pxco.corr(method='pearson')
        
        component=PCA(n_components=4);
        components=component.fit(px);
        pxPCA=component.fit_transform(px);
        pxPCA=pandas.DataFrame(pxPCA);
        explainedVarience=components.explained_variance_
        explainedVarienceRatio=components.explained_variance_ratio_
        LastChartRowPCA=px.iloc[len(pxPCA[0])-2:];
             
        print("Explained Varience =       ",explainedVarience)
        print("Explained Varience Ratio = ",explainedVarienceRatio)
        print(type(components)," components ------ below  ")
        print(components)
        print(pxPCA)
        print(type(components)," components ------ above  ")
        print("pxcor ---- ",pxcor)
        print(type(pxco))
        
        
        
        xTreeMod1000=RandomForestRegressor(n_estimators = 1000).fit(px,py);
        xTreeModPredict1000=xTreeMod1000.predict(LastChartRow);
        print("1000 Tree",xTreeModPredict1000,"Extracted value - ",xTreeModPredict1000[1])
        
        xLinearMod=linear_model.LinearRegression().fit(px,py);
        xLinearPredictMod=xLinearMod.predict(LastChartRow);
        print("xLinearPredictMod ",xLinearPredictMod,"Extracted value - ",xLinearPredictMod[1])
        #return xlfarrvix;
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------
     
        #xx=xlfarrvix.drop(['dayshiftedclose','date','xldate'], axis=1);
        #xx=xlfarrvix.drop(['dayshiftedclose','date'], axis=1);
        xx=px;
        xy=xlfarrvix['dayshiftedclose'];
    
        #------------------------------------------------
        print("xx review series splits ")
        xx_train,xx_test,xy_train,xy_test=train_test_split(px,py,test_size=0.2);
        #xx_train,xx_test,xy_train,xy_test=train_test_split(xx,xy,test_size=0.2);
        
        print("xx tree model 10 ")
        xTreeMod10=RandomForestRegressor(n_estimators = 10).fit(xx_train,xy_train);
        xTreeModPredict10=xTreeMod10.predict(xx_test);
        Std_ofTP10=numpy.std(xTreeModPredict10);
        
        print("xx tree model 100 ")
        xTreeMod100=RandomForestRegressor(n_estimators = 100).fit(xx_train,xy_train);
        xTreeModPredict100=xTreeMod100.predict(xx_test);
        Std_ofTP100=numpy.std(xTreeModPredict100);
        
        print("xx tree model 200 ")
        xTreeMod200=RandomForestRegressor(n_estimators = 200).fit(xx_train,xy_train);
        xTreeModPredict200=xTreeMod200.predict(xx_test);
        Std_ofTP200=numpy.std(xTreeModPredict200);
        
        print("xx tree model 1000 ")
        xTreeMod1000=RandomForestRegressor(n_estimators = 1000).fit(xx_train,xy_train);
        xTreeModPredict1000=xTreeMod1000.predict(xx_test);
        Std_ofTP1000=numpy.std(xTreeModPredict1000);
        
        print("xx linear model ")
        xLinearMod=linear_model.LinearRegression().fit(xx_train,xy_train);
        xLinearPredictMod=xLinearMod.predict(xx_test);
        Std_ofTPxLinearPredictMod=numpy.std(xLinearPredictMod);
        
        
        print("xx base review frame ")
        xreviewFrame=pandas.DataFrame(xy_test);
        xreviewFrame.columns=['Shifted close'];
        #xreviewFrame['close']=list(xx_test['close']);
          
        print("xx model specific review frame ")        
        xreviewFrame['Tree Prediction 10']=xTreeModPredict10;
        xreviewFrame['Tree Prediction 100']=xTreeModPredict100;
        xreviewFrame['Tree Prediction 200']=xTreeModPredict200;
        xreviewFrame['Tree Prediction 1000']=xTreeModPredict1000;
        xreviewFrame['Linear Prediction']=xLinearPredictMod;
        #------------------------------------------------
        
        
        print("after pause ")
        print("xreviewFrame datatype ------------- ",type(xreviewFrame))
        print("xreviewFrame.corr()");
        print(xreviewFrame.corr());
        xSTD=numpy.std(xreviewFrame);
        print(xSTD)
        
        print("x-----------------------------------")
        print("Std_of Shifted Close ",numpy.std(xy))
        print("Std_ofTP10 ",Std_ofTP10)
        print("Std_ofTP100 ",Std_ofTP100)
        print("Std_ofTP200 ",Std_ofTP200)
        print("Std_ofTP1000 ",Std_ofTP1000)
        print('Linear StD=',numpy.std(xLinearPredictMod))
                 
        return;        
        
        
        
        
        
def IEXColmaker(TargetSymbol):
        print("IEXColmaker(): running");
        URLPull=test;
        print("URL Data Pulled ")
        URLPull=URLPull.replace("xTargetSymbolx",TargetSymbol)
        vixPull=URLPull.replace(TargetSymbol,"VXX");
        xlfPull=URLPull.replace(TargetSymbol,"SQQQ");
        iexpull=requests.get(URLPull);
        vixPull=requests.get(vixPull);
        xlfPull=requests.get(xlfPull);
        print("Secondary Data Pulled ")
      
        iexdata=json.loads(iexpull.text);
        vixdata=json.loads(vixPull.text);
        xlfdata=json.loads(xlfPull.text);
        print("Jsons Loaded ")
       
        arr=[];
        vixarr=[];
        xlfarr=[];
             
        keys=list(iexdata[0].keys());
        vixkeys=list(vixdata[0].keys());
        xlfkeys=list(xlfdata[0].keys());
        
        def colPrefix(x):
            prefixedelems=[];
            for elems in x:
                elems="vx"+elems;
                prefixedelems.append(elems);
                prefixedelems;
            return prefixedelems;    
        vixkeys=colPrefix(vixkeys);               
        def subtable(data,key,z):
            iarr=[];    
            count=0;
            while count<len(key): 
              iarr.append(SinglestockIEXdict(data,key[count],z));  
              count=count+1;
            return iarr;
        arr=subtable(iexdata,keys,0);
        vixarr=subtable(vixdata,keys,"vx");
        xlfarr=subtable(xlfdata,keys,"xl");
                       
        def dframemaker(x,y):
            drops=["label","symbol","id","key","subkey"];
            altdrops=[];
            for elem in drops:
                elem=y+elem;
                altdrops.append(elem);
            Newarr=pandas.DataFrame(x).transpose();
            Newarr=Newarr.rename(columns=Newarr.iloc[0]);
            Newarr=Newarr.drop([0]).reset_index().drop(altdrops, axis=1);    
            return Newarr;    
        arr1=dframemaker(arr,"");
        vixarr1=dframemaker(vixarr,"vx");
        xlfxarr1=dframemaker(xlfarr,"xl");
              
        def metricshift(w,q):
            shiftCol=[];
            shiftColDate=[];
            w=w[q];
            date=arr1['date'];
            count=0;
            while count<len(w):
              shiftColDate.append(date[count]);  
              count=count+1;
              if count==len(w):
                 return shiftCol;       
              shiftCol.append(w[count]);
            return shiftCol;
        dayshiftedclose=metricshift(arr1,'close');
        def compare(x1,y1,z):
            f=248 
            if len(y1)>len(x1):
               y1=y1.drop([len(x1)]);
               return y1; 
                    
            daten=z+'date'    
            x=x1['date']; 
            y=y1[daten];    
       
            count=0;  
            xdesignator=int(x[len(x)-1][8:]);
            ydesignator=int(y[len(y)-1][8:]);
            alty=y1;
           
            #print("xdesignator==ydesignator ",xdesignator,"==",ydesignator) 
            if xdesignator==ydesignator:
               #print("xdesignator==ydesignator ",xdesignator,"==",ydesignator)         
               return y1;
            if xdesignator<ydesignator:
               while count < len(x):
                  if x[count]==y[count]: 
                     print(count,"--",x[count],"==",y[count]);   
                  else:
                     arr=[];   
                     yrmo=y[count][:8];
                     newday=x[count];
                     newday=pandas.DataFrame([newday], columns=[daten]);
                     for elem in alty.columns:
                         arr.append(0);
                     narr=pandas.DataFrame(arr);
                     narr=narr.transpose();
                     altyCols=list(alty.columns).remove('index');
                     narr.columns=alty.columns; 
                     narr=narr.drop(columns=[daten]);
                     narr[daten]=newday;
                     topcan=alty[:count];
                     midcan=narr;
                     bottomcan=alty[count:];
                     topcan=topcan.append(midcan);
                     topcan=topcan.append(bottomcan);
                     topcan=topcan.drop(columns=['index'])   
                     topcan=topcan.reset_index();
                                          
                     tdesignator=topcan[daten].iloc[len(topcan)-1]; 
                     tdesignator=int(tdesignator[8:]); 
                     if xdesignator==tdesignator:
                        return topcan        
                     else:
                        if len(topcan)>len(x1):
                           return topcan;
                  count=count+1;
            return y1;            
        arr1=arr1.drop([len(dayshiftedclose)]);
        vixarr1=compare(arr1,vixarr1,'vx'); 
        xlfxarr1=compare(arr1,xlfxarr1,'xl');
               
        arr1['dayshiftedclose']=dayshiftedclose;
        arrvix=arr1.merge(vixarr1, on="index");
        xlfarrvix=arrvix.merge(xlfxarr1, on="index");
        xlfarrvix=xlfarrvix.drop(['xldate','vxdate'], axis=1)
        
        Sqltable=SQLLoad.MakeDailyTable(arr1,TargetSymbol);
        projection(xlfarrvix)
        return xlfarrvix;
       
            

def Char2Num(col):
 arr={};
 arrout=[];
 count=0;
 for member in col:
     if member in arr:
        arrout.append(arr[member]);
     else:
        arr[member]=count;
        arrout.append(arr[member]);
        count=count+1;
 return arrout;      
  
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
    def NasdaqMKTIndicator0(x):
        arr=[];
        count=0; 
        while count<len(x):
              arr.append(0);
              count=count+1;
        return arr;
    
    def NONnasdaqMKTIndicator(col):
        arr={};
        arrout=[];
        count=0;
        for member in col:
            if member in arr:
               arrout.append(arr[member]);
            else:
               count=count+1
               arr[member]=count;
               arrout.append(arr[member]);
        return arrout;   
        
    os.chdir("/GMDelight/GMDelight/Sheets/rememberGME/NasdaqAbbreviations");
    try:
       NasdaqNativeAbbreviations=pandas.read_csv('ActiveNativendqAbbrev','|');
       NasdaqAbbreviations=pandas.read_csv('ActivendqAbbrev','|');
    except:
       print("Nasdaq Symbol Update Failed - Archive in use") 
       NasdaqNativeAbbreviations=pandas.read_excel('NasdaqArcaneNative.xlsx');
       NasdaqAbbreviations=pandas.read_excel('NasdaqArcaneOther.xlsx');

    #dfmi.loc[:, ('one', 'second')]
    TopSymbols=NasdaqNativeAbbreviations.loc[:, ("Symbol","Security Name","ETF")]    
    #TopSymbols=NasdaqNativeAbbreviations[["Symbol","Security Name","ETF"]];
    TopSymbols["MKT"]=NasdaqMKTIndicator0(TopSymbols);
    
    #dfmi.loc[:, ('one', 'second')]
    BottomSymbols=NasdaqAbbreviations.loc[:, ("ACT Symbol","Security Name","ETF")]    
    #BottomSymbols=NasdaqAbbreviations[["ACT Symbol","Security Name","ETF"]];
    BottomSymbols["Symbol"]=BottomSymbols["ACT Symbol"];
    BottomSymbols=BottomSymbols.drop(["ACT Symbol"], axis=1);
    BottomSymbols["MKT"]=NONnasdaqMKTIndicator(NasdaqAbbreviations["Exchange"]);
    
    STKsymbols=TopSymbols.append(BottomSymbols).reset_index();
    STKsymbols=STKsymbols.drop(["index"], axis = 1);
    STKsymbols.columns=["Symbols","Security Name","ETF","MKT"];
    STKsymbols["ETF Num"]=Char2Num(STKsymbols["ETF"])

    #print(IEXColmaker("AMD"))    
    #print(STKsymbols)
    return STKsymbols;
    
def DailyBasisInserter():
    skiplist=" ";    
    today=date.today()        
    d=timedelta(days=1);
    fromday=today-d;    
    tallyPattern=[]; 
    insertedSymbols=[];    
    print("initiating DailyBasisInserter() 1 ")    
    Symbols=runNasdaq()['Symbols'];
    tally=0;
    while tally < len(Symbols):
        SqlCall=SQLLoad.CallFromSQL(Symbols[tally],"DailyTabl",today);
        SqlCall1=SQLLoad.CallFromSQL(Symbols[tally],"DailyTabl",fromday);
        last2days=len(SqlCall)+len(SqlCall1);
       
        inskip=skiplist.find(str(Symbols[tally]));
        print('inskip===',inskip)
        print('Symbols[tally] ===',Symbols[tally])
        print("Currently ",Symbols[tally]);  
        print("Next ",Symbols[tally+1]);
        
        URLPull=test;
        URLPull=URLPull.replace("xTargetSymbolx",Symbols[tally])
        print(URLPull)
        iexpull=requests.get(URLPull);
        iexdata=json.loads(iexpull.text);
        print("len(iexdata) -- ",len(iexdata));
        
        if len(iexdata)<60:
           inskip=str(inskip)+str(Symbols[tally]);
           skip=inskip.find(str(Symbols[tally]));
           skip=skip+len(iexdata);     
           print("inskip ",inskip)
           print("skip ",skip)
           print("iexdata - ",len(iexdata),"  iexdata - fired ")
           last2days=last2days+skip;
        if last2days<1:
              print("iexdata------------------------Start-------------------------------------------------------");
              print(pandas.DataFrame(iexdata)['date']);
              print("iexdata------------------------end-------------------------------------------------------"); 
              print(Symbols[tally]," activating IEXcolmaker with length ",len(iexdata))    
              IEXColmaker(Symbols[tally]);
              print("-----Inserting---------")  
               
        
                
        print("initiating DailyBasisInserter() loop ",tally)         
        tallyPattern.append(tally);
        insertedSymbols.append(Symbols[tally]);
        #print('tallyPattern ---------- ',tallyPattern)
        #print('insertedSymbols-------- ',insertedSymbols)
        """
        if (len(insertedSymbols)%10)==0:
           print("len(insertedSymbols----) ",len(insertedSymbols))
        """
        if len(insertedSymbols)>2:
           print("Last Successfully loaded Inserted Symbol - ",insertedSymbols[len(insertedSymbols)-1])
        tally=tally+1;
        

        
DailyBasisInserter();       
                
        
        
#pullNasdaqAbbreves();
#print(runNasdaq());
#print(runNasdaq()['Symbols']);
#IEXColmaker("AMD");
#SqlCall=SQLLoad.CallFromSQL("*","DailyTable");
#print(SqlCall);



#---------------------------------------------------------------------------------------------------------------
"""
    
    def nasdaqTester():
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------")
        #brokenlines=[];
        responseCode=[];
        columnsOfNasdaqNativeAbbreviation=NasdaqAbbreviations.columns
        NasdaqTesFrame=NasdaqAbbreviations['CQS Symbol'];
        print(type(NasdaqTesFrame))
        print(NasdaqTesFrame)
        sze=len(NasdaqTesFrame)
        lineItem=0;
        errCount=0;
       
       #while (lineItem < 10):
        #    nums=NasdaqAbbreviations['CQS Symbol'][lineItem];
        #print(NasdaqTesFrame)
      
        for nums in NasdaqAbbreviations['CQS Symbol']:
          
            test="https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e"
                     
   #ACTIVATE FOR REAL DATA0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000         
            #test="https://cloud.iexapis.com/stable/stock/"+str(nums)+"/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
            rtest=requests.get(test); 
            if (str(rtest).find("200")>0):
                errCount=errCount+str(rtest).find("200"); 
            
            print(str(rtest).find("200"));
            #brokenlines.append(lineItem);
            responseCode.append(rtest);
            print(str(rtest)+"   "+str(lineItem)+" of "+str(sze));
            lineItem=lineItem+1;
        NasdaqTesFrame=pandas.DataFrame(NasdaqTesFrame,columns=['CQS Symbol']); 
        
        print("NasdaqTesFrame")
        print(NasdaqTesFrame)
        #NasdaqTesFrame['broken line numbers']=brokenlines;
        NasdaqTesFrame['response Code']=responseCode;
        print(type(NasdaqTesFrame)) 
        print(NasdaqTesFrame.columns)
        print(NasdaqTesFrame) 
        print("errCount = "+str(errCount))
        print(os.getcwd())
        os.chdir("/GMDelight/GMDelight/Sheets/rememberGME/GMEouts")
        print(os.getcwd())
        print(os.listdir())
        NasdaqExp=pandas.read_excel('gmetemplate.xlsx')
        print(NasdaqExp)
        NasdaqTesFrame.to_excel(r'gmetemplate.xlsx',index=False)
        #NasdaqExp=pandas.reprint("NasdaqExp.columns")ad_excel('gmetemplate.xlsx')
        print(NasdaqExp)
        print("NasdaqExp.columns")
        print(NasdaqExp.columns)
        
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------")
    trd=threading.Thread(target=nasdaqTester);
    trd.start();
    #NasdaqTesFrame['broken line numbers']=brokenlines;
    #NasdaqTesFrame['response Code']=responseCode;
    #print(NasdaqTestFrame)
    
    
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
    print("Month Maker")
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
"""    
    
     
     






