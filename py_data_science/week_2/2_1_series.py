######################## Series
import pandas as pd
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
# print s.iloc[3]
# print s.loc['Sumo']

ar = [1, 2, 3]
series = pd.Series(ar)
# print series

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
# print all_countries

################################# Data Frame
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Store 1', 'Store 1', 'Store 2'])
# print df
# print '------------------------------------------'
# print df.loc['Store 2']
# print df.loc['Store 1', 'Cost']
# print df.T
# print '------------------------------------------'
# print df.T.loc['Cost']

copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
# print copy_df

################################ Data Frame Indexing and Loading
costs = df['Cost']
# print costs+2

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
# THIS DOES NOT WORK WELL
for col in df.columns:
    if col[0:2]=="01":
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[0:2]=="02":
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[0:2]=="02":
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[0:2]=='':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 
# print df.columns
# print df.head()

only_gold = df.where(df['Gold'] > 0).dropna()
# print only_gold.head()
# print only_gold['Gold'].count()
# print df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]

################################# Indexing DataFrames
df['country'] = df.index
# df = df.set_index('Gold')
# print df.head()
df = df.reset_index()
# print df.head()

df = pd.read_csv('census.csv')
df = df[df['SUMLEV'] == 50]
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
# print df.head()
df = df.set_index(['STNAME', "CTYNAME"])
print df.head()
# print df.loc[ [('Michigan', 'Washtenaw County'),
#          ('Michigan', 'Wayne County')] ]
# print df['SUMLEV'].unique()

##################################### Missing Values
# df = pd.read_csv('log.csv')
# df = df.set_index('time')
# print df.head()
# df = df.sort_index()
# print df.head()
# df = df.reset_index()
# print df.head()
# df = df.set_index(['time', 'user'])
# print df.head()
# df = df.fillna(method='ffill')
# print df.head()
#---------------------------------------------------------------------------------------------------------


# df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
# for col in df.columns:
#    if col[0:4] == '01 !':
#       df.rename(columns = {col: 'Gold' + col[4:]}, inplace = True)
#    if col[0:4] == '02 !':
#       df.rename(columns = {col: 'Silver' + col[4:]}, inplace = True)
#    if col[0:4] == '03 !':
#       df.rename(columns = {col: 'Bronze' + col[4:]}, inplace = True)
#    if col[0:1] == '':
#       df.rename(columns = {col: '#' + col[1:]}, inplace = True)
# only_gold = df.where(df['Gold'] > 0).dropna()
# # winter_gold_only = df[df['Gold'] == 0 & df['Gold.1'] > 0]
# df['Country'] = df.index
# df = df.set_index('Gold')
# df = df.reset_index()
import pandas as pd
import numpy as np
df = pd.read_csv('log.csv')
df = df.set_index('time')
df = df.sort_index()
df = df.reset_index()
df = df.set_index(['time', 'user'])
# df = df.fillna(method='ffill')
print df.head()