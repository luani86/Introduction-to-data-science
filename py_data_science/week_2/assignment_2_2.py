#------------------------------------ DataFrame Preparation ----------------------------------
import pandas as pd
import numpy as np

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')

#------------------------------------ PART 1 ----------------------------------

# Question 0: Get the information about the first country in df
def answer_zero():
    return df.iloc[0]
# print answer_zero()
# print df.head()
#------------------------------------ PART 1 ----------------------------------
# Question 1: Which country has won the most gold medals in summer games?
def answer_1(df):
    most_summer_gold_country = df['Gold'].idxmax()
    return most_summer_gold_country
# print answer_1(df)

# Question 2: Which country had the biggest difference between their summer and winter gold medal counts?
def answer_2(df):
    max_diff_country = abs(df['Gold'] - df['Gold.1']).idxmax()
    return max_diff_country
# print answer_2(df)

# Question 3: Country with biggest difference between summer gold medal counts and winter gold medal counts relative to their total gold medal count?
def answer_3(df):
    df = df.where(df['Gold'] > 0).dropna()
    df = df.where(df['Gold.1'] > 0).dropna()
    max_rel_diff_df = abs(df['Gold'] - df['Gold.1']) / (df['Gold'] + df['Gold.1'])
    return max_rel_diff_df.idxmax()
# print answer_3(df)

# Question 4: Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2`) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
def answer_4(df):
    new_df = df
    return pd.DataFrame(new_df['Gold.2'] * 3 + new_df['Silver.2'] * 2 + new_df['Bronze.2'])
# print answer_4(df)

#------------------------------------ PART 2 ----------------------------------
census_df = pd.read_csv('census.csv')

# Question 5: Which state has the most counties in it? (hint: consider the sumlevel key carefully!
def answer_5(df):
    count_counties = df['STNAME'].value_counts() - 1
    return count_counties.idxmax()
#print answer_5(census_df)

# Question 5: Another way
def answer_5_a(df):
    cty_count = []
    sumlevs_str = ''
    sumlevs = df['SUMLEV'].values
    for i in sumlevs:
        i = str(i)
        sumlevs_str += i
    sumlevs_str_arr = sumlevs_str.split('40')
    longest_dist = max(sumlevs_str_arr, key=len)
    max_county_num = len(longest_dist) / 2
    # Or the way below with the loop:
    # for j in sumlevs_str_arr:
    #     cty_count.append(len(j))
    # max_county_num = max(cty_count) / 2
    state_max_cty = pd.DataFrame(df['STNAME'].value_counts() - 1)
    state_max_cty = state_max_cty.where(state_max_cty['STNAME'] == max_county_num).dropna()
    return state_max_cty
# print answer_5_a(census_df)

# Question 5: Another way
# Function returns the array of lengths of the substrings labeled at the beginning and the end in a string
def kmer_lengths(string, label):
    string += label
    kmer_pos = []
    kmer_dist = []
    for i in range (0, len(string)):
        kmer = ''
        if string[i] == label:
            kmer_pos.append(i)
    for i in range(0, len(kmer_pos)-1):
        dist = ((kmer_pos[i+1] - kmer_pos[i]) -1) / 2
        if dist != 0:
            kmer_dist.append(dist)
    return kmer_dist
# print kmer_lengths('405050405050504050505040', '4')

def answer_5_b(df):
    sumlevs_str = ''
    kmer_pos = []
    sumlevs = df['SUMLEV'].values
    for i in sumlevs:
        i = str(i)
        sumlevs_str += i
    kmer_dist = kmer_lengths(sumlevs_str, '4')
    state_max_cty = pd.DataFrame(df['STNAME'].value_counts() - 1)
    state_max_cty = state_max_cty.where(state_max_cty['STNAME'] == max(kmer_dist)).dropna()
    return state_max_cty
# print answer_5_b(census_df)
# print census_df.head()


# Question 5.a: Average number of counties in a state!
def average_cty(df):
    total_states = len(df[df['SUMLEV'] == 40])
    total_counties = len(df[df['SUMLEV'] == 50])
    average_counties = float(total_counties) / float(total_states)
    return round(average_counties, 2)
# print average_cty(census_df)

