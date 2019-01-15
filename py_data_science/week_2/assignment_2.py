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

# def answer_zero():
#     # This function returns the row for Afghanistan, which is a Series object. The assignment
#     # question description will tell you the general format the autograder is expecting
#     return df.iloc[0]
# print answer_zero()
# print '-----------------------------------------------'
# print df.head()

# Question 1: Which country has won the most gold medals in summer games?

def answer_one():
    df_gold = df['Gold']
    return df[df['Gold'] == max(pd.Series(df_gold.values))]['ID']

# print answer_one()

# Question 2: Which country had the biggest difference between their summer gold (Gold) and winter gold (Gold.1) medal counts?
def answer_two():
    gold_summer = pd.Series(df['Gold'])
    gold_winter = pd.Series(df['Gold.1'])
    df['Difference'] = abs(gold_summer - gold_winter)
    # differences = pd.Series(df['Difference'])
    # max_diff = abs(max(differences))
    # df_max_diff = df[df['Difference'] == max_diff]
    # max_diff_country = df_max_diff['ID']
    return max(df['Difference']['ID'])
# print answer_two()
# print df.head()

# Question 3: Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
def answer_three():
    gold_summer = df['Gold']
    gold_winter = df['Gold.1']
    df['Total Gold'] = (gold_summer + gold_winter)
    df['Relative Difference'] = abs(gold_summer - gold_winter) / df['Total Gold']
    df['Relative Difference'] = df['Relative Difference'].where(df['Relative Difference'] != 1)
    return df['Relative Difference'].dropna().idxmax()
# print answer_three()
# print df.dropna()

# Question 4: Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2`) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
def answer_four():
    df['Points'] = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze.2']
    return df['Points']
# print answer_four()
# print df.head()
#------------------------------------ PART 2 ----------------------------------
census_df = pd.read_csv('census.csv')
# Question 5: Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
def answer_five():
    return census_df["STNAME"].value_counts().idxmax()
# print answer_five()

# Question 6: Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
df2 = census_df[['STNAME', 'CTYNAME', 'CENSUS2010POP']]
census_df_sorted = df2.sort_values(['STNAME','CENSUS2010POP'], ascending=False).groupby('STNAME')

new=pd.Series(["result"])

for table, content in census_df_sorted:
    new[table] = content["CENSUS2010POP"][1:4].sum()

# print new.head(5)
def answer_six():
    # return census_df.index.values[0: 3]
    return census_df
# print answer_six()
# print census_df['CENSUS2010POP']

#----------------- WRONG -----------------
# def answer_six():
#     largest_pop = census_df['CENSUS2010POP'].sort_values()[len(census_df['CENSUS2010POP']) - 1]
#     sub_largest_pop = census_df['CENSUS2010POP'].sort_values()[len(census_df['CENSUS2010POP']) - 2]
#     sub_sub_largest_pop = census_df['CENSUS2010POP'].sort_values()[len(census_df['CENSUS2010POP']) - 3]
#     # max_country = census_df[census_df['CENSUS2010POP'] == largest_pop]['STNAME']
#     # sub_max_country = census_df[census_df['CENSUS2010POP'] == sub_largest_pop]['STNAME']
#     # sub_sub_max_country = census_df[census_df['CENSUS2010POP'] == sub_sub_largest_pop]['STNAME']
#     # return (max_country, sub_max_country, sub_sub_max_country)
#----------------- WRONG -----------------

# Question 7: Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
census_df=census_df[census_df["STNAME"] != census_df["CTYNAME"]]


def answer_seven():
    census_df['MAX'] = census_df[["POPESTIMATE2010",
    "POPESTIMATE2011",
    'POPESTIMATE2012',
    'POPESTIMATE2013',
    'POPESTIMATE2014',
    'POPESTIMATE2015']].max(axis=1)

    census_df['MIN'] = census_df[["POPESTIMATE2010",
    "POPESTIMATE2011",
    'POPESTIMATE2012',
    'POPESTIMATE2013',
    'POPESTIMATE2014',
    'POPESTIMATE2015']].min(axis=1)
    census_df['DIFF'] = census_df['MAX'] - census_df['MIN']
    unique = census_df["STNAME"].value_counts().values
    max_diff = max(census_df['DIFF'])
    max_diff_county = census_df[census_df['DIFF'] == max_diff]['CTYNAME']
    # census_df['U'] = census_df["STNAME"].value_counts()
    return max_diff_county
# print answer_seven()
# print census_df.head()
# print census_df[census_df['CTYNAME'] == 'Harris County']

# Question 8: Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
import pandas as pd
import numpy as np
census_df = pd.read_csv('census.csv')
def answer_eight():
    census_df['DIFF'] = census_df['POPESTIMATE2015'] - census_df['POPESTIMATE2014']
answer_eight()
# census_df = census_df[census_df['CTYNAME'][0:10] == 'Washington']
census_df = census_df[census_df['CTYNAME'].str.startswith('Washington') == True]
census_df = census_df[census_df['DIFF'] > 0]
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'REGION']
census_df = census_df[columns_to_keep]
census_df = census_df.reset_index() 
census_df.sort_values(['index'], ascending=[False])
census_df = census_df.set_index('index') 
census_df_1 = census_df[census_df['REGION'] == 1]
# print census_df_1
# print '--------------------------------------------'
census_df_2 = census_df[census_df['REGION'] == 2]
# print census_df_2
