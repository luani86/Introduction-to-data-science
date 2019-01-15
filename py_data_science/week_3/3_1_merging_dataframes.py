import numpy as np
import pandas as pd
df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
df['Date'] = ['December 1', 'January 1', 'mid-May']
df['Delivered'] = True
df['Feedback'] = ['Positive', None, 'Negative']
adf = df.reset_index()
adf['Date'] = pd.Series({0: 'December 1', 1: 'mid-May'})
# print adf

############################################ Merging Dataframes
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

mergedOuter = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
mergedInner = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
mergedLeft = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
mergedRight = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
# print staff_df
# print student_df
# print mergedOuter
# print mergedInner
# print mergedLeft
# print mergedRight
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
merged = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
# print merged

############################ Merge product and invoices
products_df = pd.DataFrame([{'Product ID': 4109, 'Price': 5.0, 'Product': 'Sushi Roll'},
                            {'Product ID': 1412, 'Price': 0.5, 'Product': 'Egg'},
                            {'Product ID': 8931, 'Price': 1.5, 'Product': 'Bagel'}])
invoices_df = pd.DataFrame([{'Customer': 'Ali', 'Product ID': 4109, 'Quantity': 1},
                            {'Customer': 'Eric', 'Product ID': 1412, 'Quantity': 12},
                            {'Customer': 'Ande', 'Product ID': 8931, 'Quantity': 6},
                            {'Customer': 'Sam', 'Product ID': 4109, 'Quantity': 2}])
totals_df = pd.merge(products_df, invoices_df, how='outer')
totals_df['Total Price'] = totals_df['Price'] * totals_df['Quantity']
# print products_df
# print invoices_df
# print totals_df

########################## Overlapping names
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
merged = pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
# print merged
x = 109
print round((float(x)-32) * 5/9, 1)