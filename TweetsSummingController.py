import DBconnect

#CONVERT TUPLE TO LIST FUNCTION
def tupleToList(t):
    emptyList = list()
    for i in range(0,len(t)):
        emptyList.append(list(t[i]))
    return emptyList


class TweetsSummingController:

    def __init__(self, TweetsSumming_as_list):
        self.tweets_counter = 0
        self.requested_episode = TweetsSumming_as_list[0]
        self.total_tweets = TweetsSumming_as_list[1]
        self.category = TweetsSumming_as_list[2]
        self.selected = TweetsSumming_as_list[3]
        self.total_vector = [0] * 8

    def tweetSumming(self):
        tweets = ()
        query_string = "SELECT * FROM tweet WHERE EpisodeID=" + str(self.requested_episode)
        result = DBconnect.DBconnect.send_query(query_string)
        tweets = tupleToList(result)

        stop = 0
        if (self.category == "character"):

            # COLLECT ALL CHARACTER NICK NAMES
            character_nicks = ()

            q = '"'
            query_string = "select Nick from nick where SubID = " \
                           "(select CharacterID from category where CharacterName like " + q + self.selected + q + ")";
            result = DBconnect.DBconnect.send_query(query_string)
            character_nicks = tupleToList(result)

            nicks = []
            nicks.append(self.selected)
            for i in character_nicks:
                tmp = i
                tmp = ''.join(tmp)
                nicks.append(tmp)
            character_nicks = nicks

            for tweet in tweets:
                self.tweets_counter+=1
                cleanText = tweet[12]

                for nick in character_nicks:
                    if nick in cleanText:
                        vector = tweet[10].split(" ")
                        newVector = []
                        for i in vector:
                            x = (int(i))
                            newVector.append(x)

                        for i in range(len(newVector)):
                            self.total_vector[i] += newVector[i]

                        cleanText = tweet[12].split(" ")
                        if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                            self.locateRepresentativetweetsprocedure(self, newVector)


        elif (self.category == "house"):

            # COLLECT ALL CHARATERS FROM SPECIFIC HOUSE
            characters_house = ()

            q = '"'
            query_string = "SELECT CharacterName FROM category where HouseName like " + q + "%" \
                           + str(self.selected) + "%" + q + " and CharacterName is not null";
            result = DBconnect.DBconnect.send_query(query_string)
            if (result != 0):
                characters_house = tupleToList(result)
                characters = []
                for i in characters_house:
                    tmp = i
                    tmp = ''.join(tmp)
                    characters.append(tmp)
                characters_house = characters

            for tweet in tweets:
                self.tweets_counter+=1
                cleanText = tweet[12]

                house = self.selected
                if house in cleanText:
                    vector = tweet[10].split(" ")
                    newVector = []
                    for i in vector:
                        x = (int(i))
                        newVector.append(x)

                    for i in range(len(newVector)):
                        self.total_vector[i] += newVector[i]

                    cleanText = tweet[12].split(" ")
                    if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                        self.locateRepresentativetweetsprocedure(self, newVector)
                    stop = 1

                if stop == 0:
                    for character in characters_house:
                        #COLLECT ALL CHARACTERS NICKS
                        character_nicks = ()

                        q = '"'
                        query_string = "select Nick from nick where SubID = " \
                               "(select CharacterID from category where CharacterName like "+ q + str(character) + q + ")";
                        result = DBconnect.DBconnect.send_query(query_string)
                        character_nicks = tupleToList(result)

                        nicks = []
                        nicks.append(str(character))
                        for i in character_nicks:
                            tmp = i
                            tmp = ''.join(tmp)
                            nicks.append(tmp)
                        character_nicks = nicks

                        for nick in character_nicks:
                            if nick in cleanText:
                                vector = tweet[10].split(" ")
                                newVector = []
                                for i in vector:
                                    x = (int(i))
                                    newVector.append(x)

                                for i in range(len(newVector)):
                                    self.total_vector[i] += newVector[i]

                                cleanText = tweet[12].split(" ")
                                if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                                    self.locateRepresentativetweetsprocedure(self, newVector)

                else: stop = 0;


        elif (self.category == "location"):

            # COLLECT ALL LOCATION NICK NAMES
            location_nicks = ()
            q = '"'
            query_string = "SELECT Nick FROM nick where CategoryID = 2 and SubID = " \
                           "(select LocationID from category where LocationName like " \
                           + q + str(self.selected) + q + ")";
            result = DBconnect.DBconnect.send_query(query_string)

            if (result != 0):
                location_nicks = tupleToList(result)
                nicks = []
                nicks.append(str(self.selected))
                for i in location_nicks:
                    tmp = i
                    tmp = ''.join(tmp)
                    nicks.append(tmp)
                location_nicks = nicks

                for nick in location_nicks:
                    for tweet in tweets:
                        self.tweets_counter+=1
                        cleanText = tweet[12]

                        if nick in cleanText:
                            vector = tweet[10].split(" ")
                            newVector = []
                            for i in vector:
                                x = (int(i))
                                newVector.append(x)

                            for i in range(len(newVector)):
                                self.total_vector[i] += newVector[i]

                            cleanText = tweet[12].split(" ")
                            if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                                self.locateRepresentativetweetsprocedure(self, newVector)

        return self.total_vector



    def locateRepresentativetweetsprocedure(self,tweet_vector):
        distance_from_total = 0
        current_distance1 = 100
        current_distance2 = 100

        representive_tweet1 = ""
        representive_tweet2 = ""

        maximal_value = max(self.total_vector)
        normalized_total_vector = self.total_vector
        for i in range(len(normalized_total_vector)):
            normalized_total_vector[i] //= maximal_value

        substitution_vector = []
        for i in range(len(tweet_vector)):
            substitution_vector.append(abs(tweet_vector - normalized_total_vector))

        for value in substitution_vector:
            distance_from_total+=value

        if (representive_tweet1 > distance_from_total):
            representive_tweet2 = representive_tweet1
            representive_tweet1 = distance_from_total

        elif (representive_tweet2 > distance_from_total):
            representive_tweet2 = distance_from_total
            










