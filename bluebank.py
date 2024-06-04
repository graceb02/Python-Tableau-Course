#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:10:28 2024

@author: ericagrace
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

# #method 1 to read json data
# json_file = open('loan_data_json.json')
# data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

# #finding unique values in purpose column
# print(loandata['purpose'].unique())

# #describe the data
# print(loandata.describe())

# #describing the data for a specific column
# print(loandata['int.rate'].describe())
# print(loandata['fico'].describe())

#numpy library - loaded with lots of math functions
#using exp to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual.income'] = income

#arrays
arr = np.array([1, 2, 4])

#if statements and for loops and try/except
#FICO score

ficocat = []
for fico in loandata['fico']:
    try:
        if fico >= 300 and fico < 400:
            cat = 'Very Poor'
        elif fico >= 400 and fico <600:
            cat = 'Poor'
        elif fico >= 600 and fico < 660:
            cat = 'Fair'
        elif fico >=660 and fico < 700:
            cat = 'Good'
        elif fico >=700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Error - Unknown'
    ficocat.append(cat)
   
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[columnname] condition, newcolname] = 'value if met'

#for interest rates, a new column is wanted.  rate >0.12 then high, else low
loandata.loc[loandata['int.rate'] >.12, 'int.rate.type'] = 'high'
loandata.loc[loandata['int.rate'] <=.12, 'int.rate.type'] = 'low'

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
#create a bar graph with matplotlib.pyplot
catplot.plot.bar(color='green', width = 0.6)
plt.show()

#group by purpose
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red')
plt.show()

# scatter plots
# annual income vs debt to income ratio
ypoint = loandata['annual.income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color='red')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index= True)

























