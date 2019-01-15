import numpy as np
import pandas as pd
# Timestamp
tm = pd.Timestamp('9/1/2016 10:05AM')
# print tm

# Period
per = pd.Period('2016-01', 'M')
# print per

# Datetime Index
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
# print t1

# Period Index
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
# print t2

# Convert to Datetime
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
ts3.index = pd.to_datetime(ts3.index)
# dateformat = pd.to_datetime('4.7.12', dayfirst=True)
# print ts3

# TimeDelta
td = pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')
date = pd.Timestamp('1/1/2016 8:10AM') + pd.Timedelta('12D 1H')
# print date

# Working with Dates in a Dataframe
dates = pd.date_range('10-1-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame({'count 1': 100 + np.random.randint(-5, 10, 9), 
'count 2': 120 + np.random.randint(-5, 10, 9)},index=dates)
# print df.index.weekday_name
# print df.diff()
# print df.resample('M').mean()
# print df['2017']
# print df['2016-12']
# print df['2016-12':]
# print df.asfreq('2D', method='ffill')
# print df

# Not working
# import matplotlib.pyplot as plt
# df.plot()
