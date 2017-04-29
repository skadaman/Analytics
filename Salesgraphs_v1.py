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



#%%
from bokeh.layouts import row,column,gridplot
from bokeh.models import NumeralTickFormatter, ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import output_file, show

d1= ColumnDataSource( data={'x':raw.Market,'y':raw.ix[:,1]})
plot1=figure()
plot1.circle(x='x',y='y', source=d1, color='blue')
plot1.yaxis.axis_label='Portfolio Gross Margin'
plot1.xaxis.axis_label="Simulated Power Price"
plot1.yaxis.formatter=NumeralTickFormatter(format='$0a')

plot2=figure()
d2= ColumnDataSource( data={'x':t2,'y':t1})
plot2.line(x='x',y='y', source=d2)
plot2.yaxis.axis_label='Probabilty'
plot2.xaxis.axis_label="Portfolio Gross Margin"
plot2.xaxis.formatter=NumeralTickFormatter(format='$0a')
layout1=row(plot1, plot2)
#output_file(
#r"\\ascendanalytics.com\users\sxk94\Python\Sales\Outputs\Sales_1.html"
#)
output_file(r"C:\Users\sebastian\Desktop\Outputs\Sales_2.html")
show(layout1)