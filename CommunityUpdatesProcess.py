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

SheetsAreLoaded=None; 
IsCommValid=None;
IsGoogleValid=None;
IsBingValid=None;


Market_Lookup={
308:"Seattle-Bellevue_WA>308>SBMM>Community_MSM203"
19:"Tucson_AZ>19>SBMM>Community_MSM203"
166:"St. Louis_MO>166>SBMM>Community_MSM203"
290:"Tyler_TX>290>SBMM>Community_MSM203"
40:"Stockton-Lodi_CA>40>SBMM>Community_MSM203"
41:"Vallejo-Napa_CA>41>SBMM>Community_MSM203"
310:"Tacoma_WA>310>SBMM>Community_MSM203"
216:"Syracuse_NY>216>SBMM>Community_MSM203"
251:"York_PA>251>SBMM>Community_MSM203"
79:"Tallahassee_FL>79>SBMM>Community_MSM203"
350:"Sussex_DE>350>SBMM>Community_MSM203"
131:"Shreveport-Bossier City_LA>131>SBMM>Community_MSM203"
309:"Spokane-Couer d Alene_WA>309>SBMM>Community_MSM203"
347:"Sussex County_NJ>347>SBMM>Community_MSM203"
233:"Tulsa_OK>233>SBMM>Community_MSM203"
80:"Tampa-St. Petersburg_FL>80>SBMM>Community_MSM203"
247:"Scranton-Wilkes-Barre_PA>247>SBMM>Community_MSM203"
343:"Somerset County_NJ>343>SBMM>Community_MSM203"
120:"Wichita_KS>120>SBMM>Community_MSM203"
228:"Toledo_OH>228>SBMM>Community_MSM203"
258:"Sumter_SC>258>SBMM>Community_MSM203"
183:"Wilmington_NC>183>SBMM>Community_MSM203"
116:"South Bend_IN>116>SBMM>Community_MSM203"
353:"St. George_UT>353>SBMM>Community_MSM203"
311:"Yakima_WA>311>SBMM>Community_MSM203"
292:"Waco_TX>292>SBMM>Community_MSM203"
321:"Washington-Fond du Lac_WI>321>SBMM>Community_MSM203"
288:"Sherman-Denison_TX>288>SBMM>Community_MSM203"
197:"Warren County_NJ>197>SBMM>Community_MSM203"
354:"Valdosta_GA>354>SBMM>Community_MSM203"
249:"State College_PA>249>SBMM>Community_MSM203"
43:"Visalia_CA>43>SBMM>Community_MSM203"
61:"Wilmington-Newark_DE>61>SBMM>Community_MSM203"
141:"Worcester_MA>141>SBMM>Community_MSM203"
11:"Tuscaloosa_AL>11>SBMM>Community_MSM203"
42:"Ventura_CA>42>SBMM>Community_MSM203"
88:"Savannah_GA>88>SBMM>Community_MSM203"
59:"Waterbury_CT>59>SBMM>Community_MSM203"
362:"Ozaukee-Sheboygan_WI>362>SBMM>Community_MSM203"
342:"Passaic County_NJ>342>SBMM>Community_MSM203"
295:"Salt Lake City-Ogden_UT>295>SBMM>Community_MSM203"
294:"Provo-Orem_UT>294>SBMM>Community_MSM203"
320:"Racine_WI>320>SBMM>Community_MSM203"
75:"Panama City_FL>75>SBMM>Community_MSM203"
202:"Santa Fe_NM>202>SBMM>Community_MSM203"
38:"Santa Cruz_CA>38>SBMM>Community_MSM203"
215:"Rochester_NY>215>SBMM>Community_MSM203"
181:"Raleigh-Durham-Chapel Hill_NC>181>SBMM>Community_MSM203"
76:"Pensacola_FL>76>SBMM>Community_MSM203"
37:"Santa Barbara_CA>37>SBMM>Community_MSM203"
34:"San Francisco_CA>34>SBMM>Community_MSM203"
204:"Reno_NV>204>SBMM>Community_MSM203"
244:"Philadelphia_PA>244>SBMM>Community_MSM203"
300:"Richmond-Petersburg_VA>300>SBMM>Community_MSM203"
365:"Outer Banks_NC>365>SBMM>Community_MSM203"
32:"Salinas_CA>32>SBMM>Community_MSM203"
287:"San Antonio_TX>287>SBMM>Community_MSM203"
252:"Providence-Warwick_RI>252>SBMM>Community_MSM203"
332:"Poconos_PA>332>SBMM>Community_MSM203"
81:"Palm Beach County_FL>81>SBMM>Community_MSM203"
39:"Santa Rosa_CA>39>SBMM>Community_MSM203"
77:"Punta Gorda_FL>77>SBMM>Community_MSM203"
31:"Sacramento_CA>31>SBMM>Community_MSM203"
36:"San Luis Obispo_CA>36>SBMM>Community_MSM203"
284:"Rio Grande Valley_TX>284>SBMM>Community_MSM203"
307:"Richland_WA>307>SBMM>Community_MSM203"
246:"Reading_PA>246>SBMM>Community_MSM203"
245:"Pittsburgh_PA>245>SBMM>Community_MSM203"
74:"Orlando_FL>74>SBMM>Community_MSM203"
69:"Lakeland-Winter Haven_FL>69>SBMM>Community_MSM203"
232:"Oklahoma City_OK>232>SBMM>Community_MSM203"
243:"Lancaster_PA>243>SBMM>Community_MSM203"
348:"Morris County_NJ>348>SBMM>Community_MSM203"
136:"Lawrence_MA>136>SBMM>Community_MSM203"
9:"Mobile_AL>9>SBMM>Community_MSM203"
26:"Modesto_CA>26>SBMM>Community_MSM203"
319:"Milwaukee-Waukesha_WI>319>SBMM>Community_MSM203"
24:"Los Angeles_CA>24>SBMM>Community_MSM203"
170:"Memphis_TN>170>SBMM>Community_MSM203"
333:"Ocean City_MD>333>SBMM>Community_MSM203"
316:"Kenosha_WI>316>SBMM>Community_MSM203"
318:"Madison_WI>318>SBMM>Community_MSM203"
198:"Mercer County_NJ>198>SBMM>Community_MSM203"
299:"Norfolk-Newport News_VA>299>SBMM>Community_MSM203"
15:"Little Rock_AR>15>SBMM>Community_MSM203"
158:"Minneapolis-St. Paul_MN>158>SBMM>Community_MSM203"
358:"Morgantown_WV>358>SBMM>Community_MSM203"
213:"New York_NY>213>SBMM>Community_MSM203"
127:"Lafayette_LA>127>SBMM>Community_MSM203"
306:"Olympia_WA>306>SBMM>Community_MSM203"
265:"Knoxville_TN>265>SBMM>Community_MSM203"
281:"Laredo_TX>281>SBMM>Community_MSM203"
10:"Montgomery_AL>10>SBMM>Community_MSM203"
352:"Imperial Valley_CA>352>SBMM>Community_MSM203"
71:"Miami-Dade County_FL>71>SBMM>Community_MSM203"
65:"Martin-St. Lucie-Okeechobee Counties_FL>65>SBMM>Community_MSM203"
203:"Las Vegas_NV>203>SBMM>Community_MSM203"
195:"Middlesex County_NJ>195>SBMM>Community_MSM203"
188:"Omaha_NE>188>SBMM>Community_MSM203"
266:"Nashville_TN>266>SBMM>Community_MSM203"
72:"Naples_FL>72>SBMM>Community_MSM203"
212:"Nassau-Suffolk_NY>212>SBMM>Community_MSM203"
155:"Lansing_MI>155>SBMM>Community_MSM203"
8:"Huntsville_AL>8>SBMM>Community_MSM203"
154:"Kalamazoo-Battle Creek_MI>154>SBMM>Community_MSM203"
329:"Indian River County_FL>329>SBMM>Community_MSM203"
28:"Orange County_CA>28>SBMM>Community_MSM203"
345:"Ocean County_NJ>345>SBMM>Community_MSM203"
257:"Myrtle Beach_SC>257>SBMM>Community_MSM203"
87:"Macon_GA>87>SBMM>Community_MSM203"
169:"Jackson_MS>169>SBMM>Community_MSM203"
163:"Kansas City_MO>163>SBMM>Community_MSM203"
196:"Monmouth County_NJ>196>SBMM>Community_MSM203"
27:"Oakland-Alameda_CA>27>SBMM>Community_MSM203"
194:"Hudson County_NJ>194>SBMM>Community_MSM203"
344:"Hunterdon County_NJ>344>SBMM>Community_MSM203"
130:"New Orleans_LA>130>SBMM>Community_MSM203"
180:"Jacksonville_NC>180>SBMM>Community_MSM203"
70:"Melbourne_FL>70>SBMM>Community_MSM203"
361:"Logan_UT>361>SBMM>Community_MSM203"
280:"Killeen_TX>280>SBMM>Community_MSM203"
226:"Mansfield_OH>226>SBMM>Community_MSM203"
151:"Flint_MI>151>SBMM>Community_MSM203"
335:"Hilton Head_SC>335>SBMM>Community_MSM203"
67:"Gainesville_FL>67>SBMM>Community_MSM203"
51:"Greeley_CO>51>SBMM>Community_MSM203"
66:"Fort Walton Beach_FL>66>SBMM>Community_MSM203"
55:"Hartford_CT>55>SBMM>Community_MSM203"
278:"Galveston_TX>278>SBMM>Community_MSM203"
64:"Fort Myers_FL>64>SBMM>Community_MSM203"
49:"Fort Collins-Loveland_CO>49>SBMM>Community_MSM203"
356:"Hawaii Island_HI>356>SBMM>Community_MSM203"
168:"Hattiesburg_MS>168>SBMM>Community_MSM203"
152:"Grand Rapids_MI>152>SBMM>Community_MSM203"
256:"Greenville-Spartanburg_SC>256>SBMM>Community_MSM203"
241:"Harrisburg_PA>241>SBMM>Community_MSM203"
178:"Greenville_NC>178>SBMM>Community_MSM203"
60:"Dover_DE>60>SBMM>Community_MSM203"
54:"Danbury_CT>54>SBMM>Community_MSM203"
62:"Daytona Beach_FL>62>SBMM>Community_MSM203"
177:"Greensboro-Winston-Salem-High Point_NC>177>SBMM>Community_MSM203"
4:"Decatur_AL>4>SBMM>Community_MSM203"
144:"Hagerstown_MD>144>SBMM>Community_MSM203"
276:"El Paso_TX>276>SBMM>Community_MSM203"
223:"Dayton-Springfield_OH>223>SBMM>Community_MSM203"
208:"Dutchess County_NY>208>SBMM>Community_MSM203"
277:"Fort Worth_TX>277>SBMM>Community_MSM203"
210:"Glens Falls_NY>210>SBMM>Community_MSM203"
150:"Detroit_MI>150>SBMM>Community_MSM203"
349:"Essex County_NJ>349>SBMM>Community_MSM203"
351:"Eastern Shore_MD>351>SBMM>Community_MSM203"
175:"Fayetteville_NC>175>SBMM>Community_MSM203"
111:"Gary_IN>111>SBMM>Community_MSM203"
23:"Fresno_CA>23>SBMM>Community_MSM203"
17:"Flagstaff_AZ>17>SBMM>Community_MSM203"
176:"Goldsboro_NC>176>SBMM>Community_MSM203"
110:"Fort Wayne_IN>110>SBMM>Community_MSM203"
179:"Hickory_NC>179>SBMM>Community_MSM203"
255:"Florence_SC>255>SBMM>Community_MSM203"
5:"Dothan_AL>5>SBMM>Community_MSM203"
125:"Baton Rouge_LA>125>SBMM>Community_MSM203"
83:"Athens_GA>83>SBMM>Community_MSM203"
200:"Albuquerque_NM>200>SBMM>Community_MSM203"
2:"Anniston_AL>2>SBMM>Community_MSM203"
82:"Albany_GA>82>SBMM>Community_MSM203"
199:"Cumberland County_NJ>199>SBMM>Community_MSM203"
142:"Baltimore_MD>142>SBMM>Community_MSM203"
100:"Chicago_IL>100>SBMM>Community_MSM203"
261:"Chattanooga_TN>261>SBMM>Community_MSM203"
85:"Augusta_GA>85>SBMM>Community_MSM203"
218:"Akron_OH>218>SBMM>Community_MSM203"
107:"Bloomington_IN>107>SBMM>Community_MSM203"
364:"Blacksburg_VA>364>SBMM>Community_MSM203"
205:"Albany-Saratoga_NY>205>SBMM>Community_MSM203"
53:"Bridgeport_CT>53>SBMM>Community_MSM203"
269:"Austin_TX>269>SBMM>Community_MSM203"
238:"Allentown-Bethlehem_PA>238>SBMM>Community_MSM203"
174:"Charlotte_NC>174>SBMM>Community_MSM203"
296:"Charlottesville_VA>296>SBMM>Community_MSM203"
271:"Brazoria_TX>271>SBMM>Community_MSM203"
192:"Atlantic-Cape May_NJ>192>SBMM>Community_MSM203"
207:"Buffalo-Niagara Falls_NY>207>SBMM>Community_MSM203"
273:"Bryan-College Station_TX>273>SBMM>Community_MSM203"
305:"Bremerton_WA>305>SBMM>Community_MSM203"
46:"Boulder-Longmont_CO>46>SBMM>Community_MSM203"
270:"Beaumont_TX>270>SBMM>Community_MSM203"
220:"Cincinnati_OH>220>SBMM>Community_MSM203"
3:"Birmingham_AL>3>SBMM>Community_MSM203"
193:"Bergen County_NJ>193>SBMM>Community_MSM203"
337:"Corvallis_OR>337>SBMM>Community_MSM203"
47:"Colorado Springs_CO>47>SBMM>Community_MSM203"
330:"Auburn-Opelika_AL>330>SBMM>Community_MSM203"
21:"Bakersfield_CA>21>SBMM>Community_MSM203"
173:"Asheville_NC>173>SBMM>Community_MSM203"
133:"Boston_MA>133>SBMM>Community_MSM203"
219:"Canton-Massillon_OH>219>SBMM>Community_MSM203"
96:"Boise_ID>96>SBMM>Community_MSM203"
341:"Sandusky_OH>341>SBMM>Community_MSM203"
285:"Midland-Odessa_TX>285>SBMM>Community_MSM203"
283:"Lubbock_TX>283>SBMM>Community_MSM203"
234:"Eugene-Springfield_OR>234>SBMM>Community_MSM203"
91:"Des Moines_IA>91>SBMM>Community_MSM203"
86:"Columbus_GA>86>SBMM>Community_MSM203"
340:"Central Oregon_OR>340>SBMM>Community_MSM203"
132:"Barnstable-Yarmouth_MA>132>SBMM>Community_MSM203"
326:"Wheeling_WV>326>SBMM>Community_MSM203"
289:"Texarkana_TX>289>SBMM>Community_MSM203"
370:"Steamboat Springs_CO>370>SBMM>Community_MSM203"
366:"Southern Pines_NC>366>SBMM>Community_MSM203"
235:"Medford-Ashland_OR>235>SBMM>Community_MSM203"
122:"Louisville_KY>122>SBMM>Community_MSM203"
121:"Lexington_KY>121>SBMM>Community_MSM203"
355:"Kauai_HI>355>SBMM>Community_MSM203"
161:"Columbia-Jefferson City_MO>161>SBMM>Community_MSM203"
22:"Chico_CA>22>SBMM>Community_MSM203"
334:"Summit-Rocky Mountains_CO>334>SBMM>Community_MSM203"
58:"Stamford-Norwalk_CT>58>SBMM>Community_MSM203"
298:"Lynchburg_VA>298>SBMM>Community_MSM203"
367:"Harrisonburg_VA>367>SBMM>Community_MSM203"
63:"Broward County-Ft. Lauderdale_FL>63>SBMM>Community_MSM203"
346:"Union County_NJ>346>SBMM>Community_MSM203"
25:"Merced_CA>25>SBMM>Community_MSM203"
268:"Amarillo_TX>268>SBMM>Community_MSM203"
105:"Rockford_IL>105>SBMM>Community_MSM203"
12:"Fayetteville_AR>12>SBMM>Community_MSM203"
108:"Elkhart-Goshen_IN>108>SBMM>Community_MSM203"
182:"Rocky Mount_NC>182>SBMM>Community_MSM203"
56:"New Haven-Meriden_CT>56>SBMM>Community_MSM203"
360:"Tupelo_MS>360>SBMM>Community_MSM203"
229:"Youngstown-Warren_OH>229>SBMM>Community_MSM203"
162:"Joplin_MO>162>SBMM>Community_MSM203"
227:"Steubenville_OH>227>SBMM>Community_MSM203"
171:"Billings_ND>171>SBMM>Community_MSM203"
97:"South East Idaho_ID>97>SBMM>Community_MSM203"
323:"Charleston_WV>323>SBMM>Community_MSM203"
52:"Pueblo_CO>52>SBMM>Community_MSM203"
297:"Danville_VA>297>SBMM>Community_MSM203"
201:"Las Cruces_NM>201>SBMM>Community_MSM203"
301:"Roanoke_VA>301>SBMM>Community_MSM203"
123:"Owensboro_KY>123>SBMM>Community_MSM203"
264:"Johnson City-Bristol_TN>264>SBMM>Community_MSM203"
7:"Gadsden_AL>7>SBMM>Community_MSM203"
336:"Hot Springs_AR>336>SBMM>Community_MSM203"
282:"Longview_TX>282>SBMM>Community_MSM203"
164:"Springfield_MO>164>SBMM>Community_MSM203"
126:"Houma_LA>126>SBMM>Community_MSM203"
339:"Eastern Arizona_AZ>339>SBMM>Community_MSM203"
109:"Evansville_IN>109>SBMM>Community_MSM203"
324:"Huntington-Ashland_WV>324>SBMM>Community_MSM203"
263:"Jackson_TN>263>SBMM>Community_MSM203"
217:"Utica-Rome_NY>217>SBMM>Community_MSM203"
206:"Binghamton_NY>206>SBMM>Community_MSM203"
124:"Alexandria_LA>124>SBMM>Community_MSM203"
128:"Lake Charles_LA>128>SBMM>Community_MSM203"
14:"Jonesboro_AR>14>SBMM>Community_MSM203"
50:"Grand Junction_CO>50>SBMM>Community_MSM203"
328:"Cheyenne_WY>328>SBMM>Community_MSM203"
291:"Victoria_TX>291>SBMM>Community_MSM203"
274:"Corpus Christi_TX>274>SBMM>Community_MSM203"
129:"Monroe_LA>129>SBMM>Community_MSM203"
325:"Parkersburg-Marietta_OH>325>SBMM>Community_MSM203"
363:"Durango_CO>363>SBMM>Community_MSM203"
286:"San Angelo_TX>286>SBMM>Community_MSM203"
13:"Fort Smith_AR>13>SBMM>Community_MSM203"
89:"Oahu_HI>89>SBMM>Community_MSM203"
149:"Benton Harbor_MI>149>SBMM>Community_MSM203"
262:"Clarksville_TN>262>SBMM>Community_MSM203"
191:"Portsmouth_NH>191>SBMM>Community_MSM203"
156:"Traverse_MI>156>SBMM>Community_MSM203"
267:"Abilene_TX>267>SBMM>Community_MSM203"
167:"Biloxi_MS>167>SBMM>Community_MSM203"
102:"Decatur_IL>102>SBMM>Community_MSM203"
303:"Burlington_VT>303>SBMM>Community_MSM203"
94:"Sioux City_IA>94>SBMM>Community_MSM203"
239:"Altoona_PA>239>SBMM>Community_MSM203"
113:"Kokomo_IN>113>SBMM>Community_MSM203"
374:"Prescott_AZ>374>SBMM>Community_MSM203"
90:"Cedar Rapids_IA>90>SBMM>Community_MSM203"
93:"Iowa City_IA>93>SBMM>Community_MSM203"
95:"Waterloo-Cedar Falls_IA>95>SBMM>Community_MSM203"
1:"Anchorage_AK>1>SBMM>Community_MSM203"
369:"Kingman-Lake Havasu City_AZ>369>SBMM>Community_MSM203"
357:"Wailuku_HI>357>SBMM>Community_MSM203"
237:"Salem_OR>237>SBMM>Community_MSM203"
30:"Riverside-San Bernardino_CA>30>SBMM>Community_MSM203"
253:"Charleston_SC>253>SBMM>Community_MSM203"
73:"Ocala_FL>73>SBMM>Community_MSM203"
214:"Orange County_NY>214>SBMM>Community_MSM203"
18:"Phoenix-Mesa_AZ>18>SBMM>Community_MSM203"
112:"Indianapolis_IN>112>SBMM>Community_MSM203"
236:"Portland-Vancouver_OR>236>SBMM>Community_MSM203"
78:"Sarasota-Bradenton_FL>78>SBMM>Community_MSM203"
68:"Jacksonville-St. Augustine_FL>68>SBMM>Community_MSM203"
35:"San Jose_CA>35>SBMM>Community_MSM203"
275:"Dallas_TX>275>SBMM>Community_MSM203"
84:"Atlanta_GA>84>SBMM>Community_MSM203"
279:"Houston_TX>279>SBMM>Community_MSM203"
33:"San Diego_CA>33>SBMM>Community_MSM203"
302:"Washington_DC>302>SBMM>Community_MSM203"
148:"Ann Arbor_MI>148>SBMM>Community_MSM203"
222:"Columbus_OH>222>SBMM>Community_MSM203"
304:"Bellingham_WA>304>SBMM>Community_MSM203"
48:"Denver_CO>48>SBMM>Community_MSM203"
221:"Cleveland_OH>221>SBMM>Community_MSM203"
254:"Columbia_SC>254>SBMM>Community_MSM203"
}


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
   
   print("communities basic import done")
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
   print("Google basic import done")
   return  WorkingGoogle
  
