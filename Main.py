from nltk.stem import WordNetLemmatizer

import CleaningTweetsController
import DBconnect
import AnalysisController
import Tweet
import Episode
import ScriptFilesController


#ScriptFilesController.ScriptFilesController.file_to_scriptLines("C://Users\אליה\PycharmProjects\script1.txt",1)
#ScriptFilesController.ScriptFilesController.file_to_scriptLines("C://Users\אליה\PycharmProjects\script2.txt",2)

#AnalysisController.AnalysisController.analyze_tweets_by_episode()

#emotionsVector = [1,2]

CleaningTweetsController.CleaningTweetsController.cleanTweets();

#DBconnect.DBconnect.upload_tweets_file()

#cleanText = ["Jon","is","not","that","pretty"]

#tweet = Tweet.Tweet(1,"1/1/00","name","pretty Jon is not the love of my beautiful life",cleanText,[])

#episode = Episode.Episode(1,"","")

#AnalysisController.AnalysisController.analyze_tweet(tweet,episode)



#query_string = "SELECT count(*) FROM tweet"
#query_string = "SELECT * FROM tweets"

#result = DBconnect.DBconnect.send_query(query_string)
