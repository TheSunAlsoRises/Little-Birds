import Episode

class Tweet:
    #
    # def __init__(self,date,tweetID,userID,userName,location,text,emotionsVec,episodeID,cleanText):
    #     self.date = date
    #     self.tweetID = tweetID
    #     self.userID = userID
    #     self.userName = userName
    #     self.location = location
    #     self.text = text
    #     self.emotionsVec = emotionsVec
    #     self.episodeID = 0
    #     self.cleanText = cleanText
    #
    #     self.wordsCounter = 0
    #
    #     self.ambiguousWordsList = list()


     def __init__(self,tweet_as_list):
           self.date = tweet_as_list[0]
           self.tweetID = tweet_as_list[2]
           self.userID = tweet_as_list[3]
           self.userName = tweet_as_list[4]
           self.location = tweet_as_list[5]
           self.text = tweet_as_list[6]
           self.emotionsVec = tweet_as_list[10]
           self.episodeID = tweet_as_list[11]
           self.cleanText = tweet_as_list[12]

           self.wordsCounter = 0
           self.ambiguousWordsList = list()
