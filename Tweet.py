
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