def WorkingBing():
  os.chdir('/app/Sheets/CommunityUpdates/Bing/currentBing')
  WorkingBing=pandas.read_excel('WorkingBing')
  IsBingValid=CheckSheetData("WorkingBing",WorkingBing,'Campaign','Ad Group','Title Part 1','Final Url')
  if IsBingValid!='Valid':
   return IsBingValid
  WorkingBing=pandas.DataFrame(WorkingBing,columns=['Campaign','Ad Group','Final Url']).drop(0)
  print("Bing basic import done")
  return WorkingBing

def filterNonParticipators(FrameToBeFiltered):
 print("Start Filter ",FrameToBeFiltered['Builder Name'].count()," rows")
 FilteredFrame=FrameToBeFiltered
 CatchDiscards=[];
 FilterString='(communityname=,Q5),(Clayton Homes,B5),(Clayton Homes,A5),\
 (Oakwoord Homes,A5),(Oakwoord Homes,B5),(G & I Homes,A5),(G & I Homes,B5),\
 (Craftmark Homes,A5),(Craftmark Homes,B5),(Freedom Homes,A5),(Freedom Homes,B5),\
 (Crossland Homes,A5),(Crossland Homes,B5)),(Luv Homes,A5),(Luv Homes,B5),\
 (International Homes,A5),(International Homes,B5),(Clayton,A5);'
 count=5;
 while count < len(numpy.array(FrameToBeFiltered['Brand Name'])):
  if FilterString.find(str(numpy.array(FrameToBeFiltered['Brand Name'])[[count]]))>-1:
   CatchDiscards.append(count)
  if FilterString.find(str(numpy.array(FrameToBeFiltered['Community Id'])[[count]]))>-1:
   CatchDiscards.append(count)
  if FilterString.find(str(numpy.array(FrameToBeFiltered['Builder Name'])[[count]]))>-1:
   CatchDiscards.append(count)
  count+=1; 
  if len(CatchDiscards)!=0:
   count2=0;
   while count2<len(CatchDiscards):
    print("Entered the second while loop count2= ",count2)
    FilteredFrame=FilteredFrame.drop(CatchDiscards[count2])
    count2+=1;                  
 print("End Filter") 
 return FilteredFrame 
 
