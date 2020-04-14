import datetime as dt 
import matplotlib.pyplot as pyplot
from matplotlib import style 
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2019,12,31)

df = web.DataReader('AMD','yahoo',start,end)
print(df.tail(6))

df.to_csv('amd.csv')
