
class ScriptLine:

    static_lines_counter = 1        # Counts all the lines in all the scripts (to give each line a unique IDs
    # static_scenes_counter = 0     -> Not needed for now

    def __init__(self,scriptline_as_list):
        self.lineID = scriptline_as_list[0]
        self.emotionsVec = scriptline_as_list[1]
        self.text = scriptline_as_list[2]

        # will be:
        #self.cleanText = scriptline_as_list[3]

        # for now:
        self.cleanText = scriptline_as_list[2].split()

        self.location = scriptline_as_list[4]
        self.speaker = scriptline_as_list[5]
        self.scriptID = scriptline_as_list[6]

        self.wordsCounter = 0
        self.ambiguousWordsList = list()

    #
    # def __init__(self,lineID,emotionsVec,text,cleanText,location,speaker,scriptID):
    #     self.lineID = lineID
    #     self.emotionsVec = emotionsVec
    #     self.text = text
    #     self.cleanText = cleanText
    #     self.location = location
    #     self.speaker = speaker
    #     self.scriptID = scriptID
    #
    #     self.episodeID = 0
    #     self.wordsCounter = 0
    #     self.ambiguousWordsList = list()
