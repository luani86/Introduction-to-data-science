import numpy as np
import pandas as pd
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
grades = df['Grades'].astype('category')
# grades_ordered = df['Grades'].astype('category',
#                              categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
#                              ordered=True)
# print grades_ordered >= 'C'

# Task: Casting series with ordering
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
df = pd.DataFrame(s)
df.rename(columns={0: 'Level'}, inplace=True)
# df_ordered = df['Level'].astype('category', categories=['Low', 'Medium', 'High'], ordered=True)
# print df_ordered > 'Medium'
# print df_ordered

df = pd.read_csv('census.csv')
df = df[df['SUMLEV'] == 50]
# df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
# It seems thhat cut groups values i intervals
# df_cut = pd.cut(df['avg'], 10)
# print df_cut

# Task: Group sizes to 3 categories
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
s_cut = pd.cut(s, 3, labels= ['Small', 'Medium', 'Large'])
# print s_cut
df = pd.read_csv('cars.csv')
df_pivot = df.pivot_table(values='price', index='color', columns='name', aggfunc=np.mean)
print df_pivot