import glob
import numpy
import scipy
import pandas
import BidOpAssist
import fileHandler
from flask import Flask, Markup, render_template, request
import os
import psycopg2


def initialCommUpdatProcess():
  
  #os.chdir('/app/Sheets')
  #print(os.getcwd())
  #print(os.listdir())
  print("***************************************************")
  os.chdir('/app/Sheets/CommunityUpdates/currentCommunities')
  WorkingCommunities=open('WorkingCommunities').read()
  print(os.listdir())
  print(open('WorkingCommunities'))
  print(WorkingCommunities)
  
  
  



