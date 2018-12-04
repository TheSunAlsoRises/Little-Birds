
class Script:

    def __init__(self, script_as_list):

        self.scriptID = script_as_list[0]
        self.analyzedWordsCounter = 0

        self.ambiguousWordsList = list()
        self.ambiguousWordsList_emotionsVector = list()
        self.ambiguousWordsList_instancesCount = list()
