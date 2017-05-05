# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:14:41 2017

@author: sxk94

This is a script that creates Bokeh plots for prices and generation, created for the Austin Pilot.

"""
import pandas as pd
import numpy as np

#Import Data
raw_infile=r"\\ascendanalytics.com\main\Services\Austin\Shiny Plots\Data.csv"
RawData=pd.read_csv(raw_infile, skiprows=12,header=0)
#Clean the data
RawData=RawData.dropna()
RawData['Hour']=RawData.iloc[:,0].apply(lambda x: x[-5:-3].replace(" ",""))
RawData['Day']=RawData.iloc[:,0].apply(lambda x:str( x.strip()[:3].replace(" ","")))
RawData['SimRep']=RawData.iloc[:,1].apply(lambda x: str(x).replace(" ",""))
RawData['MPBasisPAP']=RawData.iloc[:,2].apply(
lambda x: float(x[1:].strip().replace("$","").replace("(","").replace(")","").replace(",",""))
)
RawData['MPHouston']=RawData.iloc[:,3].apply(
lambda x: float(x[1:].replace("$","").strip().replace("(","").replace(")","").replace(",",""))
)
RawData['Generation']=RawData.iloc[:,4].apply(
lambda x: float(x.replace("-","0").strip().replace("(","").replace(")","").replace(",",""))
)
RawData['WindGrossRev']=RawData.iloc[:,5].apply(
lambda x: float(x.replace("$","0").replace("-","").strip().replace("(","").replace(")","").replace(",",""))
)

CleanData=RawData.filter(
['Hour','Day','SimRep','MPBasisPAP','MPHouston','Generation','WindGrossRev']
)
CleanData['Date']=pd.to_datetime({'year':2017,
                                 'month':6,
                                 'day':CleanData.Day,
                                 'hour':CleanData.Hour})
CleanData['Dif']=CleanData.MPHouston-CleanData.MPBasisPAP
CleanData.index=CleanData.Date
#Create a data frame for each SimRep

Clean_s2=CleanData[CleanData['SimRep']=='2']
Clean_s7=CleanData[CleanData['SimRep']=='7']
Clean_s8=CleanData[CleanData['SimRep']=='8']
Clean_s30=CleanData[CleanData['SimRep']=='30']
Clean_s42=CleanData[CleanData['SimRep']=='42']
Clean_s53=CleanData[CleanData['SimRep']=='53']
Clean_s68=CleanData[CleanData['SimRep']=='68']
Clean_s84=CleanData[CleanData['SimRep']=='84']
Clean_s98=CleanData[CleanData['SimRep']=='98']
Clean_s112=CleanData[CleanData['SimRep']=='112']
Clean_s125=CleanData[CleanData['SimRep']=='125']

CleanSmall=CleanData[CleanData['Day']=='1']
# Create plots
from bokeh.charts import show,output_file,Bar,BoxPlot,Histogram,Line,Scatter,TimeSeries
from bokeh.layouts import row,column,gridplot
from bokeh.models import NumeralTickFormatter,DatetimeTickFormatter, ColumnDataSource, Select
#from bokeh.models.widgets import Tabs
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.io import output_file, show

#Market Prices


source1=ColumnDataSource( data ={'x':Clean_s2.Date,'y':Clean_s2.MPBasisPAP})
source2=ColumnDataSource( data ={'x':Clean_s2.Date,'y':Clean_s2.MPHouston})
SimRep=['2','7','8','30','42','53','68','84','98','112','125']
plot1=figure(plot_width=1200)
plot1.line(x='x',y='y', source=source1, color='orange', legend='PAP')
plot1.line(x='x',y='y', source=source2, color='green',legend='Houston')

plot1.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")
plot1.yaxis.axis_label='Price in Dollars per MWh'
plot1.xaxis.formatter=DatetimeTickFormatter(formats=dict(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    ))
#plot2=Histogram(Clean_s2['Dif'], title='Basis Difference')

menu= Select(options=SimRep,value='2',title='SimRep')

def callback(attr,old,new):
    if menu.value=='2':
        df=Clean_s2
    elif menu.value=='7':
        df=Clean_s7
    elif menu.value=='8':
        df=Clean_s8
    elif menu.value=='30':
        df=Clean_s30
    elif menu.value=='42':
        df=Clean_s42
    elif menu.value=='53':
        df=Clean_s53
    elif menu.value=='68':
        df=Clean_s68
    elif menu.value=='98':
        df=Clean_s98
    elif menu.value=='112':
        df=Clean_s112
    elif menu.value=='125':
        df=Clean_s125
    source1.data ={'x':df.Date,'y':df.MPBasisPAP}
    source2.data ={'x':df.Date,'y':df.MPHouston}
menu.on_change('value',callback)
layout=column(menu,plot1)
curdoc().add_root(layout)



#output_file(r'\\ascendanalytics.com\users\sxk94\Python\Austin\Output\test.html')
#show(plot1)



