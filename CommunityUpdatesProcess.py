MaintatanceVar="Off";
import glob
import numpy
import scipy
import pandas
import BidOpAssist
import fileHandler
from flask import Flask, Markup, render_template, request
import os
import psycopg2
import re
import threading
import numpy
import Market_LookUp
import sys
from openpyxl import Workbook
from openpyxl import load_workbook
import xlsxwriter



SheetsAreLoaded=None; 
IsCommValid=None;
IsGoogleValid=None;
IsBingValid=None;


def CheckSheetData(sheetname,sheet,checkword1,checkword2,checkword3,checkword4):
 titlestring=str(sheet.iloc[1])
 if titlestring.find(checkword1)!=-1 and titlestring.find(checkword2)!=-1 and\
  titlestring.find(checkword3)!=-1 and titlestring.find(checkword4)!=-1:
  return "Valid"
 else:
  Invalid=sheetname+" sheet contains format or content error check sheet and resubmit " 
  return Invalid
    
def LoadCommunities(WorkingCommunities,checkword1,checkword2,checkword3,checkword4):
 WorkingCommunitiesname="WorkingCommunities" 
 global IsCommValid
 IsCommValid=CheckSheetData(WorkingCommunitiesname,WorkingCommunities,checkword1,checkword2,checkword3,checkword4)
 if CheckSheetData(WorkingCommunitiesname,WorkingCommunities,checkword1,checkword2,checkword3,checkword4)=="Valid":
  WorkingCommunities=pandas.DataFrame(WorkingCommunities, columns=['Builder Name','Brand Name','Division Id','Division Name',\
                                                                   'Community Id','Community Name','City','State','Zip',\
                                                                   'Market ID','Market Name'])
   
  return WorkingCommunities
 else:
  print("Load Communities cannot run...............",IsCommValid)
  return IsCommValid  

def WorkingGoogle():  
 os.chdir('/app/Sheets/CommunityUpdates/Google/currentGoogle')
 WorkingGoogle=pandas.read_excel('WorkingGoogle')
 global IsGoogleValid 
 IsGoogleValid=CheckSheetData("WorkingGoogle",WorkingGoogle,'Campaign','Ad Group','Headline 1','Final URL')
 if IsGoogleValid!="Valid":
  return IsGoogleValid
 else:
  WorkingGoogle=pandas.DataFrame(WorkingGoogle,columns=['Campaign','Ad Group', 'Final URL'])
  return  WorkingGoogle
  
def WorkingBing():
 os.chdir('/app/Sheets/CommunityUpdates/Bing/currentBing')
 WorkingBing=pandas.read_excel('WorkingBing')
 IsBingValid=CheckSheetData("WorkingBing",WorkingBing,'Campaign','Ad Group','Title Part 1','Final Url')
 if IsBingValid!='Valid':
  return IsBingValid
 WorkingBing=pandas.DataFrame(WorkingBing,columns=['Campaign','Ad Group','Final Url']).drop(0)
 return WorkingBing


