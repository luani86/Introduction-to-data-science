import numpy as np
import pandas as pd
# Creating a DataFrame
XYZ_web = {'Days': [1, 2, 3, 4, 5, 6],
'Visitors': [1000, 700, 6000, 1000, 400, 350], 
'Bounce_rate': [20, 20, 23, 15, 10, 34]}
df = pd.DataFrame(XYZ_web)

# Slicing a DataFrame
# print df.head(2)
# print df.tail(2)

# Merging DataFrames
df1 = pd.DataFrame({'HPI': [80, 90, 70, 60], 'Int_rate': [2, 1, 2, 1], 'IND_GDP': [50, 45, 45, 67]},
index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({'HPI': [80, 90, 70, 60], 'Int_rate': [2, 1, 2, 1], 'IND_GDP': [50, 45, 45, 67]},
index=[2005, 2006, 2007, 2008])
merged = pd.merge(df1, df2, on='HPI')
# print merged

# Joining DataFrames
df1 = pd.DataFrame({'Int_rate': [2, 1, 2, 1], 'IND_GDP': [50, 45, 45, 67]},
index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({'Low_Tier_HPI': [50, 45, 67, 34], 'Unemployment': [1, 3, 5, 6]},
index=[2001, 2003, 2004, 2004])

joined = df1.join(df2)
# print joined

# Change the index in DataFrames
df = pd.DataFrame({'Day': [1, 2, 3, 4],
'Visitors': [200, 100, 230, 300], 
'Bounce_rate': [20, 45, 60, 10]})
df.set_index('Day', inplace=True)

# Visualization (Doesn't work)

# import matplotlib.py as plt
# from matplotlib import style
# style.use('fivethirtyeight')
# df.plot()
# plt.show()
# print df

# Change the column headers
df = pd.DataFrame({'Day': [1, 2, 3, 4],
'Visitors': [200, 100, 230, 300], 
'Bounce_rate': [20, 45, 60, 10]})
df.set_index('Day', inplace=True)
df = df.rename(columns={'Visitors': 'Users'})
# print df

# Concatenation of DataFrames
df1 = pd.DataFrame({'HPI': [80, 85, 88, 85], 
'Int_rate': [2, 3, 2, 2], 
'IND_GDP_Thousands': [50, 55, 65, 55]},
index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80, 85, 88, 85], 
'Int_rate': [2, 1, 2, 1], 
'IND_GDP_Thousands': [50, 55, 65, 55]},
index=[2005, 2006, 2007, 2008])

concat = pd.concat([df1, df2])
# print concat

# Data Munging (Convert csv file to html)
cars = pd.read_csv('cars.csv', index_col=0)
cars.to_html('cars.html')
print cars[2:]
print cars

df = pd.read_csv('salaries.csv')
description = df.describe()
df_array = df.values
# print description
#----------------------------------------------------------------------------------------------








