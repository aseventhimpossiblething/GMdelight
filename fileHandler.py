import BidOpAssist
from datetime import datetime
from flask import Flask, Markup, render_template, request
import glob
import os
import psycopg2
import pandas
import time
import xlrd
import io

def ValidatXLSXtime(arr):
        print("Crtitical Value ",time.time()-os.path.getctime(arr))
        Error=arr+" Generated an error check that filetype is xlsx"
        Valid=arr+" is valid"
        if time.time()-os.path.getctime(arr)>600000:
            print(Error)
        else:
            print(Valid)

def BidOpFileHandler():
    print("********************************BidOpFileHandler() flag 1************************************************")

    print("request.files______:   ",request.files)

    print("********************************BidOpFileHandler() flag 2************************************************")

    print("request.files['sheet']______:    ",request.files['sheet'])

    print("********************************BidOpFileHandler() flag 3*************************************************")

    print("request.files['sheet'].filename_______:     ",request.files['sheet'].filename)

   
    print("*********************************BidOpFileHandler() flag 4***********************************************")

    print("os.getcwd()_____: ",os.getcwd())

    print("********************************BidOpFileHandler() flag 5************************************************")

    print("os.listdir()____:",os.listdir())

    print("********************************BidOpFileHandler() flag 6************************************************")

    os.chdir('/app/Sheets')

    print("os.chdir(/Sheets)____:")

    print("********************************BidOpFileHandler() flag 7************************************************")

    print("os.getcwd()_____: ",os.getcwd())

    print("********************************BidOpFileHandler() flag 8************************************************")

    print("os.listdir()____:",os.listdir())

    print("********************************BidOpFileHandler() flag 9************************************************")

    request.files['sheet'].save(request.files['sheet'].filename)

    print("********************************BidOpFileHandler() flag 10************************************************")

    print("os.getcwd()____:",os.getcwd)

    print("********************************BidOpFileHandler() flag 11************************************************")

    print("os.listdir()____:",os.listdir())

    print("********************************BidOpFileHandler() flag 12************************************************")
    
    print("os.path.join('/app/Sheets',request.files['sheet'].filename))_____:",os.path.join('/app/Sheets',request.files['sheet'].filename))

    print("********************************BidOpFileHandler() flag 13************************************************")

    print("request.files['sheet'].filename_______:     ",request.files['sheet'].filename)

    print("********************************BidOpFileHandler() flag 14************************************************")

    print("request.files['sheet']______:    ",request.files['sheet'])

    print("********************************BidOpFileHandler() flag 15************************************************")

    print("request.files______:    ",request.files)

    print("**************************BidOpFileHandler() flag 16******************************************************")
    
    toscrn = "done"
    print("**************************BidOpFileHandler() flag 17******************************************************")
    

    
    return toscrn


