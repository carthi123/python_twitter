# importing the required modules
import tweepy

# Getting the API from the my twitter account using tweepy
def get_twitter_api( ):
    # Consumer key, consumer secret, access token and access secret
    # from twitter application
    consumer_key = "bDa4E2lGtdIG5nd3bvDinpThH"
    consumer_secret = "KNF61HTnZMWJjizkwNo6tznmYcEB8zEUo9V0bjs8Lf9fKRVw6x"
    access_token = "863437146077581312-Zl4aeEog8hoZ5W3e0Q5DjRYlUTvy7JN"
    access_token_secret = "Ho4fz2AEckYc6BaXHVs1OuRyzAJdxADcbVmGqKa63UUBx"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

# Analysing the words form the tweets and returning number of positive and negative words.
def wordanalysis ( pos_words, neg_words, celeb_tweets ):
    pos = 0
    neg = 0
    celeb_word = celeb_tweets.split(" ")
    for i in celeb_word:
        if i in pos_words:
            pos += 1
        elif i in neg_words:
            neg += 1
    return pos, neg

#Analysing the celebrity details from tweets
def tweetanalysis( celeb_data ):
    api = get_twitter_api()
    pos_file = open("pos_word.txt",'r')
    neg_file = open("neg_word.txt",'r')
    pos_word = (pos_file.read()).split("\n")
    neg_word = (neg_file.read()).split("\n")
    for i in range(len(celeb_data)):
        positive = 0
        negative = 0
        celeb_tweets = api.search(celeb_data[i]["Name"], lang="en", locale="en", count = 50 )
        for tweets in celeb_tweets:
            p,n = wordanalysis( pos_word, neg_word, tweets.text )
            positive += p
            negative += n
        if positive > negative :
            celeb_data[i]["Twitter sentimental analysis"] = "POSITIVE"
        elif negative > positive :
            celeb_data[i]["Twitter sentimental analysis"] = "NEGATIVE"
        elif positive == negative :
            celeb_data[i]["Twitter sentimental analysis"] = "NEUTRAL"
    return celeb_data
