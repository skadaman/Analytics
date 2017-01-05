# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 08:35:54 2016

@author: Sebastian Kadamany
"""


import pandas as pd
import glob
import datetime
#File concatenation
#files= glob.iglob("/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Power/*.csv")
#df_list = []
#d=pd.to_datetime('01/29/2016', format='%m/%d/%Y')
#for filename in files:
#    df=pd.read_csv(filename, header=6)
#    df['Date']=d
#    d+=datetime.timedelta(days=1)
#    df_list.append(df)
#    raw_power=pd.concat(df_list)
#raw_power.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Full_Power.csv')

############ read concatenated file and format columns ############

raw_power=pd.read_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Full_Power.csv',index_col=0)
raw_power.info()
raw_power.head()
raw_power.tail()
raw_power.columns=['Hour','Node','Price','EnergyComponent','LossComponent','Congestion','Date']
raw_power['Month']= raw_power.Date.apply(lambda x: x[5:7])
raw_power['Day']= raw_power.Date.apply(lambda x : x[8:])
raw_power['Dollars']=raw_power.Price/20
raw_power['Year']=2016

#raw_power.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Full_PowerDollars.csv')

Guadalajara=raw_power.query("Node=='03GDU-230'")
Guadalajara['DT']=pd.date_range(start='1/29/2016', periods=7872, freq='H')
Guadalajara.index=Guadalajara['DT']
Guadalajara.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Guadalajara_Power.csv')


Potosi=raw_power.query("Node=='03SLP-230'")
Potosi['DT']=pd.date_range(start='1/29/2016', periods=7872, freq='H')
Potosi.index=Potosi['DT']
Potosi.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Potosi_Power.csv')


######### Plots for Node  1 #############
MeanGuadalajara=Guadalajara[['Hour','Dollars','Month']].groupby(['Month','Hour']).agg({'Dollars':'mean'})
MeanGuadalajara.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/GuadalajaraMean_Power.csv')
MeanPotosi=Potosi[['Hour','Dollars','Month']].groupby('Month','Hour').Agg({'Dollars':'mean'})
JanMeanG=MeanGuadalajara.loc['01':'01']
FebMeanG=MeanGuadalajara.loc['02':'02']
MarMeanG=MeanGuadalajara.loc['03':'03']
AprMeanG=MeanGuadalajara.loc['04':'04']
MayMeanG=MeanGuadalajara.loc['05':'05']
JunMeanG=MeanGuadalajara.loc['06':'06']
JulMeanG=MeanGuadalajara.loc['07':'07']
AugMeanG=MeanGuadalajara.loc['08':'08']
SepMeanG=MeanGuadalajara.loc['09':'09']
OctMeanG=MeanGuadalajara.loc['10':'10']
NovMeanG=MeanGuadalajara.loc['11':'11']
DecMeanG=MeanGuadalajara.loc['12':'12']
import matplotlib.pyplot as plt
plt.style.use('ggplot')
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12)) = plt.subplots(nrows=4, ncols=3, sharey='all')
ax1.bar(range(1,25),JanMeanG.Dollars)
ax2.bar(range(1,25),FebMeanG.Dollars)
ax3.bar(range(1,25),MarMeanG.Dollars)
ax4.bar(range(1,25),AprMeanG.Dollars)
ax5.bar(range(1,25),MayMeanG.Dollars)
ax6.bar(range(1,25),JunMeanG.Dollars)
ax7.bar(range(1,25),JulMeanG.Dollars)
ax8.bar(range(1,25),AugMeanG.Dollars)
ax9.bar(range(1,25),SepMeanG.Dollars)
ax10.bar(range(1,25),OctMeanG.Dollars)
ax11.bar(range(1,25),NovMeanG.Dollars)
ax12.bar(range(1,25),DecMeanG.Dollars)
ax1.set_title("January")
ax2.set_title("February")
ax3.set_title("March")
ax4.set_title("April")
ax5.set_title("May")
ax6.set_title("June")
ax7.set_title("July")
ax8.set_title("August")
ax9.set_title("September")
ax10.set_title("October")
ax11.set_title("November")
ax12.set_title("December")
ax1.set_xticks([])
ax2.set_xticks([])
ax3.set_xticks([])
ax4.set_xticks([])
ax5.set_xticks([])
ax6.set_xticks([])
ax7.set_xticks([])
ax8.set_xticks([])
ax9.set_xticks([])
ax10.set_xticks([1,6,12,18,24])
ax11.set_xticks([1,6,12,18,24])
ax12.set_xticks([1,6,12,18,24])
plt.suptitle("Gudalajara Node Avg. Price of Energy by Hour and Month", y=.4, fontsize=16)
ax4.set_ylabel('Average Price Day Ahead (USD)')
ax11.set_xlabel("Daily Hours")
plt.subplots_adjust(bottom=0.6,top=2.2)
plt.savefig('/Users/Work/Desktop/AverageGuadalajara_MonthHour.png', bbox_inches="tight", bpi=120)


######## Creating plots for Node 2 #####
MeanPotosi=Potosi[['Hour','Dollars','Month']].groupby(['Month','Hour']).agg({'Dollars':'mean'})
JanMeanS=MeanPotosi.loc['01':'01']
FebMeanS=MeanPotosi.loc['02':'02']
MarMeanS=MeanPotosi.loc['03':'03']
AprMeanS=MeanPotosi.loc['04':'04']
MayMeanS=MeanPotosi.loc['05':'05']
JunMeanS=MeanPotosi.loc['06':'06']
JulMeanS=MeanPotosi.loc['07':'07']
AugMeanS=MeanPotosi.loc['08':'08']
SepMeanS=MeanPotosi.loc['09':'09']
OctMeanS=MeanPotosi.loc['10':'10']
NovMeanS=MeanPotosi.loc['11':'11']
DecMeanS=MeanPotosi.loc['12':'12']

fig, ((ax1,ax2,ax3), (ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12)) = plt.subplots(nrows=4, ncols=3, sharey='all')
ax1.bar(range(1,25),JanMeanS.Dollars,facecolor='g')
ax2.bar(range(1,25),FebMeanS.Dollars,facecolor='g')
ax3.bar(range(1,25),MarMeanS.Dollars,facecolor='g')
ax4.bar(range(1,25),AprMeanS.Dollars,facecolor='g')
ax5.bar(range(1,25),MayMeanS.Dollars,facecolor='g')
ax6.bar(range(1,25),JunMeanS.Dollars,facecolor='g')
ax7.bar(range(1,25),JulMeanS.Dollars,facecolor='g')
ax8.bar(range(1,25),AugMeanS.Dollars,facecolor='g')
ax9.bar(range(1,25),SepMeanS.Dollars,facecolor='g')
ax10.bar(range(1,25),OctMeanS.Dollars,facecolor='g')
ax11.bar(range(1,25),NovMeanS.Dollars,facecolor='g')
ax12.bar(range(1,25),DecMeanS.Dollars,facecolor='g')
ax1.set_title("January")
ax2.set_title("February")
ax3.set_title("March")
ax4.set_title("April")
ax5.set_title("May")
ax6.set_title("June")
ax7.set_title("July")
ax8.set_title("August")
ax9.set_title("September")
ax10.set_title("October")
ax11.set_title("November")
ax12.set_title("December")
ax1.set_xticks([])
ax2.set_xticks([])
ax3.set_xticks([])
ax4.set_xticks([])
ax5.set_xticks([])
ax6.set_xticks([])
ax7.set_xticks([])
ax8.set_xticks([])
ax9.set_xticks([])
ax10.set_xticks([1,6,12,18,24])
ax11.set_xticks([1,6,12,18,24])
ax12.set_xticks([1,6,12,18,24])
plt.suptitle("San Luis Potosi Node Avg. Price of Energy by Hour and Month", y=.4, fontsize=16)
ax4.set_ylabel('Average Price Day Ahead (USD)')
ax11.set_xlabel("Daily Hours")
plt.subplots_adjust(bottom=0.6,top=2.2)
plt.savefig('/Users/Work/Desktop/AveragePotosi_MonthHour.png', bbox_inches="tight", bpi=120)

""" 
Creating a plot of the prices by date and hour and daily/monthly volatility 
"""
##### Vols by Month
aggregations={'Dollars':{'Average':'mean','SDev':'std'}}
Gstd=Guadalajara[['Month','Dollars']].groupby('Month').agg(aggregations)
Gstd['Vol']=Gstd.Dollars.SDev/Gstd.Dollars.Average

Pstd=Potosi[['Month','Dollars']].groupby('Month').agg(aggregations)
Pstd['Vol']=Pstd.Dollars.SDev/Pstd.Dollars.Average
import numpy as np


x=np.arange(1,len(Gstd.Vol)+1)
m,b=np.polyfit(x=x,y=Gstd.Vol, deg=1)
plt.scatter(range(1,13),Gstd.Vol)
plt.plot(x,m*x+b)
plt.ylabel('Volatility (Standard Dev / Average)')
plt.xlabel('Months 2016')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.title('Volatility at Guadalajara Node')
plt.savefig('/Users/Work/Desktop/VolatilityGuadalajara_Monthly.png', bbox_inches="tight", bpi=120)

x=np.arange(1,len(Pstd.Vol)+1)
m,b=np.polyfit(x=x,y=Pstd.Vol, deg=1)
plt.scatter(range(1,13),Pstd.Vol)
plt.plot(x,m*x+b)
plt.ylabel('Volatility (Standard Dev / Average)')
plt.xlabel('Months 2016')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.title('Volatility at San Luis Potosi Node')
plt.savefig('/Users/Work/Desktop/VolatilityPotosi_Monthly.png', bbox_inches="tight", bpi=120)





###### Vols by month day #####
GstdD=Guadalajara[['Month','Dollars','Day']].groupby(['Month','Day']).agg(aggregations)
GstdD['Vol']=GstdD.Dollars.SDev/GstdD.Dollars.Average

PstdD=Potosi[['Month','Dollars','Day']].groupby(['Month','Day']).agg(aggregations)
PstdD['Vol']=PstdD.Dollars.SDev/PstdD.Dollars.Average

######## Creating plots for Node 2 #####

###Still need to do node1 may not be needed"
JanVolsS=PstdD.loc['01':'01']
FebVolsS=PstdD.loc['02':'02']
MarVolsS=PstdD.loc['03':'03']
AprVolsS=PstdD.loc['04':'04']
MayVolsS=PstdD.loc['05':'05']
JunVolsS=PstdD.loc['06':'06']
JulVolsS=PstdD.loc['07':'07']
AugVolsS=PstdD.loc['08':'08']
SepVolsS=PstdD.loc['09':'09']
OctVolsS=PstdD.loc['10':'10']
NovVolsS=PstdD.loc['11':'11']
DecVolsS=PstdD.loc['12':'12']

fig, ((ax1,ax2,ax3), (ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12)) = plt.subplots(nrows=4, ncols=3, sharey='all')
ax1.scatter(range(29,32),JanVolsS.Vol,color='g')
ax2.scatter(range(1,30),FebVolsS.Vol,color='g')
ax3.scatter(range(1,32),MarVolsS.Vol,color='g')
ax4.scatter(range(1,31),AprVolsS.Vol,color='g')
ax5.scatter(range(1,32),MayVolsS.Vol,color='g')
ax6.scatter(range(1,31),JunVolsS.Vol,color='g')
ax7.scatter(range(1,32),JulVolsS.Vol,color='g')
ax8.scatter(range(1,32),AugVolsS.Vol,color='g')
ax9.scatter(range(1,31),SepVolsS.Vol,color='g')
ax10.scatter(range(1,32),OctVolsS.Vol,color='g')
ax11.scatter(range(1,31),NovVolsS.Vol,color='g')
ax12.scatter(range(1,22),DecVolsS.Vol,color='g')
ax1.set_title("January")
ax2.set_title("February")
ax3.set_title("March")
ax4.set_title("April")
ax5.set_title("May")
ax6.set_title("June")
ax7.set_title("July")
ax8.set_title("August")
ax9.set_title("September")
ax10.set_title("October")
ax11.set_title("November")
ax12.set_title("December")
ax1.set_xticks([])
ax2.set_xticks([])
ax3.set_xticks([])
ax4.set_xticks([])
ax5.set_xticks([])
ax6.set_xticks([])
ax7.set_xticks([])
ax8.set_xticks([])
ax9.set_xticks([])
ax10.set_xticks([1,5,10,15,20,25,31])
ax11.set_xticks([1,5,10,15,20,25,31])
ax12.set_xticks([1,5,10,15,20,25,31])
ax1.set_yticks([0,.1,.2,.3,.4,.5])
plt.suptitle("San Luis Potosi Volatility of Energy Price by Month Day", y=.4, fontsize=16)
ax4.set_ylabel('Volatility Std/Avg')
ax11.set_xlabel("Days")
plt.subplots_adjust(bottom=0.6,top=2.2)

###Timeseries of DA prices####
fig, ax=plt.subplots()
ax.plot(Guadalajara.index,Guadalajara.Dollars,color='blue')
fig.autofmt_xdate()
plt.ylabel('Prices in Dollars')
plt.title('DA Prices at Guadalajara Node')
plt.savefig('/Users/Work/Desktop/DAPriceGuadalajara_Monthly.png', bbox_inches="tight", bpi=120)


fig, ax=plt.subplots()
ax.plot(Potosi.index,Potosi.Dollars,color='g')
fig.autofmt_xdate()
plt.ylabel('Prices in Dollars')
plt.title('DA Prices at San Luis Potosi Node')
plt.savefig('/Users/Work/Desktop/DAPricePotosi_Monthly.png', bbox_inches="tight", bpi=120)




    

