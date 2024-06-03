#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:01:34 2024

@author: ericagrace
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <-- format of read_csv

data = pd.read_csv('transaction2.csv', sep=';')

# working with calculations
# defining variables

# costPerItem = 11.73
# sellingPricePerItem = 21.11
# numberOfItemsPurchased = 6

#mathematical operations on tableau

# profitPerItem = sellingPricePerItem - costPerItem
# profitPerTransaction = numberOfItemsPurchased * profitPerItem
# costPerTransaction = numberOfItemsPurchased * costPerItem
# sellingPricePerTransaction = numberOfItemsPurchased *sellingPricePerItem

# calculations with whole columns
# variable = dataframe['columnName']

costPerItem = data['CostPerItem']
numberOfItemsPurchased = data['NumberOfItemsPurchased']
costPerTransaction = costPerItem * numberOfItemsPurchased

#adding a new column to a dataframe

data['CostPerTransaction'] = costPerTransaction

#sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit and markup

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = round(data['ProfitPerTransaction']/data['CostPerTransaction'],2)

# rounding markup to two decimals

#data['Markup'] = round(data['Markup'], 2) 

# combinging the date fields
# note data types must all be string to concatinate day and month and year into one field

data['Date'] = data['Day'].astype(str)+ '-' + data['Month'] + '-' + data['Year'].astype(str)

#using iloc to view specifif columns/rows

# data.iloc[0] #row with index = 0
# data.iloc[0:3] #first three rows
# data.iloc[-5:] #last 5 rows

# data.head(5) #first 5 rows

# data.iloc[4, 2] #4th row, second column
# data.iloc[:, 2] #all rows on second column

#split function
#using split to split up the client keywords column
#new_variable = column.split('sep', expand= True)

split_col = data['ClientKeywords'].str.split(',' , expand= True)

#creating new columns in data for these new columns
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#getting rid of the square brackets using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#changing text to lower case with lower()
data['ItemDescription'] = data['ItemDescription'].str.lower()

#merge data files - joining data
# bring in new data file:
    
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files - merge_df = pd.merge(df_one, df_two on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns - df = df.drop('columnname', axis = 1) axis zero is a row, one is a column

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1) #multiple columns

# export to csv - to_csv function

data.to_csv('ValueInc_Cleaned.csv', index = False)








