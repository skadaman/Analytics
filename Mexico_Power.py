# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:03:13 2017

@author: Sebastian Kadamany

This script uses Mexican Energy Data to create visualisations with Bokeh
"""
#%%
import pandas as pd
import numpy as np
from bokeh.charts import show,output_file,BoxPlot,Histogram,Line,Scatter,TimeSeries
from bokeh.layouts import row,column,gridplot
from bokeh.models import NumeralTickFormatter
from bokeh.models.widgets import Tabs, Panel
#from bokeh.models import HoverTool
#%%
#Import Power Prices First#
#********************Full time series and boxplot Power **********************#
Power_1=pd.read_csv(r'\\ascendanalytics.com\users\sxk94\Mexico\Data\Appended\Guadalajara_Power.csv')
Power_2=pd.read_csv(r'\\ascendanalytics.com\users\sxk94\Mexico\Data\Appended_2017\Power\DA\MexDAPow_2017_thruJun.csv')
Power_2['DT']=pd.date_range(start='1/01/2017', periods=4343, freq='H')
Power_2.index=Power_2['DT']
del Power_2['Unnamed: 0']
del Power_1['DT.1']
Power_1.index=Power_1['DT']
Power=Power_1.append(Power_2)
Power['DT']=pd.to_datetime(Power['DT'])
Power.head()
#del Power['DT.1']
#Power.index=Power['DT']
#%%
mbox=BoxPlot(Power,values='Dollars',label='Month',color='Month', 
             title='Monthly  DA Price Distributions for 2016-2017',plot_width=1200)
mbox.yaxis.axis_label='Dollars per MWh'
mbox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

mline=Scatter(data=Power,x='DT',y='Dollars',
                 title='TimeSeries of Guadalajara Node Prices 2016-2017', color='Month',
                 xscale='datetime', plot_width=1200)
mline.yaxis.axis_label='Dollars per MWh'
mline.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")
#layout1=column(mline,mbox)
#output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output\TimeSeriesandDistribution.html')
#show(layout1)
firstp=Panel(child=column(mline,mbox),title='TimeSeries')
#%%
#**************** Monthly Hourly Price Means ************************************#

MeanGuadalajara=Power[['Hour','Dollars','Month']].groupby(['Month','Hour']).agg({'Dollars':'mean'})
JanMeanG=MeanGuadalajara.loc[1:1]
FebMeanG=MeanGuadalajara.loc[2:2]
MarMeanG=MeanGuadalajara.loc[3:3]
AprMeanG=MeanGuadalajara.loc[4:4]
MayMeanG=MeanGuadalajara.loc[5:5]
JunMeanG=MeanGuadalajara.loc[6:6]
JulMeanG=MeanGuadalajara.loc[7:7]
AugMeanG=MeanGuadalajara.loc[8:8]
SepMeanG=MeanGuadalajara.loc[9:9]
OctMeanG=MeanGuadalajara.loc[10:10]
NovMeanG=MeanGuadalajara.loc[11:11]
DecMeanG=MeanGuadalajara.loc[12:12]

JanMeanG=pd.DataFrame(JanMeanG.to_records())
FebMeanG=pd.DataFrame(FebMeanG.to_records())
MarMeanG=pd.DataFrame(MarMeanG.to_records())
AprMeanG=pd.DataFrame(AprMeanG.to_records())
MayMeanG=pd.DataFrame(MayMeanG.to_records())
JunMeanG=pd.DataFrame(JunMeanG.to_records())
JulMeanG=pd.DataFrame(JulMeanG.to_records())
AugMeanG=pd.DataFrame(AugMeanG.to_records())
SepMeanG=pd.DataFrame(SepMeanG.to_records())
OctMeanG=pd.DataFrame(OctMeanG.to_records())
NovMeanG=pd.DataFrame(NovMeanG.to_records())
DecMeanG=pd.DataFrame(DecMeanG.to_records())

flatall=pd.DataFrame(MeanGuadalajara.to_records())
tri1=flatall[flatall['Month']<=4]
tri2=flatall[np.logical_and(flatall['Month']>4,flatall['Month']<9)]
tri3=flatall[flatall['Month']>=9]

tri1s=Scatter(data=tri1,y='Dollars',x='Hour',color='Month', marker='Month',legend='top_left',
              title='Hourly Average Prices by Month First Third')
tri2s=Scatter(data=tri2,y='Dollars',x='Hour',color='Month', marker='Month',legend='top_left',
              title='Hourly Average Prices by Month Second Third')
tri3s=Scatter(data=tri3,y='Dollars',x='Hour',color='Month', marker='Month',legend='top_left',
              title='Hourly Average Prices by Month Last Third')
tri1s.yaxis.axis_label='Average Dollars per MWh'
tri2s.yaxis.axis_label='Average Dollars per MWh'
tri3s.yaxis.axis_label='Average Dollars per MWh'
tri1s.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")
tri2s.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")
tri3s.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")
tri1s.y_range=tri2s.y_range=tri3s.y_range
layout= row(tri1s,tri2s,tri3s)

#output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output\HourlyAveragePricesbyMonth.html')              
#show(layout)
secondp=Panel(child=row(tri1s,tri2s,tri3s),title='Averages')
tabsp=Tabs(tabs=[firstp,secondp])
output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output2\PowerDATabs.html') 
show(tabsp)
#%%
#************************ Load plots ************************#

#**********TimeSeries and BoxPlots***************#
Load=pd.read_csv(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Data\Guadalajara_Load.csv')
Load.head()
del Load['Date.1']

LScat=Scatter(data=Load,x='Date',y='Volume',
                 title='Guadalajara Load Profile for 2016-2017', color='Month',
                 xscale='datetime', plot_width=1200)
LScat.yaxis.axis_label='Load in MW'
LScat.legend.location='top_right'
LScat.legend.orientation='horizontal'

LBox=BoxPlot(Load,values='Volume',label='Month',color='Month', 
             title='Monthly Load Profile Distributions 2016-2017',plot_width=1200)
LBox.yaxis.axis_label='Load in MW'
LBox.legend.location='top_right'
LBox.legend.orientation='horizontal'

first=Panel(child=column(LScat,LBox),title='Profiles')
#output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output\LoadProfileandDistribution.html')
#show(layout2)
#**************** Monthly Hourly Load Means ************************************#
Meanloads=Load[['Hour','Volume','Month']].groupby(['Month','Hour']).agg({'Volume':'mean'})
flatload=pd.DataFrame(Meanloads.to_records())
tril1=flatload[flatload['Month']<=4]
tril2=flatload[np.logical_and(flatload['Month']>4,flatload['Month']<9)]
tril3=flatload[flatload['Month']>=9]

tri1ls=Scatter(data=tril1,y='Volume',x='Hour',color='Month', marker='Month',legend='top_left',
               title='Hourly Load Mean for the First Trimester')
tri2ls=Scatter(data=tril2,y='Volume',x='Hour',color='Month', marker='Month',legend='top_left',
              title='Hourly Load Mean for the Second Trimester' )
tri3ls=Scatter(data=tril3,y='Volume',x='Hour',color='Month', marker='Month',legend='top_left',
               title='Hourly Load Mean for the Third Trimester')
tri1ls.yaxis.axis_label='Load in MW'
tri2ls.yaxis.axis_label='Load in MW'
tri3ls.yaxis.axis_label='Load in MW'
second=Panel(child=row(tri1ls,tri2ls,tri3ls),title='Averages')
#layoutl=row(tri1ls,tri2ls,tri3ls)
#output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output\LoadHourlyMeanbyMonth.html')
#show(layoutl)
ltabs=Tabs(tabs=[first,second])
output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output\HistoricLoadTabs.html')
show(ltabs)
#%%
#******************** Historic Ancilliaries*********************#
#******************** Full time series and boxplot Ancilliaries  **********************#
FullAnci_16=pd.read_csv(r'\\ascendanalytics.com\users\sxk94\Mexico\Data\Appended\Full_anci.csv')
FullAnci_17=pd.read_csv(r'\\ascendanalytics.com\users\sxk94\Mexico\Data\Appended_2017\Acillary\DA\MexDAAnci_2017_thruJun_reformat.csv')
FullAnci=FullAnci_16.append(FullAnci_17)
#FullAnci=pd.read_csv(r'\\ascendanalytics.com\users\sxk94\Mexico\Data\Appended\Full_Anci2017.csv')
#FullAnci.head()
FullAnci.columns=['index','Hour','Zone','Type','Price','Date']
AnciZ1=FullAnci[FullAnci['Zone']=='ZONA 1']
AnciZ1['Date']=pd.to_datetime(AnciZ1['Date'])
AnciZ1['Month']=AnciZ1.Date.apply(lambda x: x.month)
AnciZ1['Dollars']=AnciZ1.Price/20


Z1Secondary=AnciZ1[AnciZ1['Type']=='Reserva de regulacion secundaria']
Z1Secondary['DT']=pd.date_range(start='1/29/2017', periods=12215, freq='H')
Z1Spin10=AnciZ1[AnciZ1['Type']=='Reserva rodante de 10 minutos']
Z1Spin10['DT']=pd.date_range(start='1/29/2017', periods=12215, freq='H')
Z1noSpin10=AnciZ1[AnciZ1['Type']=='Reserva no rodante de 10 minutos']
Z1noSpin10['DT']=pd.date_range(start='1/29/2017', periods=12215, freq='H')
Z1spinSupp=AnciZ1[AnciZ1['Type']=='Reserva rodante suplementaria']
Z1spinSupp['DT']=pd.date_range(start='1/29/2017', periods=12215, freq='H')
Z1nospinSupp=AnciZ1[AnciZ1['Type']=='Reserva no rodante suplementarias']
Z1nospinSupp['DT']=pd.date_range(start='1/29/2017', periods=12215, freq='H')
#%%
SecScat=Scatter(data=Z1Secondary,x='DT',y='Dollars',color='Month',
                title='Secondary Reserve Prices 2016-2017')
SecScat.yaxis.axis_label='Dollars per MWh'
SecScat.legend.location='top_right'
SecScat.legend.orientation='horizontal'
SecScat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

Spin10Scat=Scatter(data=Z1Spin10,x='DT',y='Dollars',color='Month',
                   title='10 Minute Spinning Reserve 2016-2017')
Spin10Scat.yaxis.axis_label='Dollars per MWh'
Spin10Scat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

SecScat.y_range=Spin10Scat.y_range
Spin10Scat.legend.location='top_right'
Spin10Scat.legend.orientation='horizontal'

noSpin10Scat=Scatter(data=Z1noSpin10,x='DT',y='Dollars',color='Month',
                     title='Non-Spinning 10 Minute Reserve 2016-2017')
noSpin10Scat.yaxis.axis_label='Dollars per MWh'
noSpin10Scat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

SpinSuppScat=Scatter(data=Z1spinSupp,x='DT',y='Dollars',color='Month',
                     title='Spinning Supplementary Reserve 2016-2017')
SpinSuppScat.yaxis.axis_label='Dollars per MWh'
SpinSuppScat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

NoSpinSuppScat=Scatter(data=Z1nospinSupp,x='DT',y='Dollars',color='Month',
                       title='Non-Spinning Supplementary Reserve 2016-2017')
NoSpinSuppScat.yaxis.axis_label='Dollars per MWh'
NoSpinSuppScat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

noSpin10Scat.y_range=SpinSuppScat.y_range=NoSpinSuppScat.y_range

SecBox=BoxPlot(Z1Secondary,values='Dollars',color='Month',
                title='Secondary Reserve Prices 2016-2017',label='Month')
SecBox.yaxis.axis_label='Dollars per MWh'
SecBox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")
SecScat.y_range=SecBox.y_range
Spin10Box=BoxPlot(Z1Spin10,values='Dollars',color='Month',
                   title='10 Minute Spinning Reserve 2016-2017',label='Month')
Spin10Box.yaxis.axis_label='Dollars per MWh'
Spin10Box.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

SecScat.y_range=Spin10Scat.y_range=Spin10Scat.y_range=Spin10Box.y_range

noSpin10Box=BoxPlot(Z1noSpin10,values='Dollars',color='Month',
                     title='Non-Spinning 10 Minute Reserve 2016-2017',label='Month')
noSpin10Box.yaxis.axis_label='Dollars per MWh'
noSpin10Box.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

SpinSuppBox=BoxPlot(Z1spinSupp,values='Dollars',color='Month',
                     title='Spinning Supplementary Reserve 2016-2017',label='Month')
SpinSuppBox.yaxis.axis_label='Dollars per MWh'
SpinSuppBox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

NoSpinSuppBox=BoxPlot(Z1nospinSupp,values='Dollars',color='Month',
                       title='Non-Spinning Supplementary Reserve 2016-2017',label='Month')
NoSpinSuppBox.yaxis.axis_label='Dollars per MWh'
NoSpinSuppBox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

glayout=gridplot([[SecScat,SecBox],[Spin10Scat,Spin10Box],
                  [noSpin10Scat,noSpin10Box],[SpinSuppScat,SpinSuppBox],
                  [NoSpinSuppScat,NoSpinSuppBox]])

output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output2\AnciMonthtype.html')
show(glayout)
#%%

#********************* Results Data *******************#
Results=pd.read_excel(r'\\ascendanalytics.com\users\sxk94\Mexico\Results2\RawModelResultsDA_s2.XLSX')
Results['Month']= Results.Date.apply(lambda x : x.month)
Results['Year']=Results.Date.apply(lambda x : x.year)
#Net Revenue
NetRevenueScat=Scatter(data=Results,x='Date',y='Net Revenue ($)',color='Year',
                    title='Hourly Net Revenue Time Series')
NetRevenueScat.yaxis.axis_label='Hourly Net Revenue in Dollars'
NetRevenueScat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

NetRevenueBox=BoxPlot(Results,values='Net Revenue ($)',label='Year',color='Year',
                      title='Yearly Distributions of Hourly Net Revenue')
NetRevenueBox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")
NetRevenueBox.yaxis.axis_label='Hourly Net Revenue in Dollars'

Rlayout=column(NetRevenueScat,NetRevenueBox)
output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output2\ProjectedNetRevenue2.html')
show(Rlayout)
#%%
#Generation
GenerSum=Results[['Year','Generation (MW)','Month']].groupby(['Year','Month']).agg({'Generation (MW)':'sum'})
flatGenerSum=pd.DataFrame(GenerSum.to_records())
flatGenerSum['Time']=flatGenerSum['Month'].map(str)+'/'+flatGenerSum['Year'].map(str)
flatGenerSum['Time']=flatGenerSum.Time.apply(lambda x : pd.to_datetime(x))
GenerationScat=Scatter(data=flatGenerSum,x='Time',y='Generation (MW)',color='Year',
                    title='Generation Time Series',plot_width=1200)
GenerationScat.yaxis.axis_label='Generation in MW'

GenerationBox=BoxPlot(flatGenerSum,values='Generation (MW)',label='Year',color='Year',
                      title='Yearly Distributions of Generation',plot_width=1200)
GenerationBox.yaxis.axis_label='Generation in MW'

Glayout=column(GenerationScat,GenerationBox)
GenerationScat.legend.orientation='horizontal'
GenerationBox.legend.orientation='horizontal'
output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output2\GenerationForecast2.html')
show(Glayout)
#%%
#************** Prices for ancillary services******#
RSecScat=Scatter(data=Results,x='Date',y='Secondary Reseve Prices ($)',color='Year',
                title='Secondary Reserve Prices')
RSecScat.yaxis.axis_label='Dollars per MWh'
RSecScat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

RSpin10Scat=Scatter(data=Results,x='Date',y='Supplementary Spinning Prices ($)',color='Year',
                   title='10 Minute Spinning Reserve')
RSpin10Scat.yaxis.axis_label='Dollars per MWh'
RSpin10Scat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")


RnoSpin10Scat=Scatter(data=Results,x='Date',y='10mSpin Prices ($)',color='Year',
                     title='Non-Spinning 10 Minute Reserve')
RnoSpin10Scat.yaxis.axis_label='Dollars per MWh'
RnoSpin10Scat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

RSpinSuppScat=Scatter(data=Results,x='Date',y='10m NoSpin Prices ($)',color='Year',
                     title='Spinning Supplementary Reserve')
RSpinSuppScat.yaxis.axis_label='Dollars per MWh'
RSpinSuppScat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

############
#%%
RSecBox=BoxPlot(Results,values='Secondary Reseve Prices ($)',color='Year',
                title='Secondary Reserve Prices',label='Year')
RSecBox.yaxis.axis_label='Dollars per MWh'
RSecBox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

RSpin10Box=BoxPlot(Results,values='Supplementary Spinning Prices ($)',color='Year',
                   title='10 Minute Spinning Reserve',label='Year')
RSpin10Box.yaxis.axis_label='Dollars per MWh'
RSpin10Box.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

RnoSpin10Box=BoxPlot(Results,values='10mSpin Prices ($)',color='Year',
                     title='Non-Spinning 10 Minute Reserve',label='Year')
RnoSpin10Box.yaxis.axis_label='Dollars per MWh'
RnoSpin10Box.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

RSpinSuppBox=BoxPlot(Results,values='10m NoSpin Prices ($)',color='Year',
                       title='Non-Spinning Supplementary Reserve',label='Year')
RSpinSuppBox.yaxis.axis_label='Dollars per MWh'
RSpinSuppBox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

rglayout=gridplot([[RSecScat,RSecBox],[RSpin10Scat,RSpin10Box],
                  [RnoSpin10Scat,RnoSpin10Box],[RSpinSuppScat,RSpinSuppBox]])
output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output2\ResultsAnciMonthtype2.html')
show(rglayout)
#%%
#************************Gas******************#
Gas=pd.read_csv(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Data\Gas.csv')
Gasmean=Gas[['Year','Gas','Month']].groupby(['Year','Month']).agg({'Gas':'mean'})
flatGasmean=pd.DataFrame(Gasmean.to_records())
flatGasmean['Time']=flatGasmean['Month'].map(str)+'/'+flatGasmean['Year'].map(str)
flatGasmean['Time']=flatGasmean.Time.apply(lambda x : pd.to_datetime(x))

GasScat=Scatter(data=flatGasmean,x='Time',y='Gas',color='Year',
                title='Gas Monthly Time Series')
GasScat.yaxis.axis_label='Dollars per MmBTU'
GasScat.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

GasBox=BoxPlot(flatGasmean,values='Gas',color='Year',label='Year', 
               title='Yearly Gas Price Distributions')
GasBox.yaxis.axis_label='Dollars per MmBTU'
GasBox.yaxis[0].formatter=NumeralTickFormatter(format="$0.00")

Gaslayout=column(GasScat,GasBox)
output_file(r'\\ascendanalytics.com\users\sxk94\Python\Mexico\Output\Gasprices.html')
show(Gaslayout)


