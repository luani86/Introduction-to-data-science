import numpy as np
import pandas as pd
import xlsx2html as xlsx2html
# import matplotlib.pyplot as plt
# ---------------------------------- QUESTION 1 ----------------------------------
# Handling the indicators.xls file (Converting to csv, renaming the columns and changing the values)
def create_energy(file):
    df = pd.read_excel(file)
    df = df[16:243]
    df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    df.to_csv("indicators.csv", encoding="utf-8")
    df_1 = pd.read_csv('indicators.csv')

    df_1.columns = ['ID','Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    df_1.set_index('ID', inplace=True)
    df_1['Energy Supply'] = df_1['Energy Supply'].convert_objects(convert_numeric=True) * 1000000

    df_1['Country'] = df_1['Country'].str.replace('\d+', '')
    df_1['Country'] = df_1['Country'].str.replace(r"\(.*\)","")
    df_1['Country'] = df_1['Country'].str.rstrip()
    renamed_countries = {"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"}
    df_1['Country'] = df_1['Country'].replace(renamed_countries, regex=True)
    return df_1
Energy = create_energy('indicators.xls')
# print Energy.loc[21, 'Energy Supply'] Returns Energy supply value from the index (ID) 21
# print Energy

# Handling the world_bank.csv file (Trimming the header and changing the values)
def create_GDP(file):
    GDP = pd.read_csv(file)
    # wb = pd.read_csv('https://raw.githubusercontent.com/sidsriv/Introduction-to-Data-Science-in-python/master/world_bank.csv')

    rename_countries = {"Korea, Rep.": "South Korea", 
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"}
    GDP['Country'] = GDP['Country'].replace(rename_countries, regex=True)
    return GDP
GDP = create_GDP('world_bank.csv')
# print GDP

# Handling the scimagojr.xlsx file ()
def create_scimen(file):
    ScimEn = pd.read_excel(file)
    return ScimEn
ScimEn = create_scimen('scimagojr.xlsx')
# print ScimEn

# Joining the files together
def answer_1(file_1, file_2, file_3):
    file_3 = file_3[:15]
    # file_2 = file_2.where(set(file_2['Country']).intersection(set(file_3['Country'])))
    columns_final = ['Country','Rank', 
    'Documents', 
    'Citable documents', 
    'Citations', 
    'Self-citations', 
    'Citations per document', 
    'H index', 
    'Energy Supply', 
    'Energy Supply per Capita', 
    '% Renewable', 
    '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    result = pd.merge(file_1, file_2, on='Country', how = 'inner')
    result = pd.merge(result, file_3, on='Country', how = 'inner')
    result = result[columns_final].set_index('Country').sort_values('Rank')
    return result
df = answer_1(Energy, GDP, ScimEn)
# print df

# QUESTION 2: When you joined the datasets, but before you reduced this to the top 15 items, 
# how many entries did you lose?
def get_inner_number(file_1, file_2, file_3):
    # file_3 = file_3[:15]
    columns_final = ['Country',
    'Rank', 
    'Documents', 
    'Citable documents', 
    'Citations', 
    'Self-citations', 
    'Citations per document', 
    'H index', 
    'Energy Supply', 
    'Energy Supply per Capita', 
    '% Renewable', 
    '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    result = pd.merge(file_1, file_2, on='Country', how = 'inner')
    result = pd.merge(result, file_3, on='Country', how = 'inner')
    result = result[columns_final].set_index('Country').sort_values('Rank')
    inner_number = max(result.count())
    return inner_number
inner_number = get_inner_number(Energy, GDP, ScimEn)

def get_outer_number(file_1, file_2, file_3):
    # file_3 = file_3[:15]
    columns_to_keep = ['Country',
    'Rank', 
    'Documents', 
    'Citable documents', 
    'Citations', 
    'Self-citations', 
    'Citations per document', 
    'H index', 
    'Energy Supply', 
    'Energy Supply per Capita', 
    '% Renewable', 
    '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    result = pd.merge(file_1, file_2, on='Country', how = 'outer')
    result = pd.merge(result, file_3, on='Country', how = 'outer')
    result = result[columns_to_keep].set_index('Country').sort_values('Rank')
    outer_number = max(result.count())
    return outer_number
outer_number = get_outer_number(Energy, GDP, ScimEn)
def get_number_diff(num_1, num_2):
    diff = abs(num_1 - num_2)
    return diff
difference = get_number_diff(inner_number, outer_number)
# print difference

# QUESTION 3: What is the average GDP over the last 10 years for each country? 
# (exclude missing values from this calculation.)
def answer_3(df):
    columns_to_keep = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    df = df[columns_to_keep]
    df['avgGDP'] = (df['2006'] + df['2007'] + 
    df['2008'] + df['2009'] + 
    df['2010'] + df['2011'] + 
    df['2012'] + df['2013'] + 
    df['2014'] + df['2015']) / len(columns_to_keep)
    df = df['avgGDP'].dropna().sort_values(ascending=False)
    return df
avgGDP = answer_3(df)
# Can not contain 15 countries because of the dropna().
# print avgGDP
df['avgGDP'] = avgGDP
# print df
# QUESTION 4: By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
def answer_4(df, GDP_position):
    df = df.sort_values('avgGDP')
    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    df['GDP_max'] = df[years].max(axis=1)
    df['GDP_min'] = df[years].min(axis=1)
    df['GDP_diff'] = df['GDP_max'] - df['GDP_min']
    return df.iloc[GDP_position - 1]['GDP_diff']
    # return df
GDP_change = answer_4(df, 6)
# print GDP_change

# QUESTION 5: What is the mean Energy Supply per Capita?
def answer_5(df):
    supply_values = map(float, df['Energy Supply per Capita'].values)
    mean_supply = np.mean(supply_values)
    return mean_supply
mean_supply = answer_5(df)
# print mean_supply

# QUESTION 6: What country has the maximum % Renewable and what is the percentage?
def answer_6(df):
    # print df['% Renewable']
    best_country = df['% Renewable'].idxmax()
    return (best_country, df.loc[best_country]['% Renewable'])
renewable = answer_6(df)
# print renewable

# QUESTION 7: Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
def answer_7(df):
    columns_to_keep = ['Citations', 
    'Self-citations']
    df = df[columns_to_keep]
    df['cit_ratio'] = df['Self-citations'] / df['Citations']
    max_ratio = max(df['cit_ratio'])
    max_ratio_country = df['cit_ratio'].idxmax()
    # print df
    return (max_ratio_country, max_ratio)
max_cit_country = answer_7(df)
# print max_cit_country

# QUESTION 8: Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
def answer_8(df):
    columns_to_keep = ['Energy Supply', 
    'Energy Supply per Capita'
    ]
    df = df[columns_to_keep]
    energy_supply_nums = []
    energy_per_capita_nums = []
    df['Energy Supply'] = pd.to_numeric(df['Energy Supply'])
    df['Energy Supply per Capita'] = pd.to_numeric(df['Energy Supply per Capita'])
    df['popul'] = df['Energy Supply'] / df['Energy Supply per Capita']
    max_popul = np.max(df['popul'])
    max_popul_country = df['popul'].idxmax()
    # print df
    return (max_popul_country, max_popul)
max_popul = answer_8(df)
# print max_popul

# QUESTION 9: Create a column that estimates the number of citable documents per person.
#  What is the correlation between the number of citable documents per capita and the energy
#  supply per capita? Use the .corr() method, (Pearson's correlation)
def answer_9(df):
    columns_to_keep = ['Citable documents', 
    'Energy Supply', 
    'Energy Supply per Capita', ]
    df = df[columns_to_keep]
    df['Energy Supply'] = pd.to_numeric(df['Energy Supply'])
    df['Energy Supply per Capita'] = pd.to_numeric(df['Energy Supply per Capita'])
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['Citable docs per Capita'] = df['Citable documents'] / df['PopEst']
    capita_energy_relation = df['Citable docs per Capita'].corr(df['Energy Supply per Capita'])
    print df
    return capita_energy_relation
capita_energy_relation = answer_9(df)
# print capita_energy_relation
# Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst'] (found on internet)

# QUESTION 10: Create a new column with a 1 if the country's % Renewable value is at or above the median
#  for all countries in the top 15, and a 0 if the country's % Renewable value is below the median
def answer_10(df):
    columns_to_keep = ['Rank',
    '% Renewable']
    df = df[columns_to_keep]
    renew_median = df['% Renewable'].median()
    df['Renewable grade'] = np.where(df['% Renewable']>=renew_median, 1, 0)
    # print 'Renuwable median is %r.' % renew_median
    return df['Renewable grade']
HighRenew = answer_10(df)
# print HighRenew

# QUESTION 11: Use the following dictionary to group the Countries by Continent, 
# then create a dateframe that displays the sample size (the number of countries in each continent bin), 
# and the sum, mean, and std deviation for the estimated population of each country.
def answer_11(df):
    ContinentDict  = {'China':'Asia', 
    'United States':'North America', 
    'Japan':'Asia', 
    'United Kingdom':'Europe', 
    'Russian Federation':'Europe', 
    'Canada':'North America', 
    'Germany':'Europe', 
    'India':'Asia',
    'France':'Europe', 
    'South Korea':'Asia', 
    'Italy':'Europe', 
    'Spain':'Europe', 
    'Iran':'Asia',
    'Australia':'Australia', 
    'Brazil':'South America'}
    # columns_to_keep = [
    # 'Rank', 
    # 'Documents', 
    # 'Citable documents', 
    # 'Citations', 
    # 'Self-citations', 
    # 'Citations per document', 
    # 'Energy Supply', 
    # 'Energy Supply per Capita', ]
    # df = df[columns_to_keep]
    df['Energy Supply'] = pd.to_numeric(df['Energy Supply'])
    df['Energy Supply per Capita'] = pd.to_numeric(df['Energy Supply per Capita'])
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    # final_columns = ['PopEst']
    # df = df[final_columns]
    # print df
    new_df = pd.DataFrame.from_dict(ContinentDict, orient='index')
    new_df['continent'] = ContinentDict.values()
    new_df['Country'] = ContinentDict.keys()
    new_df.set_index('Country', inplace=True)
    columns_new = ['continent']
    new_df = new_df[columns_new]
    merged = df.merge(new_df, on='Country', how = 'inner')
    merged.reset_index(inplace=True)
    merged.set_index(['continent'], inplace=True)
    merged = merged.groupby(merged.index)['PopEst'].agg(['size', 'sum','mean','std'])
    return merged
df_continents = answer_11(df)
# print df_continents

# QUESTION 12: ------- NOT WORKING ---------
# Cut % Renewable into 5 bins. 
# Group Top15 by the Continent, as well as these new % Renewable bins. 
# How many countries are in each of these groups?
# This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. 
# Do not include groups with no countries.
def answer_12(df):
    ContinentDict  = {'China':'Asia', 
    'United States':'North America', 
    'Japan':'Asia', 
    'United Kingdom':'Europe', 
    'Russian Federation':'Europe', 
    'Canada':'North America', 
    'Germany':'Europe', 
    'India':'Asia',
    'France':'Europe', 
    'South Korea':'Asia', 
    'Italy':'Europe', 
    'Spain':'Europe', 
    'Iran':'Asia',
    'Australia':'Australia', 
    'Brazil':'South America'}
    new_df = pd.DataFrame.from_dict(ContinentDict, orient='index')
    new_df['continent'] = ContinentDict.values()
    new_df['Country'] = ContinentDict.keys()
    new_df.set_index('Country', inplace=True)
    columns_to_keep = ['% Renewable']
    df = df[columns_to_keep]
    merged = df.merge(new_df, on='Country', how = 'inner')
    # print df
    bins = [0, 1, 5, 10, 25, 50, 100]
    merged['binned'] = pd.cut(merged['% Renewable'], bins)
    return merged
continents_renewable = answer_12(df)
# print continents_renewable

# QUESTION 13: Convert the Population Estimate series to a string with thousands separator (using commas). 
# Do not round the results. e.g. 317615384.61538464 -> 317,615,384.61538464
# This function should return a Series PopEst whose index 
# is the country name and whose values are the population estimate string.
def answer_13(df):
    df['Energy Supply'] = pd.to_numeric(df['Energy Supply'])
    df['Energy Supply per Capita'] = pd.to_numeric(df['Energy Supply per Capita'])
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    columns_to_keep = ['PopEst']
    df['PopEst'] = df['PopEst'].map('{:,.1f}'.format) # Can not prevent rounding
    df = df[columns_to_keep]
    return df
convert_pop = answer_13(df)
# print convert_pop

# OPTIONAL: Visualisation (Does not work)
# def plot_optional(df):
#     import matplotlib as plt
#     # %matplotlib inline
#     Top15 = create_energy(df)
#     ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
#                     c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
#                        '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
#                     xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6])

#     for i, txt in enumerate(Top15.index):
#         ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

#     print("This is an example of a visualization that can be created to help understand the data. \
# This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
# 2014 GDP, and the color corresponds to the continent.")
# graph = plot_optional(df)
# print graph