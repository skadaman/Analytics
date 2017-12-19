# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:37:41 2017

@author: sxk94
"""
''' imports data set and creates month year columns'''
import pandas as pd 

infile=r'\\ascendanalytics.com\users\sxk94\Python\GaryGraphs\Data\Castaic Output.xlsx'
raw=pd.read_excel(infile, header=0,)
raw['Month']=raw.Date.apply(lambda x: x.month)
raw['Year']=raw.Date.apply(lambda x: x.year)
del(raw['Sum'])
raw['Unit']=raw['RSR'].apply(lambda x: x[0:14])

netgen=raw[['Date',1,2,3,4,5,6,7,8,9,10,
                    11,12,13,14,15,16,17,18,19,
                    20,21,22,23,24,
                    'Year','Month','Unit']].groupby([
                    'Date','Year','Month','Unit']).agg('sum')
netgen=pd.DataFrame(netgen.to_records())

''' Loop that iterates over the months and years to create heatmap graphic 
for every unit month and year, pumping is negative so that will be included'''

import matplotlib.ticker as ticker
import matplotlib.cm as cm


import matplotlib.pyplot as plt



combinations = netgen.loc[:,['Month', 'Year', 'Unit']].drop_duplicates()
for i,row in combinations.iterrows():
    m = row['Month']
    y = row['Year']
    g = row['Unit']

    sub_mode = netgen.loc[(netgen['Month']==m)&(netgen['Year']==y)&(netgen['Unit']==g),
                        ['Date','1','2','3','4','5','6','7','8','9','10',
                    '11','12','13','14','15','16','17','18','19',
                    '20','21','22','23','24']]
    sub_mode=sub_mode.set_index('Date')
    fig = plt.figure()
    fig, ax = plt.subplots( figsize=(12.5,15))
    
    heatmap=ax.imshow(sub_mode, cmap=cm.coolwarm)
    ax.set_xticklabels(sub_mode.columns)
    ax.set_yticklabels(sub_mode.index)
    tick_spacing=1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_title("Heat Map of Generation for " + g)
    ax.grid( which='major',color='w', linestyle='-', linewidth=2)
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Day in Month '+str(m)+'/'+str(y))
    cbar=fig.colorbar(heatmap,ticks=list(range(-300,300,25)),
                      orientation='horizontal')
    

    plt.savefig(r'\\ascendanalytics.com\users\sxk94\Python\GaryGraphs\Output\Heatmaps\Heatmap_'+g+' '+str(y)+str(m)+'.png')
    plt.close('all')
    plt.clf()
