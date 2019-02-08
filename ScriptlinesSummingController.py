import DBconnect

#CONVERT TUPLE TO LIST FUNCTION
def tupleToList(t):
    emptyList = list()
    for i in range(0,len(t)):
        emptyList.append(list(t[i]))
    return emptyList


class ScriptlinesSummingController:

    def __init__(self, scriptlinesSummingAsList):
        self.scriptlines_counter = 0
        self.summed_scriptlines_counter = 0
        self.requested_episode = scriptlinesSummingAsList[0]
    #    self.total_scriptlines = scriptlinesSummingAsList[1]
        self.total_scriptlines = 1
        self.category = scriptlinesSummingAsList[2]
        self.selected = scriptlinesSummingAsList[3]
        self.total_vector = [0] * 8
        self.representive_scriptline_ID1 = ""
        self.representive_scriptline_ID2 = ""
        self.scriptlineText1 = ""
        self.scriptlineText2 = ""

    def scriptlinesSumming(self):

        if self.category == "character":

            # COLLECT ALL CHARACTER NICK NAMES
            q = '"'
            query_string = "select Nick from nick where CategoryID = 1 and SubID = " \
                           "(select CharacterID from category where CharacterName like " + q + self.selected + q + ")"
            result = DBconnect.DBconnect.send_query(query_string)
            if result is not None:

                character_nicks = tupleToList(result)

                name = self.selected
                nicks = []
                for i in character_nicks:
                    tmp = i
                    tmp = ''.join(tmp)
                    nicks.append(tmp)
                character_nicks = nicks

                allNicksQuery = "SELECT * FROM littlebirds.scriptline WHERE ScriptID = " + str(self.requested_episode) + " AND (" \
                                "CleanText like " + q + "%" + str(name) + "%" + q
                for nick in character_nicks:
                    if str(nick) == "ned" or str(nick) == "sam":
                        nick = " " + str(nick) + " "
                    allNicksQuery += " or CleanText like " + q + "%" + str(nick) + "%" + q
                # Close the right argument to 'AND'
                allNicksQuery += ")"

                result = DBconnect.DBconnect.send_query(allNicksQuery)
                scriptlines = tupleToList(result)

                for scriptline in scriptlines:
                    self.addVector(scriptline)

            else:
                print("not in DB!")

        elif self.category == "house":

            # COLLECT ALL CHARACTERS FROM SPECIFIC HOUSE
            q = "'"
            query_string = "SELECT CharacterName FROM category where HouseName like " + q + "%" \
                           + str(self.selected) + "%" + q + " and CharacterName is not null"
            result = DBconnect.DBconnect.send_query(query_string)
            if result is not None:
                characters_house = tupleToList(result)
                characters = []
                for i in characters_house:
                    tmp = i
                    tmp = ''.join(tmp)
                    characters.append(tmp)
                characters_house = characters

            house = self.selected
                                # Houses names are rare in other meanings, so no need in spaces before and after
            allCharactersQuery = "SELECT * FROM littlebirds.scriptline WHERE ScriptID = " + str(self.requested_episode) + " AND (" \
                                 "CleanText like " + q + "%" + str(house) + "%" + q

            for character in characters_house:
                # COLLECT ALL CHARACTERS NICKS
                character_nicks = []
                if character != house:
                    q = "'"
                    query_string = "select Nick from nick where CategoryID = 1 and SubID = " \
                           "(select CharacterID from category where CharacterName like " + q + " " + str(character) + " " + q + ")"
                    result = DBconnect.DBconnect.send_query(query_string)
                    character_nicks = tupleToList(result)

                    nicks = []
                    for i in character_nicks:
                        tmp = i
                        tmp = ''.join(tmp)
                        nicks.append(tmp)
                    character_nicks = nicks

                # Add the 'formal name'
                character_nicks.append(str(character))

                for nick in character_nicks:
                    if str(nick) == "ned" or str(nick) == "sam":
                        nick = " " + str(nick) + " "
                    allCharactersQuery += " or CleanText like " + q + "%" + str(nick) + "%" + q

            # Close the right argument to 'AND'
            allCharactersQuery += ")"

            result = DBconnect.DBconnect.send_query(allCharactersQuery)
            scriptlines = tupleToList(result)

            for scriptline in scriptlines:
                self.addVector(scriptline)

        elif self.category == "location":

            # COLLECT ALL LOCATION NICK NAMES
            q = '"'
            # Locations names are rare in other meanings, so no need in spaces before and after
            query_string = "SELECT Nick FROM nick where CategoryID = 2 and SubID = " \
                           "(select LocationID from category where LocationName like " \
                           + q + str(self.selected) + q + ")"
            result = DBconnect.DBconnect.send_query(query_string)

            if result is not None:

                location_nicks = tupleToList(result)
                location = self.selected
                nicks = []
                for i in location_nicks:
                    tmp = i
                    tmp = ''.join(tmp)
                    nicks.append(tmp)
                location_nicks = nicks

                allNicksQuery = "SELECT * FROM littlebirds.scriptline WHERE ScriptID = " + str(self.requested_episode) + " AND (" \
                                              "CleanText like " + q + "%" + str(location) + "%" + q
                for nick in location_nicks:
                    allNicksQuery += " or CleanText like " + q + "%" + str(nick) + "%" + q
                # Close the right argument to 'AND'
                allNicksQuery += ")"

                result = DBconnect.DBconnect.send_query(allNicksQuery)
                scriptlines = tupleToList(result)

                for scriptline in scriptlines:
                    self.addVector(scriptline)

            else:
                print("not in DB!")

        query_string = "SELECT Text FROM scriptline WHERE LineID like "\
                       + q + str(self.representive_scriptline_ID1) + q
        result = tupleToList(DBconnect.DBconnect.send_query(query_string))

        try:
            self.scriptlineText1 = result[0][0]
        except IndexError:
            self.scriptlineText1 = ""

        query_string = "SELECT Text FROM scriptline WHERE LineID like " \
                       + q + str(self.representive_scriptline_ID2) + q
        result = tupleToList(DBconnect.DBconnect.send_query(query_string))

        try:
            self.scriptlineText2 = result[0][0]
        except IndexError:
            self.scriptlineText2 = ""

        print("\n\nsummed scriptlines: " + str(self.summed_scriptlines_counter) + "\n\n")
        if self.summed_scriptlines_counter == 0:
            return None
        else:
            return [self.total_vector, self.scriptlineText1, self.scriptlineText2, self.summed_scriptlines_counter]

    def addVector(self, scriptline):

        self.scriptlines_counter += 1

        self.summed_scriptlines_counter += 1

        vector = scriptline[1].split(" ")
        newVector = [0.0] * 8
        for i in range(len(newVector)):
            newVector[i] = float(vector[i])

        for i in range(len(newVector)):
            self.total_vector[i] += newVector[i]

        cleanText = scriptline[3].split(" ")
        if self.scriptlines_counter > 0.9 * self.total_scriptlines and len(cleanText) > 7:
            self.locateRepresentativeScriptlinesProcedure(scriptline)

    def locateRepresentativeScriptlinesProcedure(self, scriptline):
        self.distance_from_total = 0
        self.current_distance1 = 100
        self.current_distance2 = 100

        scriptline_vector = scriptline[1].split(" ")
        maximal_value = max(self.total_vector)
        if maximal_value == 0:
            maximal_value = 0.1

        normalized_total_vector = [0.0] * 8
        for i in range(len(normalized_total_vector)):
            normalized_total_vector[i] = self.total_vector[i]

        for i in range(len(normalized_total_vector)):
            normalized_total_vector[i] = normalized_total_vector[i] / maximal_value
            # Round to three digits after the decimal point
            normalized_total_vector[i] = round(normalized_total_vector[i], 3)

        substitution_vector = []
        for i in range(len(scriptline_vector)):
            scriptline_vector[i] = float(scriptline_vector[i])
            substitution_vector.append(abs(scriptline_vector[i] - normalized_total_vector[i]))

        for value in substitution_vector:
            self.distance_from_total += value

        if (self.current_distance1 > self.distance_from_total):
            self.current_distance2 = self.current_distance1
            self.representive_scriptline_ID2 = self.representive_scriptline_ID1
            self.current_distance1 = self.distance_from_total
            self.representive_scriptline_ID1 = scriptline[0]
        elif (self.current_distance2 > self.distance_from_total):
            self.current_distance2 = self.distance_from_total
            self.representive_scriptline_ID2 = scriptline[0]
