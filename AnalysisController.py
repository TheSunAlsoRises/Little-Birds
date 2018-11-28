
import DBconnect
import Tweet
import Word
import Episode


class AnalysisController:

    #TODO treat words with negation before them


    analyzed_words_counter = 0
    lexicon = list()                # List of the words in the NRC lexicon and their emotional and sentimental values
    words_of_lexicon = list()       # List of the lexicon's words (without values)
    negation_words = list()         # List of words that negate words

    # Get the lexicon from the DB
    result = DBconnect.DBconnect.send_query("SELECT * FROM littlebirds.word;")
    for i in range(0, len(result)):
        lexicon.append(list(result[i]))
        words_of_lexicon.append((lexicon[i])[0])

    # Get the negating words from the DB
    result = DBconnect.DBconnect.tuple_to_list("SELECT Expression FROM littlebirds.expression where expression.Discriminator = 2;")
    for i in range(0, len(result)):
        negation_words.append((result[i])[0])


    @staticmethod
    def analyze_tweets_by_episode():

        # Get the episodes from the DB
        result = DBconnect.DBconnect.tuple_to_list("SELECT * FROM littlebirds.episode;")
        episodes = list()
        for episode in result:
            episodes.append(Episode.Episode(episode))

        # Get the tweets of each episode from the DB
        for episode in episodes:
            result = DBconnect.DBconnect.tuple_to_list("SELECT * FROM littlebirds.tweet WHERE littlebirds.tweet.EpisodeID = " + "1")
            # TODO: replace with:
            #tweets_of_episode = DBconnect.DBconnect.tuple_to_list("SELECT * FROM littlebirds.tweet WHERE littlebirds.tweet.EpisodeID = " + str(episodes.episodeID))

            # Analyze the tweets of each episode
            tweets_of_episode = list()
            tweets_index = 0
            for tweet in result:
                tweets_of_episode.insert(tweets_index,Tweet.Tweet(tweet))
                AnalysisController.analyze_tweet(tweets_of_episode[tweets_index],episode)
                tweets_index =+ 1



    # Analyzes a single tweet
    @staticmethod
    def analyze_tweet(tweet, episode):

        # Initialize the tweet's emotions vector
        tweet.emotionsVec = list()
        for i in range(0, 8):
            tweet.emotionsVec.append(0)

        for word in tweet.cleanText:
            try:
                index_in_lexicon = AnalysisController.words_of_lexicon.index(word)
            except ValueError:
                # The word doesn't appear in the lexicon
                continue  # Skip to next word

            # Increment the counter: another word will be analyzed now
            ### AnalysisController.analyzed_words_counter += 1

            # Get the emotional and sentimental values of the word
            word_emotions = AnalysisController.lexicon[index_in_lexicon]

            if word_emotions[10] == 1 and word_emotions[9] == 0:
                # The word is positive and not-negative
                # Increment the tweet's emotions vector by 1, in the cells
                # of the positive/neutral emotions that the word has
                # positive: joy, anticipation, trust
                # neutral: surprise
                # (insert to 'i-1' because the tuple has the word in '0'
                for i in range(5,9):
                    if word_emotions[i] == 1:
                        tweet.emotionsVec[i-1] += 1

            else:
                if word_emotions[10] == 0 and word_emotions[9] == 1:
                    # The word is negative and not-positive
                    # Increment the tweet's emotions vector by 1, in the cells
                    # of the negative/neutral emotions that the word has
                    # negative: anger, disgust, fear, sadness
                    # neutral: surprise
                    # (insert to 'i-1' because the tuple has the word in '0'
                    for i in range(1,6):
                        if word_emotions[i] == 1:
                            tweet.emotionsVec[i-1] += 1

                else:
                    if (word_emotions[10] == 0 and word_emotions[9] == 0) or (word_emotions[10] == 1 and word_emotions[9] == 1):
                        # The word is either not-negative and not-positive or
                        # both negative and positive
                        # Infer the emotional tendency of the word by the context of the
                        # other tweets it appears in, which refer to the same episode

                        # Look for the word in the tweet's ambiguous words list
                        # Insert if not there already
                        # These list will help modify the context for the episode's
                        # ambiguous words list
                        try:
                            ambig_word_index = tweet.ambiguousWordsList.index(word)
                        except ValueError:
                            tweet.ambiguousWordsList.append(word) # Add the word to the list

                        # Look for the word in the episode's ambiguous words list
                        # Insert if not there, and continue to check the next word
                        # (if its not in the episode's list, then it has no context yet)
                        try:
                            ambig_word_index = episode.ambiguousWordsList.index(word) # Get the word's index
                            episode.ambiguousWordsList_instancesCount[ambig_word_index] += 1 # Update counter
                        except ValueError:
                            episode.ambiguousWordsList.append(word) # Add the word to the list
                            ambig_word_index = episode.ambiguousWordsList.index(word)  # Get the insertion index
                            episode.ambiguousWordsList_instancesCount.insert(ambig_word_index,1)    # Initiate counter
                            continue

                        # If enough instances were collected, find the ambiguous-word's emotion
                        # with maximal value, and the ones that are close enough to it
                        #if episode.ambiguousWordsList_instancesCount[ambig_word_index] >= 0.01 * AnalysisController.analyzed_words_counter:
                        #if len(episode.ambiguousWordsList_emotionsVector) > 0:
                        try:
                            # Add if it already exists
                            if len(episode.ambiguousWordsList_emotionsVector[ambig_word_index]) > 0:
                                maximal_emotion = max(episode.ambiguousWordsList_emotionsVector[ambig_word_index])
                                max_index = episode.ambiguousWordsList_emotionsVector[ambig_word_index].index(maximal_emotion)

                                # Initialize a list for emotions with close value to 'top_emotions'
                                top_emotions = list()
                                for i in range(0,8):
                                    top_emotions.append(0)

                                # Select the emotions with high values with a '1'
                                for i in range(0,8):
                                    if episode.ambiguousWordsList[ambig_word_index][i] >= 0.9 * maximal_emotion:
                                        top_emotions[i] = 1

                                # Check if 'top_emotions' holds positive emotions
                                positive = 0
                                for i in range(0,3):
                                    if top_emotions[i] == 1:
                                        positive = 1

                                # Check if 'top_emotions' holds negative emotions
                                negative = 0
                                for i in range(4, 8):
                                    if top_emotions[i] == 1:
                                        negative = 1

                                # The word is still ambigous, continue to analyse word
                                if positive == 1 and negative == 1:
                                    continue

                                # If a context was collected, raise the values for each
                                # emotion in 'top_emotions'
                                for i in range(0,8):
                                    if top_emotions[i] == 1:
                                        tweet.emotionsVec[i] += 1

                        except IndexError:
                            #if episode.ambiguousWordsList_instancesCount[ambig_word_index] < 0.01 * AnalysisController.analyzed_words_counter:
                            #if len(episode.ambiguousWordsList_emotionsVector) == 0:
                            # Not enough instances of this word yet to gather a context
                            continue

        # Normalize the tweet's emotions vector
        maximal_emotion = max(tweet.emotionsVec)
        for i in range(0,8):
            tweet.emotionsVec[i] = tweet.emotionsVec[i] / maximal_emotion

        # Increase the values of the episode's ambiguous words vectors
        # with the ambiguous words that appeared in the tweet, to update
        # the episode's context
        for word in tweet.ambiguousWordsList:
            ambig_word_index = episode.ambiguousWordsList.index(word)
            try:
                # Add if it already exists
                if len(episode.ambiguousWordsList_emotionsVector[ambig_word_index]) > 0:
                    for i in range(0, 8):
                        episode.ambiguousWordsList_emotionsVector[ambig_word_index][i] += tweet.emotionsVec[i]

            except IndexError:
                # Initialize if the list is empty
                episode.ambiguousWordsList_emotionsVector.insert(ambig_word_index,list())
                for i in range(0, 8):
                    episode.ambiguousWordsList_emotionsVector[ambig_word_index].append(tweet.emotionsVec[i])