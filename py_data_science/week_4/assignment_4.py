# Hypothesis: University towns have their mean housing prices less effected by recessions. 
# Run a t-test to compare the ratio of the mean price of houses in university towns 
# the quarter before the recession starts compared to the recession bottom. 
# (price_ratio=quarter_before_recession/recession_bottom)

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
short_states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 
'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 
'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 
'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 
'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 
'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 
'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 
'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 
'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 
'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 
'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 
'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 
'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 
'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
# Flip the keys and values
states_short = dict((v,k) for k,v in short_states.iteritems())

# Create array of tupples (state, town)
university_towns = []
with open('week_4/data/university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            state = line
        else:
            university_towns.append((state, line))
# print university_towns
# ---------------------------------------------------------------------------

# Create the DataFrame from the obtained array
def get_list_of_university_towns(array):
    towns_df = pd.DataFrame(array, columns=['State', 'RegionName'])
    towns_df['State'] = (towns_df['State']
        .str.replace(r"\[.*\]","")
        .str.rstrip('\n')
        .replace(states_short)
    )
    towns_df['RegionName'] = (towns_df['RegionName']
        .str.replace(r"\[.*\]","")
        .str.replace(r"\(.*\)","")
        .str.replace(r"\(.*","")
        .str.rstrip('\n')
        .str.rstrip()
        )


    # towns_df.to_csv('df_towns.csv')
    return towns_df
df_university_towns =  get_list_of_university_towns(university_towns)
# print df_university_towns
# ---------------------------------------------------------------------------

# Create DataFrame with the information of the recession start time
def handle_df_for_recession():
    df_GDP = pd.read_excel('week_4/data/gdplev_0.xlsx')
    df_GDP = df_GDP.reset_index()
    df_GDP.rename(columns={df_GDP.columns[0]: 'Year', 
    df_GDP.columns[1]: 'col_1', 
    df_GDP.columns[2]: 'col_2', 
    df_GDP.columns[3]: 'col_3', 
    df_GDP.columns[4]: 'Quarter', 
    df_GDP.columns[5]: 'col_5', 
    df_GDP.columns[6]: 'GDP', 
    df_GDP.columns[7]: 'col_7', 
    }, inplace=True)
    df_GDP = df_GDP.drop(['Year','col_1', 'col_2', 'col_3', 'col_5', 'col_7'], 1)
    df_GDP = df_GDP[219:]

    df_GDP.reset_index(inplace=True)
    df_GDP = df_GDP.drop('index', 1)
    df_GDP.to_html('df_FDP.html')
    return df_GDP
df_GDP = handle_df_for_recession()
# print df_GDP

# ---------------------------------------------------------------------------
def get_recession_start(df):
    for i in range(1, len(df_GDP) - 1):
        if (df_GDP['GDP'].loc[i] < df_GDP['GDP'].loc[i - 1]) and (df_GDP['GDP'].loc[i -1] < df_GDP['GDP'].loc[i - 2]):
            recession_start = df_GDP['Quarter'].loc[i - 2]
            return recession_start
recession_start = get_recession_start(df_GDP)
# print recession_start

# ---------------------------------------------------------------------------
def get_recession_end(df):
    rec_start_ind = df.where(df['Quarter'] == recession_start).dropna().index.values[0]
    for i in range(rec_start_ind, len(df_GDP) - 1):
        if (df_GDP['GDP'].loc[i] > df_GDP['GDP'].loc[i - 1]) and (df_GDP['GDP'].loc[i - 1] > df_GDP['GDP'].loc[i - 2]):
            recession_end = df_GDP['Quarter'].loc[i]
            return recession_end
recession_end = get_recession_end(df_GDP)
# print recession_end

# ---------------------------------------------------------------------------
def get_recession_bottom(df):
    rec_start_ind = df.where(df['Quarter'] == recession_start).dropna().index.values[0]
    rec_end_ind = df.where(df['Quarter'] == recession_end).dropna().index.values[0]
    df = df[rec_start_ind: rec_end_ind]
    min_GDP = min(df['GDP'])
    df.set_index('Quarter', inplace=True)
    recession_bottom = df[df['GDP'] == min_GDP].index.values[0]
    return recession_bottom
recession_bottom = get_recession_bottom(df_GDP)
# print recession_bottom

# ---------------------------------------------------------------------------
# Converts the housing data to quarters and returns it as mean 
# values in a dataframe. This dataframe should be a dataframe with
# columns for 2000q1 through 2016q3, and should have a multi-index
# in the shape of ["State","RegionName"].
    
# Note: Quarters are defined in the assignment description, they are
# not arbitrary three month periods.
    
# The resulting dataframe should have 67 columns, and 10,730 rows.

# ---------------------------------------------------------------------------
def convert_housing_data_to_quarters():
    df_housing = pd.read_csv('week_4/data/City_Zhvi_AllHomes.csv')
    first_columns = df_housing.columns[0:6].tolist()
    last_columns = df_housing.columns[51:].tolist()
    columns_to_keep = first_columns + last_columns
    df_first = df_housing[first_columns]
    df_months = df_housing[last_columns]
    df_months = df_months.groupby(pd.PeriodIndex(df_months.columns, freq='Q'), axis=1).mean().round(1).rename(columns=lambda c: str(c).lower())
    df_quarters = pd.concat([df_first, df_months], axis=1, sort=False)
    columns_to_drop_start = df_quarters.columns[:6]
    columns_to_drop_end = df_quarters.columns[73:]
    # df_quarters.drop(columns_to_drop_start,  axis=1, inplace=True)
    df_quarters.drop(columns_to_drop_end,  axis=1, inplace=True)
    df_quarters.drop(['RegionID', 'Metro', 'CountyName', 'SizeRank'], axis=1, inplace=True)

    df_quarters.set_index(["State","RegionName"], drop=False, inplace=True)
   
    df_quarters = df_quarters.dropna()
    # df_housing.to_csv('housing.csv')
    # df_quarters.to_csv('quarters.csv')
    # print len(df_quarters)

    return df_quarters
housing_quarters = convert_housing_data_to_quarters()
# print housing_quarters

# ---------------------------------------------------------------------------
def final_university_df(df_1, df_2):
    first_quarter = recession_start
    last_quarter = recession_bottom
    print first_quarter
    print last_quarter

    # print df_2
    # print df_1
    university_towns = df_2.RegionName.values
    print university_towns

    df_final_university = df_1.where(df_1['RegionName'].isin(university_towns)).dropna()
    # df_final_university = df_1.where(df_1['RegionName'] == df_2['RegionName']).dropna()
    
    # df_final_university = df_2[df_2.index.isin(df_1.index)]
    print len(df_final_university)
    print len(df_2)
    # df_final_university.to_csv('df_final_university.csv')
    return 'test'
print final_university_df(housing_quarters, df_university_towns)
# ---------------------------------------------------------------------------
def run_ttest(): 
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    
    return "ANSWER"   
ttest = run_ttest()

