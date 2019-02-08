import DBconnect

#CONVERT TUPLE TO LIST FUNCTION
def tupleToList(t):
    emptyList = list()
    for i in range(0,len(t)):
        emptyList.append(list(t[i]))
    return emptyList


class TweetsSummingController:

    def __init__(self, tweetsSummingAsList):
        self.tweets_counter = 0
        self.summed_tweets_counter = 0
        self.requested_episode = tweetsSummingAsList[0]
    #    self.total_tweets = TweetsSumming_as_list[1]
        self.total_tweets = 1
        self.category = tweetsSummingAsList[2]
        self.selected = tweetsSummingAsList[3]
        self.total_vector = [0] * 8
        self.representive_tweet_ID1 = ""
        self.representive_tweet_ID2 = ""
        self.tweetText1 = ""
        self.tweetText2 = ""
        self.author1 = ""
        self.author2 = ""

    def tweetsSumming(self):

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

                allNicksQuery = "SELECT * FROM littlebirds.tweet WHERE EpisodeID = " + str(self.requested_episode) + " AND (" \
                                "CleanText like " + q + "%" + str(name) + "%" + q
                for nick in character_nicks:
                    if str(nick) == "ned" or str(nick) == "sam":
                        nick = " " + str(nick) + " "
                    allNicksQuery += " OR CleanText like " + q + "%" + str(nick) + "%" + q
                # Close the right argument to 'AND'
                allNicksQuery += ")"

                result = DBconnect.DBconnect.send_query(allNicksQuery)
                tweets = tupleToList(result)

                for tweet in tweets:

                    self.tweets_counter += 1
                    cleanText = tweet[12]

                    self.summed_tweets_counter += 1

                    vector = tweet[10].split(" ")
                    newVector = [0.0] * 8
                    for i in range(len(newVector)):
                        newVector[i] = float(vector[i])

                    for i in range(len(newVector)):
                        self.total_vector[i] += newVector[i]

                    cleanText = tweet[12].split(" ")
                    if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 7:
                        self.locateRepresentativeTweetsProcedure(tweet)

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
            allCharactersQuery = "SELECT * FROM littlebirds.tweet WHERE EpisodeID = " + str(self.requested_episode) + " AND (" \
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
            tweets = tupleToList(result)

            for tweet in tweets:

                self.tweets_counter += 1
                cleanText = tweet[12]

                self.summed_tweets_counter += 1

                vector = tweet[10].split(" ")
                newVector = [0.0] * 8
                for i in range(len(newVector)):
                    newVector[i] = float(vector[i])

                for i in range(len(newVector)):
                    self.total_vector[i] += newVector[i]

                cleanText = tweet[12].split(" ")
                if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 7:
                    self.locateRepresentativeTweetsProcedure(tweet)
                print(tweet[2])

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

                allNicksQuery = "SELECT * FROM littlebirds.tweet WHERE EpisodeID = " + str(self.requested_episode) + " AND (" \
                                              "CleanText like " + q + "%" + str(location) + "%" + q
                for nick in location_nicks:
                    allNicksQuery += " or CleanText like " + q + "%" + str(nick) + "%" + q
                # Close the right argument to 'AND'
                allNicksQuery += ")"

                result = DBconnect.DBconnect.send_query(allNicksQuery)
                tweets = tupleToList(result)

                for tweet in tweets:

                    self.tweets_counter += 1
                    cleanText = tweet[12]

                    self.summed_tweets_counter += 1

                    vector = tweet[10].split(" ")
                    newVector = [0.0] * 8
                    for i in range(len(newVector)):
                        newVector[i] = float(vector[i])

                    for i in range(len(newVector)):
                        self.total_vector[i] += newVector[i]

                    cleanText = tweet[12].split(" ")
                    if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 7:
                        self.locateRepresentativeTweetsProcedure(tweet)

            else:
                print("not in DB!")

        query_string = "SELECT OriginalText, UserName FROM tweet WHERE TweetID like "\
                       + q + str(self.representive_tweet_ID1) + q
        result = tupleToList(DBconnect.DBconnect.send_query(query_string))

        try:
            self.tweetText1 = result[0][0]
            self.author1 = result[0][1]
        except IndexError:
            self.tweetText1 = ""
            self.author1 = ""

        query_string = "SELECT OriginalText, UserName FROM tweet WHERE TweetID like " \
                       + q + str(self.representive_tweet_ID2) + q
        result = tupleToList(DBconnect.DBconnect.send_query(query_string))

        try:
            self.tweetText2 = result[0][0]
            self.author2 = result[0][1]
        except IndexError:
            self.tweetText2 = ""
            self.author2 = ""

        print("\n\nsummed tweets: " + str(self.summed_tweets_counter) + "\n\n")
        if self.summed_tweets_counter == 0:
            return None
        else:
            return [self.total_vector, self.tweetText1, self.author1, self.tweetText2, self.author2, self.summed_tweets_counter]


    def locateRepresentativeTweetsProcedure(self, tweet):
        self.distance_from_total = 0
        self.current_distance1 = 100
        self.current_distance2 = 100

        tweet_vector = tweet[10].split(" ")
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
        for i in range(len(tweet_vector)):
            tweet_vector[i] = float(tweet_vector[i])
            substitution_vector.append(abs(tweet_vector[i] - normalized_total_vector[i]))

        for value in substitution_vector:
            self.distance_from_total += value

        if (self.current_distance1 > self.distance_from_total):
            self.current_distance2 = self.current_distance1
            self.representive_tweet_ID2 = self.representive_tweet_ID1
            self.current_distance1 = self.distance_from_total
            self.representive_tweet_ID1 = tweet[2]
        elif (self.current_distance2 > self.distance_from_total):
            self.current_distance2 = self.distance_from_total
            self.representive_tweet_ID2 = tweet[2]