# Question 6: Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
def answer_6(df):
    df = df[['STNAME', 'CTYNAME', 'CENSUS2010POP']]
    df = df.where(df['CTYNAME'] != df['STNAME']).dropna()
    df_sorted = df.sort_values(['STNAME','CENSUS2010POP'], ascending=False).groupby('STNAME')

    new=pd.Series(["result"])
    for table, content in df_sorted:
        new[table] = content["CENSUS2010POP"][1:4].sum()
    return new.sort_values(ascending=False)[1:4]
    # return new.sort_values(ascending=False)[1:4].index
#print answer_6(census_df)


# Question 7: Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
def answer_7(df):
    df = df.where(df['STNAME'] != df['CTYNAME']).dropna()
    df['MAX'] = df[["POPESTIMATE2010",
    "POPESTIMATE2011",
    'POPESTIMATE2012',
    'POPESTIMATE2013',
    'POPESTIMATE2014',
    'POPESTIMATE2015']].max(axis=1)
    df['MIN'] = df[["POPESTIMATE2010",
    "POPESTIMATE2011",
    'POPESTIMATE2012',
    'POPESTIMATE2013',
    'POPESTIMATE2014',
    'POPESTIMATE2015']].min(axis=1)
    df['DIFF'] = df['MAX'] - df['MIN']
    return df[df['DIFF'] == max(df['DIFF'])]['CTYNAME']
# print answer_7(census_df)

# Question 8: Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
def answer_8(df):
    # df = df.where((df['STNAME'] != df['CTYNAME']) & (df['REGION'] == 1 | df['REGION'] == 2) & df['CTYNAME'].str.startswith('Washington') == True & df['POPESTIMATE2015'] > df['POPESTIMATE2014'])
    columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'REGION']
    df = df.where(df['CTYNAME'].str.startswith('Washington') == True).dropna()
    df = df.where(df['POPESTIMATE2015'] > df['POPESTIMATE2014']).dropna()
    df_1 = df.where(df['REGION'] == 1).dropna()
    df_2 = df.where(df['REGION'] == 2).dropna()
    df = pd.merge(df_1, df_2, how='outer')
    df = df[columns_to_keep].set_index('STNAME')
    return df
# print answer_8(census_df)

#----------------------------- Exercise--------------------------------------------------
# Use-Case: Find a difference in unemployment percentage between 2 years for a specific country
df = pd.read_csv('unemployed.csv', index_col=0)
def unemployed_change(df, code, year_1, year_2):
    if year_2 <= year_1:
        raise ValueError('Wrong order of years!')
    if code not in df['Country Code'].values:
        raise ValueError('Wrong country code!')

    df['Diff'] = df[str(year_2)] - df[str(year_1)]
    columns_to_keep = ['Country Code', str(year_1), str(year_2), 'Diff']
    df = df[columns_to_keep].loc[df['Country Code'] == code]
    if df['Diff'].values > 0:
        print 'Increased unemployment.'
    elif df['Diff'].values == 0:
        print 'Unchanged unemployment.'
    else:
        print 'Decreased unemployment.'
    return df
# print unemployed_change(df, 'AGO', 2010, 2011)

# Groupby exercise: Alcohol consumption by country

# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
# What is the average beer service by all countries
# average_beer_servings_countries = drinks.beer_servings.mean()
# What is the average beer service by continents
# average_beer_servings_continents = drinks.groupby('continent').beer_servings.mean()
# africa_average_drinks = drinks[drinks.continent == 'Africa'].beer_servings.mean()
# aggregation = drinks.groupby('continent').beer_servings.agg(['count', 'min', 'max', 'mean'])
# all_drinks_by_continent_average = drinks.groupby('continent').mean()
# print all_drinks_by_continent_average
# print drinks.head()

# Question 6 again:
def answer_6_a(df):
    df = df.where(df['CTYNAME'] != df['STNAME']).dropna()
    df = df.sort_values('CENSUS2010POP', ascending=False).groupby('STNAME')
    serie = pd.Series('Result')
    for table, content in df:
        serie[table] = content['CENSUS2010POP'][1:4].sum()
        sorted_serie = serie.sort_values(ascending=False)
    return sorted_serie[1:4]
# print answer_6_a(census_df)