def filterNonParticipators(theFrame):
 print(" ",len(theFrame))
 
 """
 theFrame['Community Name']=theFrame['Community Name'].str.replace("40s"," ").replace("40'"," ").replace("40"," ").replace("45s"," ")\
 .replace("45'"," ").replace("45"," ").replace("50s"," ").replace("50'"," ").replace("50"," ").replace("55s"," ")\
 .replace("55'"," ").replace("55"," ").replace("60s"," ").replace("60'"," ").replace("60"," ").replace("65s"," ")\
 .replace("65'"," ").replace("65"," ").replace("70s"," ").replace("70'"," ").replace("70"," ").replace("75s"," ")\
 .replace("75'"," ").replace("75"," ").replace("80s"," ").replace("80'"," ").replace("80"," ").replace("85s"," ")\
 .replace("85'"," ").replace("85"," ").replace("90s"," ").replace("90'"," ").replace("90"," ").replace("95s"," ")\
 .replace("95'"," ").replace("95"," ").replace("100s"," ").replace("100'"," ").replace("100"," ").replace("105s"," ")\
 .replace("105'"," ").replace("105"," ").replace("110s"," ").replace("110'"," ").replace("110"," ")
 
 theFrame=theFrame.replace({"40s":"","40's":"","(40s)":"","40s'":"","40'":"","40":"","50s":"","50's":"","(50s)":"",\
                   "50s'":"","50'":"","50":"","55s":"","55's":"","(55s)":"","55s'":"","55'":"","55":""\
                  ,"60s":"","60's":"","(60s)":"","60s'":"","60'":"","60":"","65s":"","65's":"","(65s)":"",\
                   "65s'":"","65'":"","65":"","70s":"","70's":"","(70s)":"","70s'":"","70'":"","70":""\
                  ,"75s":"","75's":"","(75s)":"","75s'":"","75'":"","75":"","85s":"","85's":"","(85s)":"",\
                   "85s'":"","85'":"","85":"","90s":"","90's":"","(90s)":"","90s'":"","90'":"","90":"",\
                   "95s":"","95's":"","(95s)":"","95s'":"","95'":"","95":"","100s":"","100's":"","(100s)":""})
                   #"100s'":"",100":"","100":"","100":"","100'":"","(100)":"","100":"","100":"","100":""})
 """                  
 
 
 theFrame=theFrame.drop_duplicates();
 print("Length theFrame=theFrame.drop_duplicates() ",len(theFrame))
 
 theFrame=theFrame.dropna()
 print("LengththeFrame=theFrame.dropna ",len(theFrame))
 #print("theFrame['Brand Name'].str.contains('Clayton') ",theFrame['Brand Name'].str.contains('Clayton'))
 
 theFrame=theFrame[~theFrame['Brand Name'].str.contains('Clayton')]
 print("theFrame[~theFrame['Brand Name'].str.contains('Clayton')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Brand Name'].str.contains('Oakwood')]
 print("theFrame[~theFrame['Brand Name'].str.contains('Oakwood')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Brand Name'].str.contains('Craftmark')]
 print("theFrame[~theFrame['Brand Name'].str.contains('Craftmark')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Builder Name'].str.contains('Clayton')]
 print("theFrame[~theFrame['Builder Name'].str.contains('Clayton')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Builder Name'].str.contains('Oakwood')]
 print("theFrame[~theFrame['Builder Name'].str.contains('Oakwood')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Builder Name'].str.contains('Craftmark')]
 print("theFrame[~theFrame['Builder Name'].str.contains('Craftmark')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Community Name'].str.contains('Clayton')]
 print("theFrame[~theFrame['Community Name'].str.contains('Clayton')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Community Name'].str.contains('Craftmark')]
 print("theFrame[~theFrame['Community Name'].str.contains('Craftmark')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Community Name'].str.contains('Oakwood')]
 print("theFrame[~theFrame['Community Name'].str.contains('Oakwood')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Brand Name'].str.contains('Freedom')]
 print("theFrame[~theFrame['Brand Name'].str.contains('Freedom')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Community Name'].str.contains('Freedom')]
 print("theFrame[~theFrame['Community Name'].str.contains('Freedom')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Builder Name'].str.contains('Freedom')]
 print("theFrame[~theFrame['Builder Name'].str.contains('Freedom')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Brand Name'].str.contains('Crossland')]
 print("theFrame[~theFrame['Brand Name'].str.contains('Crossland')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Community Name'].str.contains('Crossland')]
 print("theFrame[~theFrame['Community Name'].str.contains('Crossland')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Builder Name'].str.contains('Crossland')]
 print("theFrame[~theFrame['Builder Name'].str.contains('Crossland')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Brand Name'].str.contains('G & I')]
 print("theFrame[~theFrame['Brand Name'].str.contains('G & I'')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Community Name'].str.contains('G & I')]
 print("theFrame[~theFrame['Community Name'].str.contains('G & I')] ",len(theFrame))
 
 theFrame=theFrame[~theFrame['Builder Name'].str.contains('G & I')]
 print("theFrame[~theFrame['Builder Name'].str.contains('G & I')] ",len(theFrame))
 
 
 """
 #print(theFrame['Community Name'])
 try:
  #print("theFrame[[23]] ",theFrame[[23]])
 except:
  #print("theFrame[[23]] failed")
 
 try:
  print("theFrame['Community Name'][23] ",theFrame['Community Name'][23])
 except:
  print("theFrame['Community Name'][23] Failed ")
  """
 theFrame.reset_index() 
 print(theFrame)
 
 failcounter=0 
 DeDupstring=""
 icount=5;
 while icount<len(theFrame['Community Name']):
  try:
   print("Start of try before Community String")
   Community=str(theFrame["Community Name"][icount]).replace("40s","").replace("40'","").replace("40","").replace("45s","")\
   .replace("45'","").replace("45","").replace("50s","").replace("50'","").replace("50","").replace("55s","")\
   .replace("55'","").replace("55","").replace("60s","").replace("60'","").replace("60","").replace("65s","")\
   .replace("65'","").replace("65","").replace("70s","").replace("70'","").replace("70","").replace("75s","")\
   .replace("75'","").replace("75","").replace("80s","").replace("80'","").replace("80","").replace("85s","")\
   .replace("85'","").replace("85","").replace("90s","").replace("90'","").replace("90","").replace("95s","")\
   .replace("95'","").replace("95","").replace("100s","").replace("100'","").replace("100","").replace("105s","")\
   .replace("105'","").replace("105","").replace("110s","").replace("110'","").replace("110","")
   print("Community string and replace")
   Community=theFrame["Community Name"][icount]
   #print("Community=theFrame['Community Name'][icount] ")
   DeDupstring=DeDupstring+" "+Community
   #print("DeDupSting Grew")
   #print(Community)
   #print("Successfull fire ",icount)
  except:
   #print("Row Skipped ",icount);
   failcounter+=1;
  DeDupstring=DeDupstring+" "+Community
  icount+=1;
  print("Switching Loops") 
  print("times failed ",failcounter)
 icount0=0;
 while icount0<len(theFrame['Community Name']):
  try:
   Community=str(theFrame["Community Name"][icount]).replace("40s","").replace("40'","").replace("40","").replace("45s","")\
   .replace("45'","").replace("45","").replace("50s","").replace("50'","").replace("50","").replace("55s","")\
   .replace("55'","").replace("55","").replace("60s","").replace("60'","").replace("60","").replace("65s","")\
   .replace("65'","").replace("65","").replace("70s","").replace("70'","").replace("70","").replace("75s","")\
   .replace("75'","").replace("75","").replace("80s","").replace("80'","").replace("80","").replace("85s","")\
   .replace("85'","").replace("85","").replace("90s","").replace("90'","").replace("90","").replace("95s","")\
   .replace("95'","").replace("95","").replace("100s","").replace("100'","").replace("100","").replace("105s","")\
   .replace("105'","").replace("105","").replace("110s","").replace("110'","").replace("110","")
   
   Community=theFrame["Community Name"][icount];
   
   #Community.drop()
   if DeDupstring.count(Community)>0:
    print("found in string ",DeDupstring.count(Community)," times");
    theFrame.drop([icount0])
   
  except:
   icount0+0;
   #print("Exception on Second Loop ")
 
 
 
                                                            
 
 return theFrame;

 """
 theFrame=theFrame;
 print("at start of filter len(theFrame) ",len(theFrame));
 theFrame.reset_index();
 
 def subfilter(word,theFrame):
  theFrame0=numpy.array(theFrame['Brand Name']);
  #recursion_level=0;
  scount=0;
  found=0;
  theBrand=str(theFrame0[[scount]]);
  #print("Running Subfilter recusion Level ",recursion_level)
  while scount<len(theFrame0):
   theBrand=str(theFrame0[[scount]]);
   #print("Looping in Subfilter")
   try:
    if theBrand.find(word)!=-1:
     theFrame=theFrame.drop([scount]);
     #print(" filter droped theBrand ",theBrand);
     found+=1
    else:
     if scount<100:
      scount+0;
   except:
     found=found+0;
    
   scount+=1;
   
  if found!=0:
   #recursion_level+=1
   subfilter(word,theFrame);
   
  return theFrame;

 #theFrame=subfilter("Clayton",theFrame);
 #theFrame=subfilter("Clayton ",theFrame);
 theFrame=subfilter("Clayt",theFrame)
 
 print("At end of Filter len(theFrame) ",len(theFrame))
 return theFrame;
 """

def MergeURLs(chan,chan2):
 print("MergeURLs() start for ",chan2)
 URLS="A";
 count=0;
 if chan2=="Bing":
  count=1;
 hilecount=len(chan)
 if type(MaintatanceVar)=="<class 'int'>":
   hilecount=MaintatanceVar;
 while count < hilecount :
  URLS=URLS+chan[count]
  if count % 50000 == 0:
   print(chan2," _ ",count)
   #print("Low count setting in MergeURLS nonfunctional")
  count+=1
 return URLS
 
def communityCheck(checkby,checkin,Name):
 print("Start Community Check for ",Name)
 checkby=checkby.reset_index()
 count=0;
 DropRows=[];
 hilecount=checkby['Community Id'].count();
 if type(MaintatanceVar)=="<class 'int'>":
  hilecount=MaintatanceVar;
 while count < hilecount:
  if checkin.find(str(checkby['Community Id'][count]))>-1:
   DropRows.append(count);
   checkby=checkby.drop([count]);
   if count % 4000==0:
    print("count ",count)
    #print("Community check set for testing lower throttle check Merge also ",Name)
  count+=1;
 checkby=checkby.reset_index()
 print("End Community Check for ",Name)
 #print("DropRows")
 #print(len(DropRows))
 #print("DropRows")
 return checkby
 
 
 
 

def KeywordGen(NewDataFrame,MatchType,SearchChan):
 MatchType=MatchType.upper();
 SearchChan=SearchChan.lower();
 print("Starting KeywordGen for ",SearchChan,"Match Type ",MatchType);
 Failed_Rows=[];
 Campaign_Name=[];
 Adgroup=[];
 Keyword=[];
 Match_Type=[];
 Status=[];
 Bid=[];
 Final_URL=[];

 Title1A=[];
 Title2A=[];
 Title3A=[];
 TextA=[];
 Text2A=[];
 Path1A=[];
 Path2A=[];
 
 Title1B=[];
 Title2B=[];
 Title3B=[];
 TextB=[];
 Text2B=[];
 Path1B=[];
 Path2B=[];
 
 count=0;
 hilecount=len(NewDataFrame['Market ID']);
 Keyword_conv="none"; 
 MatchType_Conv=0;
 set_bid=.30;
 if type(MaintatanceVar)=="<class 'int'>":
  hilecount=MaintatanceVar;
 while count < hilecount:
  try:
   if SearchChan=="google":
    Campaign_Nameing_Conv=Market_LookUp.google[NewDataFrame['Market ID'][count]]
    Campaign_Nameing_Conv=Campaign_Nameing_Conv.replace("SBMM",MatchType)
    if MatchType=="SBMM":
     Keyword_conv=NewDataFrame['Community Name'][count]
     Keyword_conv=Keyword_conv.replace(" "," +")
     Keyword_conv=Keyword_conv.replace("+55+","55+")
     Keyword_conv=Keyword_conv.replace("+-","-")
     Keyword_conv=Keyword_conv.replace("+G +& +I ","G&I ")
     Keyword_conv="+"+Keyword_conv
     if len(Keyword_conv)<12:
      Keyword_conv=Keyword_conv+" Community"
     MatchType_Conv="Broad"
    if MatchType=="SB":
     Campaign_Nameing_Conv=Campaign_Nameing_Conv.replace("_GPPC403","_GPPC402")
     Keyword_conv=NewDataFrame['Community Name'][count]
     MatchType_Conv="Broad"
    if MatchType=="SX":
     Campaign_Nameing_Conv=Campaign_Nameing_Conv.replace("_GPPC403","_GPPC401")
     Keyword_conv=NewDataFrame['Community Name'][count]
     MatchType_Conv="Exact"
     set_bid=.35;
   if SearchChan=="bing":
    Campaign_Nameing_Conv=Market_LookUp.bing[NewDataFrame['Market ID'][count]]
    Campaign_Nameing_Conv=Campaign_Nameing_Conv.replace("SBMM",MatchType)
    if MatchType=="SB":
     Campaign_Nameing_Conv=Campaign_Nameing_Conv.replace("_MSM203","_MSM202")
     Keyword_conv=NewDataFrame['Community Name'][count]
     MatchType_Conv="Broad"
    if MatchType=="SX":
     Campaign_Nameing_Conv=Campaign_Nameing_Conv.replace("_MSM203","_MSM201")
     Keyword_conv=NewDataFrame['Community Name'][count]
     MatchType_Conv="Exact"
     set_bid=.35;
    if MatchType=="SBMM":
     Keyword_conv=NewDataFrame['Community Name'][count]
     Keyword_conv=Keyword_conv.replace(" "," +")
     Keyword_conv=Keyword_conv.replace("+55+","55+")
     Keyword_conv=Keyword_conv.replace("+-","-")
     Keyword_conv=Keyword_conv.replace("+G +& +I","G&I ")
     Keyword_conv="+"+Keyword_conv
     if len(Keyword_conv)<12:
      Keyword_conv=Keyword_conv+" Community"
     MatchType_Conv="Broad"
   Campaign_Name.append(Campaign_Nameing_Conv);
   AdgroupNaming_conv=str(NewDataFrame['City'][count])+str("_")+str(NewDataFrame['State'][count])+str(">")+str(NewDataFrame['Market ID'][count])+str(">")+str(NewDataFrame['Community Name'][count])+str(">")+str(NewDataFrame['Community Id'][count])           
   Adgroup.append(AdgroupNaming_conv)
   Keyword.append(Keyword_conv)
   Match_Type.append(MatchType_Conv)
   Status.append("Active")
   Bid.append(set_bid)
   Title1A_Name_Conv=NewDataFrame['Community Name'][count]
   if len(Title1A_Name_Conv)>29:
    Title1A_Name_Conv=Title1A_Name_Conv[:Title1A_Name_Conv.find("at")-1]
   if len(Title1A_Name_Conv)>29:
    Title1A_Name_Conv=Title1A_Name_Conv[:Title1A_Name_Conv.find(" ",2)]
   if len(Title1A_Name_Conv)< 20:
    Title1A_Name_Conv=Title1A_Name_Conv+" New Homes" 
   Title1A.append(Title1A_Name_Conv)
   Title2A_conv=NewDataFrame['City'][count]
   if len(Title2A_conv)<12:
    Title2A_conv=Title2A_conv+" New Homes for sale"   
   elif len(Title2A_conv)<20:
     Title2A_conv=Title2A_conv+" New Homes"
   elif len(Title2A_conv)<25:
     Title2A_conv=Title2A_conv+" Homes"
   Title2A.append(Title2A_conv)
        
   Title3A.append("Schedule a New Home Tour Today")
   TextA.append("Find your family a perfect new home at Legacy at East Greenwich 55+ in Clarksboro, NJ!")
   Text2A.append("New Homes offer security, energy efficiency, and peace of mind. Skip the remodel, Buy New!")
   Path1A_conv=NewDataFrame['City'][count].replace(" ","-")
   if len(Path1A_conv)>15:
    Path1A_conv=Path1A_conv.replace("-","")
    Path1A_conv=Path1A_conv.replace("North","N")
    Path1A_conv=Path1A_conv.replace("South","S")
    Path1A_conv=Path1A_conv.replace("West","W")
    Path1A_conv=Path1A_conv.replace("East","E")
    Path1A_conv=Path1A_conv.replace("Viejo","")
    Path1A_conv=Path1A_conv.replace("Parkland","Pklnd")
    Path1A_conv=Path1A_conv.replace("Park","Pk")
    Path1A_conv=Path1A_conv.replace("Township","Twnshp")
    Path1A_conv=Path1A_conv.replace("Springs","Spngs")
    Path1A_conv=Path1A_conv.replace("Beach","Bch")
    Path1A_conv=Path1A_conv.replace("Gardens","Gdns")
    Path1A_conv=Path1A_conv.replace("Point","Pt")
    Path1A_conv=Path1A_conv.replace("Heights","Hghts")
    Path1A_conv=Path1A_conv.replace("Plains","Plns")
    Path1A_conv=Path1A_conv.replace("Valley","Vlly")
    Path1A_conv=Path1A_conv.replace("Lake","lk")
    Path1A_conv=Path1A_conv.replace("Estates","Est")
    Path1A_conv=Path1A_conv.replace("Collection","")
    Path1A_conv=Path1A_conv.replace("Vistoso","")
    Path1A_conv=Path1A_conv.replace("Station","STA")
    Path1A_conv=Path1A_conv.replace("and","&")
   Path1A.append(Path1A_conv)
   Path2A.append("New Homes")
   Final_URL.append("https://www.newhomesource.com/community/"+NewDataFrame['State'][count].lower()+NewDataFrame['City'][count].replace(" ","-").lower())
        
  except:
   NewDataFrame=NewDataFrame.drop([count])
  count+=1;
  
 GoogleKWFrame={"Campaign Name":Campaign_Name,"Ad Group":Adgroup,"Keyword":Keyword,"Match type":Match_Type,"Status":Status,"Max CPC":Bid} 
 GoogleKWFrame=pandas.DataFrame(GoogleKWFrame)
 GoogleAdFrameA={"Campaign Name":Campaign_Name,"Ad Group":Adgroup,"Headline 1":Title1A,"Headline 2":Title2A,"Headline 3":Title3A,\
                "Description":TextA,"Description 2":Text2A,"Path 1":Path1A,"Path 2":Path2A,"Final URL":Final_URL,"Status":Status}
 GoogleAdFrameB={"Campaign Name":Campaign_Name,"Ad Group":Adgroup,"Headline 1":Title1A,"Headline 2":Title2A,"Headline 3":Title3A,\
                "Description":TextA,"Description 2":Text2A,"Path 1":Path1A,"Path 2":Path2A,"Final URL":Final_URL,"Status":Status}
 GoogleAdFrameA=pandas.DataFrame(GoogleAdFrameA)
 GoogleAdFrameB=pandas.DataFrame(GoogleAdFrameB)
 BingKWFrame={"Campaign Name":Campaign_Name,"Ad Group":Adgroup,"Keyword":Keyword,"Match type":Match_Type,"Status":Status,"Bid":Bid} 
 BingAdFrameA={"Campaign Name":Campaign_Name,"Ad Group":Adgroup,"Title Part 1":Title1A,"Title Part 2":Title2A,"Title Part 3":Title3A,\
                "Text":TextA,"Text Part 2":Text2A,"Path 1":Path1A,"Path 2":Path2A,"Final URL":Final_URL,"Status":Status}
 BingAdFrameB={"Campaign Name":Campaign_Name,"Ad Group":Adgroup,"Title Part 1":Title1A,"Title Part 2":Title2A,"Title Part 3":Title3A,\
                "Text":TextA,"Text Part 2":Text2A,"Path 1":Path1A,"Path 2":Path2A,"Final URL":Final_URL,"Status":Status}
 BingKWFrame=pandas.DataFrame(BingKWFrame)
 BingAdFrameA=pandas.DataFrame(BingAdFrameA)
 BingAdFrameB=pandas.DataFrame(BingAdFrameB)
 
 

 if SearchChan=="google":
  if MatchType=='SBMM':
   print("In KeywordGen google SBMM ")
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleKeywords/GoogleBMMKW')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleKWFrame.to_excel(writer)
   writer.save()
   
  
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionA/GoogleAdsVersionABMM')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleAdFrameA.to_excel(writer)
   writer.save()
   
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionB/GoogleAdsVersionBBMM/')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleAdFrameB.to_excel(writer)
   writer.save()
   
    
  if MatchType=='SB':
   print("In KeywordGen google SB ")
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleKeywords/GoogleBroadKW')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleKWFrame.to_excel(writer)
   writer.save()
   
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionA/GoogleAdsVersionABroad')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleAdFrameA.to_excel(writer)
   writer.save()
     
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionB/GoogleAdsVersionBBroad')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleAdFrameB.to_excel(writer)
   writer.save()
   
     
  if MatchType=='SX':
   print("In KeywordGen google SX ")
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleKeywords/GoogleExactKW')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleKWFrame.to_excel(writer)
   writer.save() 
   
 
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionA/GoogleAdsVersionAExact')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleAdFrameA.to_excel(writer)
   writer.save()
   
      
   os.chdir('/app/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionB/GoogleAdsVersionBExact')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   GoogleAdFrameB.to_excel(writer)
   writer.save()
   
     
 if SearchChan=="bing":
  if MatchType=='SBMM':
   print("In KeywordGen bing SBMM ")
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingKW/BingKWBMM')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingKWFrame.to_excel(writer)
   writer.save()
   
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsAtype/BingAdsAtypeBMM')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingAdFrameA.to_excel(writer)
   writer.save()
   
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsBtype/BingAdsBtypeBMM')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingAdFrameB.to_excel(writer)
   writer.save()
   
   
      
  if MatchType=='SB':
   print("In KeywordGen bing SB ")
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingKW/BingKWBroad')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingKWFrame.to_excel(writer)
   writer.save()
   
   
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsAtype/BingAdsAtypeBroad')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingAdFrameA.to_excel(writer)
   writer.save()
     
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsBtype/BingAdsBtypeBroad')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingAdFrameB.to_excel(writer)
   writer.save()
   
    
  if MatchType=='SX':
   print("In KeywordGen bing SX ")
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingKW/BingKWExact')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingKWFrame.to_excel(writer)
   writer.save()
   
      
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsAtype/BingAdsAtypeExact')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingAdFrameA.to_excel(writer)
   writer.save()
   
  
   os.chdir('/app/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsBtype/BingAdsBtypeExact')
   writer=pandas.ExcelWriter('DefaultSheet.xlsx')
   BingAdFrameB.to_excel(writer)
   writer.save()
   
    
def initialCommUpdatProcess():
 global IsCommUpdateRunning
  
 os.chdir('/app/Sheets/CommunityUpdates/currentCommunities')
 WorkingCommunities=pandas.read_excel('WorkingCommunities').drop([0,1,2,3])
 WorkingCommunities.columns=WorkingCommunities.iloc[0]
 WorkingCommunities=WorkingCommunities.drop([4])
 WorkingCommunities=LoadCommunities(WorkingCommunities,'Builder Name','Community Id','City','Zip')
 if IsCommValid!="Valid":
  return IsCommValid
 WorkingGoogleEOF=WorkingGoogle()    
 WorkingBingEOF=WorkingBing()
 
 WorkingCommunities['Community Id']
 WorkingGoogleEOF['Final URL']  
 WorkingBingEOF['Final Url']
 

 googleURLS=MergeURLs(WorkingGoogleEOF['Final URL'],"Google");
 bingURLS=MergeURLs(WorkingBingEOF['Final Url'],"Bing");
 WorkingCommunities=filterNonParticipators(WorkingCommunities);
 #WorkingCommunities=filterNonParticipators(filterNonParticipators(filterNonParticipators(WorkingCommunities)));
 
 
 
 NewGoogle=communityCheck(WorkingCommunities,googleURLS,"Google");
 NewBing=communityCheck(WorkingCommunities,bingURLS,"Bing");

 
 KeywordGen(NewGoogle,"sbmm","google")
 KeywordGen(NewGoogle,"sb","google")
 KeywordGen(NewGoogle,"sx","google")
 KeywordGen(NewBing,"sbmm","bing")
 KeywordGen(NewBing,"sb","bing")
 KeywordGen(NewBing,"sx","bing")
 
                       
   
 print("Main ")
 os.chdir('/app/Sheets/CommunityUpdates/Bing/currentBing')
  
 
 TheSampleText=WorkingBingEOF
 TheSamplefile=open('TheSampleText.txt','w+') 
 TheSamplefile.write(TheSampleText.to_string())
 TheSamplefile.close()
 
 
 os.chdir('/app/Sheets/')
 storeRequest=open('RequestsVsResponses.txt','a+')
 storeRequest.write("Response , ")
 storeRequest.close() 
 storeRequest=open('RequestsVsResponses.txt','r+')
 storeRequest.close()
 
  
  
 
 
 print("END OF ASYNC FILE LOAD.....................................................................")
 sys.exit()
 return "finished"





   
   

  
  
  
  



