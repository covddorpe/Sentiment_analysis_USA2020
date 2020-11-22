import pandas as pd
from langdetect import detect
   

# Importation des dataframe
df_biden = pd.read_csv('/Users/nadia/Desktop/COURS/BIR22/DataScience/Sentiment_Analysis/hashtag_joebiden.csv', lineterminator='\n', parse_dates=True)
df_trump = pd.read_csv('/Users/nadia/Desktop/COURS/BIR22/DataScience/Sentiment_Analysis/hashtag_donaldtrump.csv', lineterminator='\n', parse_dates=True) 


# Sélection de la colonne des tweets
tweets_biden = df_biden['tweet']
tweets_trump = df_trump['tweet']


# Création d'une méthode pour supprimer les tweets présents dans les deux datasets
def cleanList(listTweet, listHashtag) :
    cleanedList = [] 
    for tweet in listTweet:
        if not any(hashtag.upper() in tweet.upper() for hashtag in listHashtag):
            cleanedList.append(tweet)
    return cleanedList

cleanedTweetsTrump = cleanList(tweets_trump,['#JoeBiden', '#Biden'] );
cleanedTweetsBiden = cleanList(tweets_biden,['#DonaldTrump', '#Trump'] );


# Création d'une méthode pour ne garder que les tweets en anglais
def getOnlyEnglishTweets(listTweet) :
    onlyEnglishTweetsList = [] 
    for tweet in listTweet:
        try:
            if detect(tweet) == 'en' :
                onlyEnglishTweetsList.append(tweet)
        except:
            pass
    return onlyEnglishTweetsList

englishTweetsTrump = getOnlyEnglishTweets(cleanedTweetsTrump)
englishTweetsBiden = getOnlyEnglishTweets(cleanedTweetsBiden)