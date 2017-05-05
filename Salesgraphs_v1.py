# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:26:13 2017

@author: sxk94

Initial script to create graphs bokeh graphs. This is intended only to "sketch
" out the graphs that we want. The script will later be generalized for
reuse. 
"""
#%%
import pandas as pd

raw=pd.read_csv(
r"C:\Users\sebastian\Desktop\Inputs\BaseDashboard.csv", 
header=10, usecols=[0,2,3,4,5,6,7,9],nrows=125
)
#raw=pd.read_csv(
#r"\\ascendanalytics.com\users\sxk94\Python\Sales\Inputs\BaseDash.csv", 
#header=10, usecols=[0,2,3,4,5,6,7,9],nrows=125
#)

def removechar(df,col):
    df[col]=df[col].apply(lambda x: str(x))
    df[col]=df[col].apply(lambda x: float(
x.replace('$','').replace(',','').replace('(','').replace(')','').strip())
)

        
for i in raw:
    
    removechar(raw,i)
#%%
import numpy as np
raw['HP']=raw.ix[:,1]+raw.ix[:,2]
t1,t2=np.histogram(raw.ix[:,1],
                      bins='scott')
h1,h2=np.histogram(raw.HP, bins='scott')


#%%
from bokeh.layouts import row,column
from bokeh.models import NumeralTickFormatter,ColumnDataSource,DatetimeTickFormatter
from bokeh.plotting import figure
from bokeh.io import output_file, show

d1= ColumnDataSource( data={'x1':raw.Market,
                            'y2':raw.HP,
                            'y':raw.ix[:,1]})
plot1=figure()
plot1.circle(x='x1',y='y',
             source=d1, 
             color='steelblue',
             fill_alpha=0.5,
             size=8,
             legend='Unhedged Portfolio')
plot1.square(x='x1',
             y='y2', 
             source=d1,
             color='orange',
             fill_alpha=0.5,
             size=8,
             legend='Hedged Portfolio')
plot1.yaxis.axis_label='Portfolio Gross Margin'
plot1.xaxis.axis_label="Simulated Power Price"
plot1.yaxis.formatter=NumeralTickFormatter(format='$0a')

plot2=figure()
d2= ColumnDataSource( data={'x':h2,'y':t1,'y2':h1})
plot2.line(x='x',y='y', 
           source=d2, 
           color='steelblue',
           legend='Unhedged Portfolio')
plot2.line(x='x',y='y2',
           source=d2, 
           color='orange',
           legend='Hedged Portfolio')
plot2.yaxis.axis_label='Probabilty'
plot2.xaxis.axis_label="Portfolio Gross Margin"
plot2.xaxis.formatter=NumeralTickFormatter(format='$0a')

layout1=row(plot1, plot2)
#output_file(
#r"\\ascendanalytics.com\users\sxk94\Python\Sales\Outputs\Sales_1.html"
#)

#%%
raw2=pd.read_csv(r"C:\Users\sebastian\Desktop\Inputs\BaseDashboard.csv", 
header=195, usecols=[18,19,20,21,22,23,24],nrows=43
)
raw2.columns=['Date','AvgUnhedged','P5Unhedged','P95Unhedged','AvgHedged', 'P5Hedged','P95Hedged']
raw2['Date']=pd.to_datetime(raw2.Date)
raw2.index=raw2.Date
del(raw2['Date'])
for i in raw2:
    removechar(raw2,i)
raw2['Date']=raw2.index
#%%
d3=ColumnDataSource(raw2)
plot3=figure()

plot3.line(x='Date',y='P5Unhedged',
           source=d3, 
           color='steelblue',
           legend='Unhedged P5', 
           line_dash='dashed')
plot3.line(x='Date',y='P95Unhedged',
           source=d3, 
           color='steelblue',
           legend='Unhedged P95',
           line_dash='dashed')
plot3.line(x='Date',y='P5Hedged',
           source=d3, color='orange',
           legend='hedged P5', 
           line_dash='dashed')
plot3.line(x='Date',y='P95Hedged',
           source=d3, 
           color='orange',
           legend='hedged P95', 
           line_dash='dashed')
plot3.line(x='Date',y='AvgUnhedged',
           source=d3,
           color='steelblue',
           legend='Unhedged Mean',
           line_width=2)
plot3.xaxis.axis_label="Date"
plot3.yaxis.axis_label="Gross Margin"
plot3.yaxis.formatter=NumeralTickFormatter(format='$0a')
plot3.xaxis.formatter=DatetimeTickFormatter(years=["%Y-%b"],
                                            months=["%Y-%b"])
plot3.legend.location='top_left'
logo=figure(x_range=(0,1),
            y_range=(0,1))
logo.image_url(url=[r"C:\Users\sebastian\py\Py1\Logo.JPG"],
               x=.05,y=.85,
               h=.7,w=.9)
logo.xaxis.visible=False
logo.yaxis.visible=False
logo.toolbar.logo=None
logo.toolbar_location=None
logo.xgrid.grid_line_color=None
logo.ygrid.grid_line_color=None
bottom=row(plot3,logo)
layout2=column(layout1,bottom)


output_file(r"Outputs\Sales_4.html")
show(layout2)