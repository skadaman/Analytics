# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:37:47 2016

@author: Work
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:36:29 2016

@author: Work
"""

# This script outputs data for creating a set of rules for picking energy markets to sell in

import pandas as pd
import datetime
#******UPDATED to use DA data. RT version is called ModuleRules.py**********
# Read in data, this data set contains LMP prices for Aberdeen and a surrogate node as well
# as Ancilliary data. There is a gap starting Jun2015 to  the end  of Jul2015. This code will
# use the Aberdeen data when available over the surrogate.

#Read in data
FullData=pd.read_csv('/Users/Work/Desktop/NWE/Raw_Data/NWEDAFULL.csv')
FullData.info()
FullData.head()
#Get month and hour columns
FullData['textdate']=FullData['Interval'].astype(str)
FullData['textdate']=FullData['textdate'].str.strip()
FullData['Date']=pd.to_datetime(FullData['textdate'], format='%d%b%y:%H:%M', errors='coerce')
FullData['Hour']= FullData.Date.apply(lambda x : x.hour)
FullData['Month']= FullData.Date.apply(lambda x : x.month)
FullData['Day']= FullData.Date.apply(lambda x : x.day)
FullData['Weekday'] = FullData['Date'].apply(lambda x: x.weekday())
#Weekday data
WkData=FullData[FullData.Weekday < 5]
#WeekEnd
WkendData=FullData[FullData.Weekday > 4]
#Aggregate, get the mean of the Aberdeen data for all prices.
##WeekdY
MeanWkData=WkData[['Month','Hour','LMP','RegUP','RegDN','Spin','Supp']].groupby(['Month','Hour']).mean()
MeanWkData.head(12)
##Weekend
MeanWkendData=WkendData[['Month','Hour','LMP','RegUP','RegDN','Spin','Supp']].groupby(['Month','Hour']).mean()
MeanWkendData.head(12)

#Create subsets of data for every month
#Weekday by month
janmeanwkda=MeanWkData.loc[1:1]
febmeanwkda=MeanWkData.loc[2:2]
marmeanwkda=MeanWkData.loc[3:3]
aprmeanwkda=MeanWkData.loc[4:4]
maymeanwkda=MeanWkData.loc[5:5]
junmeanwkda=MeanWkData.loc[6:6]
julmeanwkda=MeanWkData.loc[7:7]
augmeanwkda=MeanWkData.loc[8:8]
sepmeanwkda=MeanWkData.loc[9:9]
octmeanwkda=MeanWkData.loc[10:10]
novmeanwkda=MeanWkData.loc[11:11]
decmeanwkda=MeanWkData.loc[12:12]
#Weekend by month
janmeanwkndda=MeanWkendData.loc[1:1]
febmeanwkndda=MeanWkendData.loc[2:2]
marmeanwkndda=MeanWkendData.loc[3:3]
aprmeanwkndda=MeanWkendData.loc[4:4]
maymeanwkndda=MeanWkendData.loc[5:5]
junmeanwkndda=MeanWkendData.loc[6:6]
julmeanwkndda=MeanWkendData.loc[7:7]
augmeanwkndda=MeanWkendData.loc[8:8]
sepmeanwkndda=MeanWkendData.loc[9:9]
octmeanwkndda=MeanWkendData.loc[10:10]
novmeanwkndda=MeanWkendData.loc[11:11]
decmeanwkndda=MeanWkendData.loc[12:12]
#Export to csv
##Weekday
janmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/janmeanwkda.csv')
febmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/febmeanwkda.csv')
marmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/marmeanwkda.csv')
aprmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/aprmeanwkda.csv')
maymeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/maymeanwkda.csv')
junmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/junmeanwkda.csv')
julmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/julmeanwkda.csv')
augmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/augmeanwkda.csv')
sepmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/sepmeanwkda.csv')
octmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/octmeanwkda.csv')
novmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/novmeanwkda.csv')
decmeanwkda.to_csv('/Users/Work/Desktop/NWE/Output/decmeanwkda.csv')
##weekend
janmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/janmeanwkndda.csv')
febmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/febmeanwkndda.csv')
marmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/marmeanwkndda.csv')
aprmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/aprmeanwkndda.csv')
maymeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/maymeanwkndda.csv')
junmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/junmeanwkndda.csv')
julmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/julmeanwkndda.csv')
augmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/augmeanwkndda.csv')
sepmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/sepmeanwkndda.csv')
octmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/octmeanwkndda.csv')
novmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/novmeanwkndda.csv')
decmeanwkndda.to_csv('/Users/Work/Desktop/NWE/Output/decmeanwkndda.csv')

#**** Here the RT LMP data is brought in to create the probabilities for spikes***#
#Read in data
FullDataRT=pd.read_csv('/Users/Work/Desktop/NWE/Raw_Data/RT_NWE_FULL.csv')
FullDataRT.info()
FullDataRT.head()
#Get month and hour columns
FullDataRT['textdate']=FullDataRT['Interval'].astype(str)
FullDataRT['textdate']=FullDataRT['textdate'].str.strip()
FullDataRT['Date']=pd.to_datetime(FullDataRT['textdate'], format='%d%b%y:%H:%M', errors='coerce')
FullDataRT['Hour']= FullDataRT.Date.apply(lambda x : x.hour)
FullDataRT['Month']= FullDataRT.Date.apply(lambda x : x.month)
FullDataRT['Day']= FullDataRT.Date.apply(lambda x : x.day)
FullDataRT['Weekday'] = FullDataRT['Date'].apply(lambda x: x.weekday())
#Weekday data
WkDataRT=FullDataRT[FullDataRT.Weekday < 5]
#WeekEnd
WkendDataRT=FullDataRT[FullDataRT.Weekday > 4]
#Aggregate, get the mean of the Aberdeen data for all prices.
##WeekdY
MeanWkDataRT=WkDataRT[['Month','Hour','LMP','RegUP','RegDN','Spin','Supp']].groupby(['Month','Hour']).mean()
MeanWkDataRT.head(12)
##Weekend
MeanWkendDataRT=WkendDataRT[['Month','Hour','LMP','RegUP','RegDN','Spin','Supp']].groupby(['Month','Hour']).mean()
MeanWkendDataRT.head(12)
#***********************************************************#

#Spike frequency
##Weekday
WksubRT=WkDataRT[['Month','Hour','LMP']]
WksubRT['SpikeFlag']=0
WksubRT.ix[WksubRT.LMP>100,'SpikeFlag']=1
WkSpikesRT=WksubRT[['SpikeFlag','Month','Hour']].groupby(['Month','Hour']).sum()
##Weekday
WkendsubRT=WkendDataRT[['Month','Hour','LMP']]
WkendsubRT['SpikeFlag']=0
WkendsubRT.ix[WkendsubRT.LMP>100,'SpikeFlag']=1
WkendSpikesRT=WkendsubRT[['SpikeFlag','Month','Hour']].groupby(['Month','Hour']).sum()

WkSpikesRT.to_csv('/Users/Work/Desktop/NWE/Output/WkSpikes.csv')
WkendSpikesRT.to_csv('/Users/Work/Desktop/NWE/Output/WkendSpikes.csv')

#Spike mean by day month (probabilty)
##Weekday
WkSpikesmeanRT=WksubRT[['SpikeFlag','Month','Hour']].groupby(['Month','Hour']).mean()
#Weekend
WkendSpikesmeanRT=WkendsubRT[['SpikeFlag','Month','Hour']].groupby(['Month','Hour']).mean()

WkSpikesmeanRT.to_csv('/Users/Work/Desktop/NWE/Output/WkSpikesmean.csv')
WkendSpikesmeanRT.to_csv('/Users/Work/Desktop/NWE/Output/WkendSpikesmean.csv')
#Average Spike Price
WkSpikePriceRT=WksubRT.where(WksubRT.SpikeFlag==1).groupby(['Month','Hour']).mean()
WkendSpikePriceRT=WkendsubRT.where(WkendsubRT.SpikeFlag==1).groupby(['Month','Hour']).mean()

WkSpikePriceRT.to_csv('/Users/Work/Desktop/NWE/Output/WkSpikeprice.csv')
WkendSpikePriceRT.to_csv('/Users/Work/Desktop/NWE/Output/WkendSpikeprice.csv')


#************After this point we have data set with average DA Prices and RT Spike expected Prices*******
MeanWkData['ExpectedSpikeWk']=WkSpikesmeanRT.SpikeFlag*WkSpikePriceRT.LMP
MeanWkendData['ExpectedSpikeWkend']=WkendSpikesmeanRT.SpikeFlag*WkendSpikePriceRT.LMP

#**************** returns data set that specifies what to sell*******

#Set Generation Characteristics Parameters
FullGenHR=8.9 #Mbtu/MW
MidGenHR=9.5 #Mbtu/MW
MinGenHR=10.5 #Mbtu/MW
FullGenCap=18.4 #MW
MidGenCap=11.20 #MW
MinGenCap=4.0 #MW
VariableOM=7.0 #$/MWh
Outage=.05  # will be %
StrikePriceFull=33.70 #$/MWh
StrikePriceMid=33.50 #$/MWh
GasPrice=3 #$
PowerOn= 28 #$
PowerOff= 18 #$

#Weekday Gros Margin Columns
MeanWkData['GMregulation']= MeanWkData.RegUP*(FullGenHR-MinGenHR)+MidGenCap*(PowerOn-PowerOff)/2-(StrikePriceMid-MidGenCap)
MeanWkData['GMSpin']=(FullGenCap-MinGenCap)*MeanWkData.Spin-(MinGenCap*(MinGenHR*GasPrice-VariableOM))
MeanWkData['GMnonSpin']=FullGenCap*MeanWkData.Supp

#Weekend Gross Margin Columns 
MeanWkendData['GMregulation']= MeanWkendData.RegUP*(FullGenHR-MinGenHR)+MidGenCap*(PowerOn-PowerOff)/2-(StrikePriceMid-MidGenCap)
MeanWkendData['GMSpin']=(FullGenCap-MinGenCap)*MeanWkendData.Spin-(MinGenCap*(MinGenHR*GasPrice-VariableOM))
MeanWkendData['GMnonSpin']=FullGenCap*MeanWkendData.Supp

#Subset to Only GM prices and spike then select max column name 
GMWkData=MeanWkData[['GMregulation','GMSpin','GMnonSpin','ExpectedSpikeWk']]
GMWkendData=MeanWkendData[['GMregulation','GMSpin','GMnonSpin','ExpectedSpikeWkend']]

GMWkData['ExpectedSpikeWk']=GMWkData['ExpectedSpikeWk'].fillna(value=0)
GMWkendData['ExpectedSpikeWkend']=GMWkendData['ExpectedSpikeWkend'].fillna(value=0)

GMWkData['ScaledSpike']=GMWkData['ExpectedSpikeWk']*12
GMWkendData['ScaledSpike']=GMWkendData['ExpectedSpikeWkend']*12

GMWkData['Rule']=GMWkData.idxmax(axis=1)
GMWkendData['Rule']=GMWkendData.idxmax(axis=1)
#Create final CSV
GMWkData.to_csv('/Users/Work/Desktop/NWE/Output/WeekRules.csv')
GMWkendData.to_csv('/Users/Work/Desktop/NWE/Output/WeekendRules.csv')