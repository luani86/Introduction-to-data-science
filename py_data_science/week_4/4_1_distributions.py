import pandas as pd
import numpy as np
# First number in parenthesis is number of runs and the second is the chance to get the 0.
# print np.random.binomial(1, 0.5) # Returns 1 or 0. 
# print np.random.binomial(10, 0.5) # Returns how many times we got 0 in 10 runs (about half of the times)
# print float(np.random.binomial(1000, 1))/1000 # Always returns 1.0 if the chance to get a 0 is 1

# Suppose we want to simulate the probability of flipping a fair coin 20 times, 
# and getting a number greater than or equal to 15. Use np.random.binomial(n, p, size) 
# to do 10000 simulations of flipping a fair coin 20 times, then see what proportion of the simulations 
# are 15 or greater.
x = np.random.binomial(20, .5, 10000)
result = (x>=15).mean()
# print result

chance_of_tornado = 0.01 / 100
# print np.random.binomial(100000, chance_of_tornado)

chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
two_days_in_a_row = 0
for j in range(1, len(tornado_events) -1):
    if tornado_events[j] == 1 and tornado_events[j - 1] == 1:
        two_days_in_a_row += 1
# print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))

# MORE DISTRIBUTIONS ------------------------------------------------------------------------------------
import scipy.stats as stats
distribution = np.random.normal(0.75,size=1000)
np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))
# print np.std(distribution)

# print stats.kurtosis(distribution)

# print stats.skew(distribution)
# chi_squared_df2 = np.random.chisquare(2, size=10000)
# print stats.skew(chi_squared_df2)
# chi_squared_df5 = np.random.chisquare(5, size=10000)
# print stats.skew(chi_squared_df5)
import matplotlib
import matplotlib.pyplot as plt
# output = plt.hist([chi_squared_df2,chi_squared_df5], bins=50, histtype='step', 
#                   label=['2 degrees of freedom','5 degrees of freedom'])
# plt.legend(loc='upper right')

# Hypothesis Testing ------------------------------------------------------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/sidsriv/Introduction-to-Data-Science-in-python/master/grades.csv')

# df.to_html('grades.html')
# Divide the df in 2 parts (students who applied early and late)
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']
# print len(early)
# print len(late)
# print df.head()

# Find the average grades of these 2 groups
print early.mean()
print late.mean()

# T test to see if there is significante difference in the average assignment1_grade for these 2 groups
print stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade']) 
# Because the pvalue is much larger than 0.05, we say that there is no significant difference
# Choosing the 0.05 for pvalue(alpha) as a treshold means that we expect the positive result in 5% of the sample

print stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade']) 
print stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade']) 
print stats.ttest_ind(early['assignment4_grade'], late['assignment4_grade']) 
print stats.ttest_ind(early['assignment5_grade'], late['assignment5_grade']) 
print stats.ttest_ind(early['assignment6_grade'], late['assignment6_grade']) 

# BUT! If we do many tests until we find 1 positive result that is p-hacking (wrong way). We have to avoid that
