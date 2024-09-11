#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:56:32 2024

@author: ericagrace
"""

#how do you read an excell fil
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel/xlsx files
data = pd.read_excel('articles.xlsx')

# #summary of the data
# data.describe()
# data.info()

# #counting the number of articles per source
# #format of groupby: df.groupby(['column to group'])['column to count'].count()
# data.groupby(['source_id'])['article_id'].count()
# #number of reactions by publisher
# data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column
data = data.drop('engagement_comment_plugin_count' , axis=1)

# #creating a keyword flag
# keyword = 'crash'
# #for loop to isolate each title
# length = len(data)
# keyword_flag = []
# for x in range(0, length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
    
#creating a function
def keywordFlag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0, length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
        
k = keywordFlag('murder')        

# creating a new column in the dataframe
data['keyword_flag'] = pd.Series(k)

# sentimemt analysis with vader
# #sentimentintensityanalyzer

# sent_int = SentimentIntensityAnalyzer()

# text = data['title'][16]
# sent = sent_int.polarity_scores(text)

# neg = sent['neg']
# pos = sent['pos']
# neu = sent['neu']
        

#loop through all the titles

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)    
    title_neu_sentiment.append(neu)
        
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
        
data['title_neg_sentiment'] = title_neg_sentiment  
data['title_neu_sentiment'] = title_neu_sentiment
data['title_pos_sentiment'] = title_pos_sentiment        
        
#writing the data 

data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index=False)
        
        
        
        
        
        
        
        
        
        
        