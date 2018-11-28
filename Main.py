
import DBconnect
import AnalysisController
import Tweet
import Episode


AnalysisController.AnalysisController.analyze_tweets_by_episode()

emotionsVector = [1,2]

cleanText = ["pretty","Jon","is","the","love", "love","of","my","beautiful","life"]

tweet = Tweet.Tweet(1,"1/1/00","name",
                     "pretty Jon is the love of my beautiful life",
                     cleanText,[])

episode = Episode.Episode(1,"","")

AnalysisController.AnalysisController.analyze_tweet(tweet,episode)



#query_string = "SELECT count(*) FROM tweet"
#result = DBconnect.DBconnect.send_query(query_string)