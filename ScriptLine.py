
class ScriptLine:

    static_lines_counter = 1        # Counts all the lines in all the scripts (to give each line a unique IDs
    # static_scenes_counter = 0     -> Not needed for now

    def __init__(self,lineID,emotionsVec,text,location,speaker,scriptID):
        self.lineID = lineID
        self.emotionsVec = emotionsVec
        self.text = text
        self.location = location
        self.scriptID = scriptID

        self.episodeID = 0
        self.wordsCounter = 0
        self.ambiguousWordsList = list()
