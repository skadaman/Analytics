# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime

#Read in RT Prices
RTLMP=pd.read_csv('/Users/Work/Desktop/NWE/Raw_Data/RT_NWE_final100062016.csv')
RTLMP.head()
RTLMP.info()
#set the dates to right format
RTLMP['textdate']=RTLMP['Date'].astype(str)
RTLMP['textdate']=RTLMP['textdate'].str.strip()
#Slice the date into Day, Month, Hour Units
RTLMP['D']=pd.to_datetime(RTLMP['textdate'], format='%d%b%y:%H:%M', errors='coerce')
RTLMP['Hour']= RTLMP.D.apply(lambda x : x.hour)
RTLMP['Month']= RTLMP.D.apply(lambda x : x.month)
RTLMP['Day']= RTLMP.D.apply(lambda x : x.day)
PriceData=RTLMP[['LMP','Hour','Month','Day']]
PriceData=PriceData.dropna()
PriceData['SpikeFlag']=0
PriceData.ix[PriceData.LMP >= 100, 'SpikeFlag'] = 1
PriceData['SpikeFlag'].mean()
#Surrogate spikes graph
SurSpikes=PriceData.groupby(['Month','Hour']).agg({'SpikeFlag':'sum'})
Janspikessur=SurSpikes.loc[1:1]
Febspikessur=SurSpikes.loc[2:2]
Marspikessur=SurSpikes.loc[3:3]
Aprspikessur=SurSpikes.loc[4:4]
Mayspikessur=SurSpikes.loc[5:5]
Junspikessur=SurSpikes.loc[6:6]
Julspikessur=SurSpikes.loc[7:7]
Augspikessur=SurSpikes.loc[8:8]
Sepspikessur=SurSpikes.loc[9:9]
Octspikessur=SurSpikes.loc[10:10]
Novspikessur=SurSpikes.loc[11:11]
Decspikessur=SurSpikes.loc[12:12]
#Creates all subplots and titles
plt.style.use('ggplot')
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12)) = plt.subplots(nrows=4, ncols=3, sharey='all')
ax1.bar(range(0,24),Janspikessur.SpikeFlag)
ax2.bar(range(0,24),Febspikessur.SpikeFlag)
ax3.bar(range(0,24),Marspikessur.SpikeFlag)
ax4.bar(range(0,24),Aprspikessur.SpikeFlag)
ax5.bar(range(0,24),Mayspikessur.SpikeFlag)
ax6.bar(range(0,24),Junspikessur.SpikeFlag)
ax7.bar(range(0,24),Julspikessur.SpikeFlag)
ax8.bar(range(0,24),Augspikessur.SpikeFlag)
ax9.bar(range(0,24),Sepspikessur.SpikeFlag)
ax10.bar(range(0,24),Octspikessur.SpikeFlag)
ax11.bar(range(0,24),Novspikessur.SpikeFlag)
ax12.bar(range(0,24),Decspikessur.SpikeFlag)
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
ax1.set_xticks([0,6,12,18,23])
ax2.set_xticks([0,6,12,18,23])
ax3.set_xticks([0,6,12,18,23])
ax4.set_xticks([0,6,12,18,23])
ax5.set_xticks([0,6,12,18,23])
ax6.set_xticks([0,6,12,18,23])
ax7.set_xticks([0,6,12,18,23])
ax8.set_xticks([0,6,12,18,23])
ax9.set_xticks([0,6,12,18,23])
ax10.set_xticks([0,6,12,18,23])
ax11.set_xticks([0,6,12,18,23])
ax12.set_xticks([0,6,12,18,23])
ax1.set_yticks([0,10,20,30,40])
ax4.set_ylabel('Frequency')
ax11.set_xlabel("Hours")
plt.tight_layout(h_pad=.25,w_pad=.75) 
plt.savefig('/Users/Work/Desktop/finalspikeplot.png', bbox_inches="tight", bpi=120)