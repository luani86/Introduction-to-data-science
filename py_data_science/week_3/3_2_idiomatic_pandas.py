import pandas as pd
df = pd.read_csv('census.csv')
pandorable_df =(df.where(df['SUMLEV'] == 50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'RNETMIG2014': 'RNETMIG 2014', 'RNETMIG2015': 'RNETMIG 2015'}))
# print pandorable_df.head()

nonpandorable_df = df[df['SUMLEV']==50]
nonpandorable_df.set_index(['STNAME','CTYNAME'], inplace=True)
nonpandorable_df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
# print nonpandorable_df.head()

# Remove rows where amount is 0 and rename column from Amount to Amount of item
packing = pd.read_csv('packing.csv', index_col = 0)
pandorable_packing_df = (packing.where(packing['Amount'] > 0)
    .dropna()
    .rename(columns={'Amount': 'Amount of item'})
    )
# print pandorable_packing_df

######################################
import numpy as np
# def min_max(row):
#     data = row[['POPESTIMATE2010',
#                 'POPESTIMATE2011',
#                 'POPESTIMATE2012',
#                 'POPESTIMATE2013',
#                 'POPESTIMATE2014',
#                 'POPESTIMATE2015']]
#     return pd.Series({'min': np.min(data), 'max': np.max(data)})
# print df.head()
# print min_max(df)

################################ Add min and max columns
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
df=df.apply(min_max, axis=1)
# print min_max(df)
# print df.head()

############################### Lambda
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df=df.apply(lambda x: np.max(x[rows]), axis=1)
# print df.head()
