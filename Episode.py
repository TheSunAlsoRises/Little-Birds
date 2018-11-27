class Episode:

    def __init__(self,episodeID,date,episodeName):
        self.episodeID = episodeID
        self.date = date
        self.episodeName = episodeName
        self.analyzedWordsCounter = 0

        self.ambiguousWordsList = list()
        self.ambiguousWordsList_instancesCount = list()
