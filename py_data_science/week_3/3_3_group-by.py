########################## Spliting the data
import numpy as np
import pandas as pd
df = pd.read_csv('census.csv')
df = df[df['SUMLEV'] == 50]
df = df.set_index('STNAME')
# Does not work!!!
# for state in df['STNAME'].unique():
#     avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    # print ('Counties in state ' + state + ' have an average population of ' + str(avg)')

# Does not work!!!
# for group, frame in df.groupby('STNAME'):
#     avg = np.average(frame['CENSUS2010POP'])
#     print 'Counties in state ' + state + ' have an average population of ' + str(avg)'

############################# Applying a function to the splitted data

def fun(item):
    if item[0] == 'M':
        return 0
    if item[0] == 'Q':
        return 1
    return 2
# for group, frame in df.groupby(fun):
#     print 'There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.'

df = pd.read_csv('census.csv')
df = df[df['SUMLEV'] == 50]
df = df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
# print df.head()

# Average amount of items in packing by category I:
# df = pd.read_csv('packing.csv').set_index('Category')
# avg_amount = df.groupby('Category').agg({'Amount': np.average})
# print avg_amount

# Average amount of items in packing by category II:
# df = pd.read_csv('packing.csv').set_index('Category')
# for group, amount in df.groupby('Category'):
#     avg = np.average(amount['Amount'])
#     print group + ' contains ' + str(avg) + ' items on average.'

df = pd.read_csv('census.csv')
# df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum})
df = (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011'].agg({'avg': np.average, 'sum': np.sum}))
# df = (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011'].agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))
print df


