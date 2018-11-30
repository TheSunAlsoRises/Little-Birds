class Episode:

    def __init__(self,episodeID,date,episodeName):
        self.episodeID = episodeID
        self.date = date
        self.episodeName = episodeName
        self.analyzedWordsCounter = 0

        self.ambiguousWordsList = list()
        self.ambiguousWordsList_emotionsVector = list()
        self.ambiguousWordsList_instancesCount = list()


    # def __init__(self, episode_as_list):
    #     self.episodeID = episode_as_list[0]
    #     self.episodeName = episode_as_list[1]
    #     self.date = episode_as_list[2]
    #     self.analyzedWordsCounter = 0
    #
    #     self.ambiguousWordsList = list()
    #     self.ambiguousWordsList_emotionsVector = list()
    #     self.ambiguousWordsList_instancesCount = list()