def MergeURLs(chan,chan2):
 print("MergeURLs() start for ",chan2)
 URLS="A";
 count=0;
 if chan2=="Bing":
  count=1;
 while count < 10000:
 #while count < chan.count():
  URLS=URLS+chan[count]
  if count % 20000 == 0:
   print(chan2," _ ",count)
   print("Low count setting in MergeURLS nonfunctional")
  count+=1
 print("end MergeURLs() for ",chan2)
 return URLS
 
def communityCheck(checkby,checkin,Name):
 print("Start Community Check for ",Name)
 checkby=checkby.reset_index()
 count=0;
 DropRows=[];
 while count < 1000
 #while count < checkby['Community Id'].count():
  if checkin.find(str(checkby['Community Id'][count]))>-1:
   DropRows.append(count);
   checkby=checkby.drop([count]);
   if count % 10==0:
    print("count ",count)
    print("Community check set for testing lower throttle check Merge also ")
  count+=1;
 checkby=checkby.reset_index()
 print("End Community Check for ",Name)
 return checkby
 
def initialCommUpdatProcess():
 os.chdir('/app/Sheets/CommunityUpdates/currentCommunities')
 WorkingCommunities=pandas.read_excel('WorkingCommunities').drop([0,1,2,3])
 WorkingCommunities.columns=WorkingCommunities.iloc[0]
 WorkingCommunities=WorkingCommunities.drop([4])
 WorkingCommunities=LoadCommunities(WorkingCommunities,'Builder Name','Community Id','City','Zip')
 if IsCommValid!="Valid":
  return IsCommValid
 print("WorkingCommunities LoadCommunitites has run ",IsCommValid)
 WorkingGoogleEOF=WorkingGoogle()    
 WorkingBingEOF=WorkingBing()
 
 WorkingCommunities['Community Id']
 WorkingGoogleEOF['Final URL']  
 WorkingBingEOF['Final Url']
 

 googleURLS=MergeURLs(WorkingGoogleEOF['Final URL'],"Google");
 bingURLS=MergeURLs(WorkingBingEOF['Final Url'],"Bing");
 WorkingCommunities=filterNonParticipators(WorkingCommunities);
 
 NewGoogle=communityCheck(WorkingCommunities,googleURLS,"Google");
 NewBing=communityCheck(WorkingCommunities,bingURLS,"Bing");
 
 def KeywordGen(NewDataFrame,MatchType,SearchChan):
  print("Starting KeywordGen for ",SearchChan,"Match Type ",MatchType);
  Campaign_Name=[];
  Adgroup=[];
  Keyword=[];
  Match_Type=[];
  Status=[];
  Bid=[];
  
  #Market_Lookup={5:"Dog"};
  
  MatchType=MatchType.lower();
  count=0;
  print("len(NewDataFrame['Market ID'])",len(NewDataFrame['Market ID']));
  #print("NewDataFrame['Market ID'].count()",NewDataFrame['Market ID'].count();
  while count < 6:
  #while count < len(NewDataFrame['Market ID']):
   if MatchType!="sx":
    NewDataFrame['Market ID']
    print("count ",count)
    print("Market_Lookup[308] ",Market_Lookup[308])
   count+=1; 
  print("Ending KeywordGen for ",SearchChan,"Match Type ",MatchType);  
 print(" Before Keyworden") 
 KeywordGen(NewGoogle,"sbmm","NewGoogle")
 KeywordGen(NewBing,"sbmm","NewBing") 
 print(" Before Keyworden") 
    
   
  
  
  
  
 
 
 
 TheSampleText=WorkingBingEOF
 TheSamplefile=open('TheSampleText.txt','w+') 
 TheSamplefile.write(TheSampleText.to_string())
 TheSamplefile.close()
 
 print("END OF ASYNC FILE LOAD.....................................................................")
 return "finished"





   
   

  
  
  
  



