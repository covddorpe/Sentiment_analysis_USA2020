import pandas as pd
from langdetect import detect
   

# Importation des dataframe
df_biden = pd.read_csv('/Users/nadia/Desktop/COURS/BIR22/DataScience/Sentiment_Analysis/hashtag_joebiden.csv', lineterminator='\n', parse_dates=True)
df_trump = pd.read_csv('/Users/nadia/Desktop/COURS/BIR22/DataScience/Sentiment_Analysis/hashtag_donaldtrump.csv', lineterminator='\n', parse_dates=True) 


# Sélection de la colonne des tweets
columns = ['created_at','tweet','state','country']
tweets_biden = df_biden[columns].query("created_at < '2020-11-04'").values.tolist()
tweets_trump = df_trump[columns].query("created_at < '2020-11-04'").values.tolist()


# Création d'une méthode pour supprimer les tweets présents dans les deux datasets
def cleanList(listTweet, listHashtag) :
    cleanedList = [] 
    for tweet in listTweet:
        if not any(hashtag.upper() in tweet[1].upper() for hashtag in listHashtag):
            cleanedList.append(tweet)
    return cleanedList

cleanedTweetsTrump = cleanList(tweets_trump,['#JoeBiden', '#Biden'] );
cleanedTweetsBiden = cleanList(tweets_biden,['#DonaldTrump', '#Trump'] );


# Création d'une méthode pour ne garder que les tweets en anglais
def getOnlyEnglishTweets(listTweet) :
    onlyEnglishTweetsList = [] 
    for tweet in listTweet:
        try:
            if detect(tweet[1]) == 'en' :
                onlyEnglishTweetsList.append(tweet)
        except:
            pass
    return onlyEnglishTweetsList

englishTweetsTrump = pd.DataFrame(getOnlyEnglishTweets(cleanedTweetsTrump))
englishTweetsBiden = pd.DataFrame(getOnlyEnglishTweets(cleanedTweetsBiden))

englishTweetsBiden.columns = columns
englishTweetsTrump.columns = columns

englishTweetsTrump.to_csv(r'/Users/nadia/Desktop/COURS/BIR22/DataScience/Sentiment_Analysis/export_englishTweetsTrump.csv', index = False)
englishTweetsBiden.to_csv(r'/Users/nadia/Desktop/COURS/BIR22/DataScience/Sentiment_Analysis/export_englishTweetsBiden.csv', index = False)
