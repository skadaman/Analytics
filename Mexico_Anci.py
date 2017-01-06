# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:13:42 2016

@author: Sebastian Kadamany
"""

import pandas as pd
import glob
import datetime

files= glob.iglob("/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Anci/*.csv")
df_list = []
d=pd.to_datetime('01/29/2016', format='%m/%d/%Y')
for filename in files:
    df=pd.read_csv(filename, header=6)
    df['Date']=d
    d+=datetime.timedelta(days=1)
    df_list.append(df)
    raw_anci=pd.concat(df_list)
raw_anci.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/Full_anci.csv')
raw_anci.info()
raw_anci.head()
raw_anci.tail()
raw_anci.columns=['Hour','Zone','Type','Price','Date']
raw_anci['Month']= raw_anci.Date.apply(lambda x : x.month)
raw_anci['Day']= raw_anci.Date.apply(lambda x : x.day)
raw_anci['Dollars']=raw_anci.Price/20


#zone1=raw_anci.loc[raw_anci.Zone=="ZONA 1"]
#zone1.drop('Zone')

z1_secondaryreserve=raw_anci.query("Type=='Reserva de regulacion secundaria' and Zone=='ZONA 1'")
z1_secondaryreserve['DT']=pd.date_range(start='1/29/2016', periods=7872, freq='H')
z1_secondaryreserve.index=z1_secondaryreserve['DT']
z1_secondaryreserve.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/anci_SecondaryReserve.csv')

z1_10minspin=raw_anci.query("Type=='Reserva rodante de 10 minutos' and Zone=='ZONA 1'")
z1_10minspin['DT']=pd.date_range(start='1/29/2016', periods=7872, freq='H')
z1_10minspin.index=z1_10minspin['DT']
z1_10minspin.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/anci_10minspin.csv')

z1_10minnospin=raw_anci.query("Type=='Reserva no rodante de 10 minutos' and Zone=='ZONA 1'")
z1_10minnospin['DT']=pd.date_range(start='1/29/2016', periods=7872, freq='H')
z1_10minnospin.index=z1_10minnospin['DT']
z1_10minnospin.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/anci_10minnospin.csv')

z1_suppspin=raw_anci.query("Type=='Reserva rodante suplementaria' and Zone=='ZONA 1'")
z1_suppspin['DT']=pd.date_range(start='1/29/2016', periods=7872, freq='H')
z1_suppspin.index=z1_suppspin['DT']
z1_suppspin.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/anci_suppspin.csv')

z1_suppnospin=raw_anci.query("Type=='Reserva no rodante suplementarias' and Zone=='ZONA 1'")
z1_suppnospin['DT']=pd.date_range(start='1/29/2016', periods=7872, freq='H')
z1_suppnospin.index=z1_suppnospin['DT']
z1_suppnospin.to_csv('/Users/Work/Desktop/NWE/Python_Scripts/Mexico/anci_suppnosppin.csv')


hourlymean_SR=z1_secondaryreserve[['Hour','Dollars']].groupby('Hour').agg({'Dollars':'mean'})
hourlymean_10spin=z1_10minspin[['Hour','Dollars']].groupby('Hour').agg({'Dollars':'mean'})
hourlymean_10nospin=z1_10minnospin[['Hour','Dollars']].groupby('Hour').agg({'Dollars':'mean'})
hourlymean_suppspin=z1_suppspin[['Hour','Dollars']].groupby('Hour').agg({'Dollars':'mean'})
hourlymean_suppnospin=z1_suppnospin[['Hour','Dollars']].groupby('Hour').agg({'Dollars':'mean'})

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.plot(hourlymean_SR.index,hourlymean_SR.Dollars,label='Supplementary Reserve')
plt.plot(hourlymean_10spin.index,hourlymean_10spin.Dollars, label='10Min Spin')

plt.legend(loc=4)
plt.title("Hourly Mean Price in U.S Dollars")
plt.xlabel("Hours")
plt.ylabel("U.S Dollars per MWh")
plt.xticks([1,6,12,18,24])
plt.tight_layout(h_pad=.25,w_pad=.75) 
plt.savefig('/Users/Work/Desktop/Mex_Anci1.png', bbox_inches="tight", bpi=120)


plt.plot(hourlymean_10nospin.index,hourlymean_10nospin.Dollars,label='10Min NoSpin')
plt.plot(hourlymean_suppspin.index,hourlymean_suppspin.Dollars, label='Supplementary Spinn')
plt.plot(hourlymean_suppnospin.index,hourlymean_suppnospin.Dollars, label="Supplementary NoSpin")
plt.legend(loc=2)
plt.title("Hourly Mean Price in U.S Dollars")
plt.xlabel("Hours")
plt.ylabel("U.S Dollars per MWh")
plt.xticks([1,6,12,18,24])
plt.tight_layout(h_pad=.25,w_pad=.75) 
plt.savefig('/Users/Work/Desktop/Mex_Anci2.png', bbox_inches="tight", bpi=120)

fig, ax= plt.subplots()
ax.plot(z1_secondaryreserve.index,z1_secondaryreserve.Dollars)
fig.autofmt_xdate()
plt.ylabel('Prices in Dollars')
plt.title('Secondary Reserve Prices Zone 1')
plt.savefig('/Users/Work/Desktop/Mex_Anci6.png', bbox_inches="tight", bpi=120)

fig, ax= plt.subplots()
ax.plot(z1_10minspin.index,z1_10minspin.Dollars,color='r')
fig.autofmt_xdate()
plt.ylabel('Prices in Dollars')
plt.title('10min Spinning Reserve Prices Zone 1')
plt.savefig('/Users/Work/Desktop/Mex_Anci5.png', bbox_inches="tight", bpi=120)

fig, ax= plt.subplots()
ax.plot(z1_10minnospin.index,z1_10minnospin.Dollars, color='b')
fig.autofmt_xdate()
plt.ylabel('Prices in Dollars')
plt.title('10min Non-Spinning Reserve Prices Zone 1')
plt.savefig('/Users/Work/Desktop/Mex_Anci4.png', bbox_inches="tight", bpi=120)

fig, ax= plt.subplots()
ax.plot(z1_suppspin.index,z1_suppspin.Dollars, color='g')
fig.autofmt_xdate()
plt.ylabel('Prices in Dollars')
plt.title('Supplemetary Spinning Reserve Prices Zone 1')
plt.savefig('/Users/Work/Desktop/Mex_Anci3.png', bbox_inches="tight", bpi=120)