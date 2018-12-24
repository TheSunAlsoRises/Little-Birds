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
        query_string = "SELECT * FROM tweet WHERE EpisodeID=" + self.requested_episode
        result = DBconnect.DBconnect.send_query(query_string)
        tweets = tupleToList(result)

        stop = 0
        if (self.category == "character"):
            for tweet in tweets:
                self.tweets_counter+=1

                #COLLECT ALL CHARACTER NICK NAMES
                character_nicks = ()
                query_string = "SELECT Nick FROM nick where SubID = " \
                               "(select SubID from nick where Nick = " + '"' + self.selected + '")';
                result = DBconnect.DBconnect.send_query(query_string)
                character_nicks = tupleToList(result)
                cleanText = tweet[12].split(" ")

                for nick in character_nicks:
                    if nick in tweet[12]:
                        self.total_vector += tweet[10]
                        if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                            #locateRepresentativetweetsprocedure()
                        break



        elif (self.category == "house"):
            for tweet in tweets:
                self.tweets_counter+=1

                #COLLECT ALL HOUSE NICK NAMES
                house_nicks = ()
                query_string = "SELECT Nick FROM nick where SubID = " \
                               "(select SubID from nick where Nick = " + '"' + self.selected + '")';
                result = DBconnect.DBconnect.send_query(query_string)
                house_nicks = tupleToList(result)

                #COLLECT ALL CHARATERS FROM SPECIFIC HOUSE
                characters_house = ()
                query_string = "SELECT CharacterName FROM category where HouseName like '%"+ self.selected
                +"%' and CharacterName is not null";
                result = DBconnect.DBconnect.send_query(query_string)
                characters_house = tupleToList(result)

                cleanText = tweet[12].split(" ")

                for nick in house_nicks:
                    if nick in tweet[12]:
                        self.total_vector += tweet[10]
                        if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                            #locateRepresentativetweetsprocedure()
                        stop = 1
                        break
                if stop == 0:
                    for character in characters_house:
                        character_nicks = ()
                        query_string = "SELECT Nick FROM nick where SubID = " \
                                       "(select SubID from nick where Nick = " + '"' + character + '")';
                        result = DBconnect.DBconnect.send_query(query_string)
                        character_nicks = tupleToList(result)
                        for nick in character_nicks:
                            if nick in tweet[12]:
                                self.total_vector += tweet[10]
                                if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                                    # locateRepresentativetweetsprocedure()
                                break

                else: stop = 0;


        elif (self.category == "location"):
            for tweet in tweets:
                self.tweets_counter+=1

                #COLLECT ALL LOCATION NICK NAMES
                location_nicks = ()
                query_string = "SELECT Nick FROM nick where SubID = " \
                               "(select SubID from nick where Nick = " + '"' + self.selected + '")';
                result = DBconnect.DBconnect.send_query(query_string)
                location_nicks = tupleToList(result)
                cleanText = tweet[12].split(" ")

                for nick in location_nicks:
                    if nick in tweet[12]:
                        self.total_vector += tweet[10]
                        if self.tweets_counter > 0.9 * self.total_tweets and len(cleanText) > 5:
                            #locateRepresentativetweetsprocedure()
                        break

        return self.total_vector








