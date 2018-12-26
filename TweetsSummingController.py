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
            for tweet in tweets:
                self.tweets_counter+=1

                #COLLECT ALL CHARACTER NICK NAMES
                character_nicks = ()
                q = '"'
                query_string = "SELECT Nick FROM nick where SubID = " \
                               "(select SubID from nick where Nick = " + q + self.selected + q + ")";
                result = DBconnect.DBconnect.send_query(query_string)
                character_nicks = tupleToList(result)

                nicks = []
                for i in character_nicks:
                    tmp = i
                    tmp = ''.join(tmp)
                    nicks.append(tmp)
                character_nicks = nicks

                cleanText = tweet[12].split(" ")

                for nick in character_nicks:
                    if nick in tweet[12]:
                        self.total_vector += tweet[10]
                        #if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                            #locateRepresentativetweetsprocedure()
                        break



        elif (self.category == "house"):
            for tweet in tweets:
                self.tweets_counter+=1

                #COLLECT ALL CHARATERS FROM SPECIFIC HOUSE
                characters_house = []

                q = '"'
                query_string = "SELECT CharacterName FROM category where HouseName like " + q + "%" + str(self.selected) + "%" + q \
                               + " and CharacterName is not null";
                result = DBconnect.DBconnect.send_query(query_string)
                characters_house = tupleToList(result)

                characters = []
                for i in characters_house:
                    tmp = i
                    tmp = ''.join(tmp)
                    characters.append(tmp)
                characters_house = characters

                cleanText = tweet[12].split(" ")
                house = self.selected
                if house in tweet[12]:
                    self.total_vector += tweet[10]
                    #if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                        #locateRepresentativetweetsprocedure()
                    stop = 1
                    break
                if stop == 0:
                    for character in characters_house:
                        character_nicks = ()
                        q = '"'
                        query_string = "SELECT Nick FROM nick where SubID = " \
                                       "(select SubID from nick where Nick like " + q + "%" + str(character) + "%" + q + ")";
                        result = DBconnect.DBconnect.send_query(query_string)
                        character_nicks = tupleToList(result)

                        nicks = []
                        for i in character_nicks:
                            tmp = i
                            tmp = ''.join(tmp)
                            nicks.append(tmp)
                        character_nicks = nicks

                        for nick in character_nicks:
                            if nick in tweet[12]:
                                self.total_vector += tweet[10]
                                #if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                                    # locateRepresentativetweetsprocedure()
                                break

                else: stop = 0;


        elif (self.category == "location"):
            for tweet in tweets:
                self.tweets_counter+=1

                #COLLECT ALL LOCATION NICK NAMES
                #location_nicks = ()
                #q = '"'
                #query_string = "SELECT Nick FROM nick where SubID = " \
                #               "(select SubID from nick where Nick = " + q + str(self.selected) + q + ")";
                #result = DBconnect.DBconnect.send_query(query_string)
                #location_nicks = tupleToList(result)

                cleanText = tweet[12].split(" ")
                location = self.selected

                #for nick in location_nicks:
                #    if nick in tweet[12]:
                if location in tweet[12]:
                    self.total_vector += tweet[10]
                        #if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                            #locateRepresentativetweetsprocedure()
                        #break

        return self.total_vector



def locateRepresentativetweetsprocedure():
    maximal_value = 0
    normalized_total_vector = [] * 8
    distance_from_total = 0
    current_distance1 = 100
    current_distance2 = 100

    representive_tweet1 = ""
    representive_tweet2 = ""