def CommListFileHandler():
    print("********************************CommListFileHandler() flag 1************************************************")
    print(request.files)
    print(type(request.files))
   
     
    print("********************************CommListFileHandler() flag 1.2************************************************")
        
    n=3
    """     
    if request.files['Communities']:
        print("Stopped by if")
        return "stopped by if"
    """    
        
    #request.form
    #print(type("request.files['Communities']",request.files[Communities]))
        
    print("********************************CommListFileHandler() flag 1.3************************************************")      
    print("request.files____",request.files)
    print("********************************CommListFileHandler() flag 1.4************************************************")      
    print("request.files____",request.files['Communities'])
    print("********************************CommListFileHandler() flag 1.5************************************************")       
    print("request.files____",request.files['currentGoogle'])
    print("********************************CommListFileHandler() flag 1.6************************************************")    
    print("request.files____",request.files['currentBing']) 
    print("********************************CommListFileHandler() flag 1.7************************************************")        
    reqs=request.files,request.files['currentGoogle'],request.files['currentGoogle'],request.files['currentBing']  
    print("********************************CommListFileHandler() flag 1.8************************************************")
    print("type(request.files____)",type(request.files['currentBing']))
    print("Make string")
    print(str(request.files['currentBing']))      
    print(type(str(request.files['currentBing'])))
    print("<FileStorage: '' ('application/octet-stream')>")
    """    
    emptyObj="<FileStorage: '' ('application/octet-stream')>"    
    if emptyObj==str(request.files['currentBing']):
        return "Bing slot is empty"
    if emptyObj==str(request.files['currentGoogle']):
        return "Google slot is empty"
    if emptyObj==str(request.files['Communities']):
        return "Active Community slot is empty"
    """     
        
    
    #return "empty passed through"    
        
        
    
    print("********************************CommListFileHandler() flag 2************************************************")

    print("request.files['Communities']______:    ",request.files['Communities'])
    print("request.files['currentGoogle']______:    ",request.files['currentGoogle'])
    print("request.files['currentBing']______:    ",request.files['currentBing'])

    print("********************************CommListFileHandler() flag 3*************************************************")

    """
    def validateXLSX(arr): 
        print("Starting to Run Validate()")
        workingRequest=str(type(request.files[arr].filename.index('xlsx')))
        print("past setting working request")
        print("before Print of workingRequest")
        print(str(workingRequest))
        print(workingRequest)
        print("Just before If statement")
        if str(workingRequest)=="<class 'int'>":
            print("XLSX filetype valid")
            return "valid"
        else:
            print("Filetype not valid expecting XLSX")
            rval=arr+" "+"Invalid file type entered; expecting XLSX" 
            return rval
     """   
    """
    if validateXLSX('Communities')!="valid":
        return validateXLSX('Communities')
    if validateXLSX('currentGoogle')!="valid":
        return validateXLSX('currentGoogle')
    if validateXLSX('currentBing')!="valid":
        return validateXLSX('currentBing')
    """
    """
    workingRequest="+request.files['Communities'].filename.index('xlsx')+"
    if  workingRequest!="<class 'int'>":
       print("The File Entered as Community is not in the xlsx Filetype")
    
    print(request.files['Communities'].filename.index('xlsx'))
    workingRequest="+request.files['Communities'].filename.index('xlsx')+"
    print("6",type(6))
       return "The File Entered as Community List is not in the xlsx Filetype"
    
    if type(request.files['currentGoogle'].filename.index('xlsx'))!="<class 'int'>":
       print("The File Entered as Active Google List is not in the xlsx Filetype")
       return "The File Entered as Active Google List is not in the xlsx Filetype"
    
    print(request.files['Communities'].filename.index('xlsx'))
    workingRequest="+request.files['Communities'].filename.index('xlsx')+"
    print("6",type(6))
    
    if type(request.files['currentBing'].filename.index('xlsx'))!="<class 'int'>":
       print("The File Entered as Active Bing List is not in the xlsx Filetype")
       return "The File Entered as Active Bing List is not in the xlsx Filetype"
    """   
    
    """
    print(request.files['Communities'].filename.index('xlsx'))
    workingRequest="+request.files['Communities'].filename.index('xlsx')+"
    print("6",type(6))
    if workingRequest=="type(3)":
        print("<class 'int'>==type(3)")
    else:
        print("<class 'int'>==type(3)")
        
    """
    print("Empty Test")    
    emptyObj="<FileStorage: '' ('application/octet-stream')>"    
    if emptyObj==str(request.files['currentBing']):
        return "Bing slot is empty"
    if emptyObj==str(request.files['currentGoogle']):
        return "Google slot is empty"
    if emptyObj==str(request.files['Communities']):
        return "Active Community slot is empty"    
           
       
    print("*********************************CommListFileHandler() flag 4***********************************************")
    os.chdir('/app/Sheets/CommunityUpdates/currentCommunities')
    print("os.getcwd()_____: ",os.getcwd())
    request.files['Communities'].save(request.files['Communities'].filename)
    
    os.chdir('/app/Sheets/CommunityUpdates/Google/currentGoogle')
    print("os.getcwd()_____: ",os.getcwd())
    request.files['currentGoogle'].save(request.files['currentGoogle'].filename)
    
    os.chdir('/app/Sheets/CommunityUpdates/Bing/currentBing')
    print("os.getcwd()_____: ",os.getcwd())
    request.files['currentBing'].save(request.files['currentBing'].filename)

  
                                                   
    print("********************************CommListFileHandler() flag 5************************************************")
    os.chdir('/app/Sheets/CommunityUpdates/currentCommunities')
    print("os.listdir()____:",os.listdir())
    print(" ")
    os.chdir('/app/Sheets/CommunityUpdates/Google/currentGoogle')
    print("os.listdir()____:",os.listdir())
    
    print(" ")
    os.chdir('/app/Sheets/CommunityUpdates/Bing/currentBing')
    print("os.listdir()____:",os.listdir())
    
    

    print("********************************CommListFileHandler() flag 6************************************************")
    #1day=86400000
    """ 
    def ValidatXLSXtime(arr):
        print("Crtitical Value ",time.time()-os.path.getctime(recent))
        Error=arr+" Generated an error check that filetype is xlsx"
        Valid=arr+" is valid"
        if time.time()-os.path.getctime(recent)>600000:
            print(Error)
        else:
            print(Valid)
    """         
            
        
        
    
    
    
    print(datetime.now())
    os.chdir('/app/Sheets/CommunityUpdates/currentCommunities')
    recent=max(glob.glob('*.xlsx'), key=os.path.getctime)
    #print("recent____",recent)
    #print("os.listdir()____:",os.listdir())
    #print(os.path.getctime(recent))
    ValidatXLSXtime(recent)
    
    print(" ")
    
    os.chdir('/app/Sheets/CommunityUpdates/Google/currentGoogle')
    recent=max(glob.glob('*.xlsx'), key=os.path.getctime)
    #print("recent____",recent)
    #print("os.listdir()____:",os.listdir())
    #print(os.path.getctime(recent))
    ValidatXLSXtime(recent)
    print(" ")
    
    os.chdir('/app/Sheets/CommunityUpdates/Bing/currentBing')
    recent=max(glob.glob('*.xlsx'), key=os.path.getctime)
    #print("recent____",recent)
    #print("os.listdir()____:",os.listdir())
    #print(os.path.getctime(recent))
    ValidatXLSXtime(recent)
    print(" ")
    #print(datetime.now()-os.path.getctime(recent))
    #print("time.ctime(datetime.now())",os.path.getctime(recent))
    #print(datetime.fromtimestamp(os.path.getctime(recent)).strftime('%c'))
    #print(time.time())
    #print(time.time()-os.path.getctime(recent))
    #print("Validate Below")
    #ValidatXLSXtime(recent)


   
    print("********************************CommListFileHandler() flag 11************************************************")
       
  
    HTMLoutput=Markup('<p>Structured HTML</p>')
    
    toscrn = HTMLoutput
    print("**************************CommListFileHandler() flag 17******************************************************")
    

    
    return toscrn





    


    

    




    


    

    

