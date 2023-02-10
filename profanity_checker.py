import pandas as pd
import re

# list of racial slurs
slurs = ['word1', 'word2', ......, 'wordn']


# read the file containing the tweets into a Pandas DataFrame
# assuming data is in csv format 
df = pd.read_csv('tweets.csv', names=['tweet'])


# function to calculate the profanity level of a sentence
def profanity_level(sentence):
    # split sentence into words
    words = re.findall(r'\b\w+\b', sentence)
    # check each word against the list of slurs
    level = sum(1 for word in words if word.lower() in slurs)
    return level


# add a column to the DataFrame to store the profanity level of each tweet
df['profanity_level'] = df['tweet'].apply(profanity_level)

# display the tweets and their profanity levels
print(df)

