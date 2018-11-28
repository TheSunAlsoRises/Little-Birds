
class Tweet:

    def __init__(self,tweetID,date,userName,text,cleanText,emotionsVec):
        self.tweetID = tweetID
        self.date = date
        self.userName = userName
        self.text = text
        self.cleanText = cleanText
        self.emotionsVec = emotionsVec

        self.episodeID = 0
        self.wordsCounter = 0
        self.ambiguousWordsList = list()


    def __init__(self,tweet_as_list):
        self.tweetID = tweet_as_list[2]
        self.date = tweet_as_list[0]
        self.userName = tweet_as_list[5]
        self.text = tweet_as_list[6]
        self.cleanText = tweet_as_list[9]
        self.emotionsVec = tweet_as_list[7]
        self.episodeID = tweet_as_list[8]

        self.wordsCounter = 0
        self.ambiguousWordsList = list()