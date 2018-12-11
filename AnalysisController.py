
import DBconnect
import Tweet
import Word
import Episode
import Script
import ScriptLine


class AnalysisController:

    summed_vector = [0] * 8     # Empty list with 8 zeroes

    sum_all_lines_emotions = 0

    analyzed_tweets_words_counter = 0
    analyzed_scriptlines_words_counter = 0
    lexicon = list()                # List of the words in the NRC lexicon and their emotional and sentimental values
    words_of_lexicon = list()       # List of the lexicon's words (without values)
    negation_words = list()         # List of words that negate words
    lexicon = list()            # List of the words in the NRC lexicon
                                # and their emotional and sentimental values
    words_of_lexicon = list()   # List of only the words in the NRC lexicon
                                # (no emotional or sentimental values)

    @staticmethod
    def analyze_tweets_by_episode():

        # Get the lexicon from the DB
        result = DBconnect.DBconnect.send_query("SELECT * FROM littlebirds.word;")
        for i in range(0, len(result)):
            AnalysisController.lexicon.append(list(result[i]))
            AnalysisController.words_of_lexicon.append((AnalysisController.lexicon[i])[0])

        # Get the negating words from the DB
        result = DBconnect.DBconnect.tuple_to_list \
            ("SELECT Expression FROM littlebirds.expression where expression.Discriminator = 2;")
        for i in range(0, len(result)):
            AnalysisController.negation_words.append((result[i])[0])

        # Get the episodes from the DB
        result = DBconnect.DBconnect.tuple_to_list\
            ("SELECT * FROM littlebirds.episode;")
        episodes = list()
        for episode in result:
            episodes.append(Episode.Episode(episode))

        # Get the tweets of each episode from the DB
        for episode in episodes:
            result = DBconnect.DBconnect.tuple_to_list\
                ("SELECT * FROM littlebirds.tweet WHERE littlebirds.tweet.EpisodeID = " + "1")


            # TODO: replace with:

            #result = DBconnect.DBconnect.tuple_to_list\
            # ("SELECT * FROM littlebirds.tweet WHERE littlebirds.tweet.EpisodeID = " + str(episodes.episodeID))

            # Analyze the tweets of each episode
            tweets_of_episode = list()
            tweets_index = 0
            for tweet in result:
                tweets_of_episode.insert(tweets_index, Tweet.Tweet(tweet))
                AnalysisController.analyze_tweet(tweets_of_episode[tweets_index], episode)
                tweets_index =+ 1

    # Analyzes a single tweet
    @staticmethod
    def analyze_tweet(tweet, episode):

        negation_flag = 0       # Signals if the former word was a negation word
        opposite_vec = list()   # Holds an vector with opposite values of emotions for negation

        # Initialize the tweet's emotions vector
        tweet.emotionsVec = list()
        for i in range(0, 8):
            tweet.emotionsVec.append(0)

        cleanTextList = list(tweet.cleanText.split())

        for word in cleanTextList:
            # Check if the word appear in the lexicon
            try:
                index_in_lexicon = AnalysisController.words_of_lexicon.index(word)
            except ValueError:
                # The word doesn't appear in the lexicon
                try:
                    # Check if the word is a negation word
                    AnalysisController.negation_words.index(word)
                    negation_flag = 1   # Signal for the next word that this word was negative
                    continue    # Continue to next word
                except ValueError:
                    # The word is not a negation word either
                    continue    # Skip to next word

            # Increment the counter: another word will be analyzed now
            AnalysisController.analyzed_tweets_words_counter += 1

            # Get the emotional and sentimental values of the word
            word_emotions = AnalysisController.lexicon[index_in_lexicon]

            if word_emotions[10] == 1 and word_emotions[9] == 0:
                # The word is positive and not-negative
                # Increment the tweet's emotions vector by 1, in the cells
                # of the positive/neutral emotions that the word has
                # positive: joy, anticipation, trust
                # neutral: surprise
                # (insert to 'i-1' because the tuple has the word in '0'
                if negation_flag == 0:
                    for i in range(5, 9):
                        if word_emotions[i] == 1:
                            tweet.emotionsVec[i-1] += 1

                # For each emotion that the negation of the word represents:
                # Increase the tweet's vector (for the negative emotions only)
                else:
                    if negation_flag == 1:
                        opposite_vec = AnalysisController.opposite_vector(word_emotions)
                        for i in range(1, 6):
                            if opposite_vec[i] == 1:
                                tweet.emotionsVec[i - 1] += 1

            else:
                if word_emotions[10] == 0 and word_emotions[9] == 1:
                    # The word is negative and not-positive
                    # Increment the tweet's emotions vector by 1, in the cells
                    # of the negative/neutral emotions that the word has
                    # negative: anger, disgust, fear, sadness
                    # neutral: surprise
                    # (insert to 'i-1' because the tuple has the word in '0'
                    if negation_flag == 0:
                        for i in range(1, 6):
                            if word_emotions[i] == 1:
                                tweet.emotionsVec[i-1] += 1

                    # For each emotion that the negation of the word represents:
                    # Increase the tweet's vector (for the negative emotions only)
                    else:
                        if negation_flag == 1:
                            opposite_vec = AnalysisController.opposite_vector(tweet.emotionsVec)
                            for i in range(4, 8):
                                if opposite_vec[i] == 1:
                                    tweet.emotionsVec[i] += 1

                else:
                    if (word_emotions[10] == 0 and word_emotions[9] == 0) or \
                       (word_emotions[10] == 1 and word_emotions[9] == 1):
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
                        # (if its not in the episode's list, then it obviously has no context yet)
                        try:
                            ambig_word_index = episode.ambiguousWordsList.index(word) # Get the word's index
                            episode.ambiguousWordsList_instancesCount[ambig_word_index] += 1 # Update counter
                        except ValueError:
                            episode.ambiguousWordsList.append(word)      # Add the word to the list
                            ambig_word_index = episode.ambiguousWordsList.index(word)  # Get the insertion index
                            episode.ambiguousWordsList_instancesCount.insert(ambig_word_index, 1)    # Initiate counter
                            continue

                        # If enough instances were collected, find the ambiguous-word's emotion
                        # with maximal value, and the ones that are close enough to it
                        if episode.ambiguousWordsList_instancesCount[ambig_word_index] >= \
                            0.01 * AnalysisController.analyzed_tweets_words_counter \
                            and AnalysisController.analyzed_tweets_words_counter > 3 \
                            and len(episode.ambiguousWordsList_emotionsVector) > ambig_word_index:
                            #try:
                            # Add if it already exists
                            #if len(episode.ambiguousWordsList_emotionsVector[ambig_word_index]) > 0:
                            maximal_emotion = max(episode.ambiguousWordsList_emotionsVector[ambig_word_index])
                            max_index = episode.ambiguousWordsList_emotionsVector[ambig_word_index].index(maximal_emotion)

                            # Initialize a list for emotions with close value to 'top_emotions'
                            top_emotions = list()
                            for i in range(0, 8):
                                top_emotions.append(0)

                            # Select the emotions with high values with a '1'
                            for i in range(0, 8):
                                if episode.ambiguousWordsList_emotionsVector[ambig_word_index][i] >= 0.9 * maximal_emotion:
                                    top_emotions[i] = 1

                            # Check if 'top_emotions' holds positive emotions
                            positive = 0
                            for i in range(0, 3):
                                if top_emotions[i] == 1:
                                    positive = 1

                            # Check if 'top_emotions' holds negative emotions
                            negative = 0
                            for i in range(4, 8):
                                if top_emotions[i] == 1:
                                    negative = 1

                            # The word is still ambiguous, skip to the next word
                            if positive == 1 and negative == 1:
                                continue

                            # If a context was collected, raise the values for each
                            # emotion in 'top_emotions'
                            if negation_flag == 1:
                                for i in range(0, 8):
                                    if top_emotions[i] == 1:
                                        tweet.emotionsVec[i] += 1

                            # For each emotion that the opposite of the word's top-emotions vector represents:
                            # Increase the tweet's vector (both for positive and negative emotions)
                            else:
                                if negation_flag == 1:
                                    opposite_vec = AnalysisController.opposite_vector(top_emotions)
                                    for i in range(0, 8):
                                        if opposite_vec[i] == 1:
                                            tweet.emotionsVec[i] += 1

                        #except IndexError:

                        #if episode.ambiguousWordsList_instancesCount[ambig_word_index] < 0.01 * AnalysisController.analyzed_tweets_words_counter:
                        # Not enough instances of this word yet to gather a context
                        else:
                            continue

        maximal_emotion = max(tweet.emotionsVec)
        emotionsVecAsString = ""

        # Not to divide by zero
        if maximal_emotion > 0:
            for i in range(0, 8):
                AnalysisController.sum_all_lines_emotions += tweet.emotionsVec[i]
                tweet.emotionsVec[i] = tweet.emotionsVec[i] / maximal_emotion
                tweet.emotionsVec[i] = round(tweet.emotionsVec[i], 3)
                emotionsVecAsString += str(tweet.emotionsVec[i]) + " "
            emotionsVecAsString = emotionsVecAsString[:-1]  # Lose last whitespace
        else:
            emotionsVecAsString = "0 0 0 0 0 0 0 0"

        # Update the vector in the tweet's DB tuple
        query = "UPDATE scriptline" \
                " SET EmotionsVec = " + "'" + emotionsVecAsString + "'" + \
                " WHERE LineID = " + str(tweet.tweetID) + ";"
        DBconnect.DBconnect.send_query(query)

        print(tweet.tweetID)

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
                episode.ambiguousWordsList_emotionsVector.insert(ambig_word_index, list())
                for i in range(0, 8):
                    episode.ambiguousWordsList_emotionsVector[ambig_word_index].append(tweet.emotionsVec[i])


    @staticmethod
    def analyze_scriptlines_by_script():

        # Get the lexicon from the DB
        result = DBconnect.DBconnect.send_query("SELECT * FROM littlebirds.word;")
        for i in range(0, len(result)):
            AnalysisController.lexicon.append(list(result[i]))
            AnalysisController.words_of_lexicon.append((AnalysisController.lexicon[i])[0])

        # Get the negating words from the DB
        result = DBconnect.DBconnect.tuple_to_list \
            ("SELECT Expression FROM littlebirds.expression where expression.Discriminator = 2;")
        for i in range(0, len(result)):
            AnalysisController.negation_words.append((result[i])[0])

        # Get the scripts from the DB
        result = DBconnect.DBconnect.tuple_to_list \
            ("SELECT * FROM littlebirds.script;")
        scripts = list()
        for script in result:
            scripts.append(Script.Script(script))

        # Get the tweets of each episode from the DB
        for script in scripts:
            # result = DBconnect.DBconnect.tuple_to_list \
            #     ("SELECT * FROM littlebirds.scriptline WHERE littlebirds.scriptline.ScriptID = " + "1")

            result = DBconnect.DBconnect.tuple_to_list\
            ("SELECT * FROM littlebirds.scriptline WHERE littlebirds.scriptline.ScriptID = " + str(script.scriptID))

            # Analyze the tweets of each episode
            scriptlines_of_script = list()
            scriptlines_index = 0
            for scriptline in result:
                scriptlines_of_script.insert(scriptlines_index, ScriptLine.ScriptLine(scriptline))
                AnalysisController.analyze_scriptline(scriptlines_of_script[scriptlines_index], script)
                scriptlines_index += 1
        #print("With amount of analyzed words:")
        print("With value of maximal emotion:")
        print(AnalysisController.summed_vector)

    # Analyzes a single script-line
    @staticmethod
    def analyze_scriptline(scriptline, script):

        negation_flag = 0  # Signals if the former word was a negation word
        opposite_vec = list()  # Holds an vector with opposite values of emotions for negation

        # Initialize the tweet's emotions vector
        scriptline.emotionsVec = list()
        for i in range(0, 8):
            scriptline.emotionsVec.append(0)

        cleanTextList = list(scriptline.cleanText.split())

        for word in cleanTextList:
            # Check if the word appear in the lexicon
            try:
                index_in_lexicon = AnalysisController.words_of_lexicon.index(word)
            except ValueError:
                # The word doesn't appear in the lexicon
                try:
                    # Check if the word is a negation word
                    AnalysisController.negation_words.index(word)
                    negation_flag = 1  # Signal for the next word that this word was negative
                    continue  # Continue to next word
                except ValueError:
                    # The word is not a negation word either
                    continue  # Skip to next word

            # Increment the counter: another word will be analyzed now
            AnalysisController.analyzed_scriptlines_words_counter += 1

            # Get the emotional and sentimental values of the word
            word_emotions = AnalysisController.lexicon[index_in_lexicon]

            if word_emotions[10] == 1 and word_emotions[9] == 0:
                # The word is positive and not-negative
                # Increment the tweet's emotions vector by 1, in the cells
                # of the positive/neutral emotions that the word has
                # positive: joy, anticipation, trust
                # neutral: surprise
                # (insert to 'i-1' because the tuple has the word in '0'
                if negation_flag == 0:
                    for i in range(4, 8):
                        if word_emotions[i+1] == 1:
                            scriptline.emotionsVec[i] += 1

                # For each emotion that the negation of the word represents:
                # Increase the tweet's vector (for the negative emotions only)
                else:
                    if negation_flag == 1:
                        opposite_vec = AnalysisController.opposite_vector(word_emotions)
                        for i in range(0, 5):
                            if opposite_vec[i+1] == 1:
                                scriptline.emotionsVec[i] += 1

            else:
                if word_emotions[10] == 0 and word_emotions[9] == 1:
                    # The word is negative and not-positive
                    # Increment the tweet's emotions vector by 1, in the cells
                    # of the negative/neutral emotions that the word has
                    # negative: anger, disgust, fear, sadness
                    # neutral: surprise
                    # (insert to 'i-1' because the tuple has the word in '0'
                    if negation_flag == 0:
                        for i in range(0, 5):
                            if word_emotions[i+1] == 1:
                                scriptline.emotionsVec[i] += 1

                    # For each emotion that the negation of the word represents:
                    # Increase the tweet's vector (for the negative emotions only)
                    else:
                        if negation_flag == 1:
                            opposite_vec = AnalysisController.opposite_vector(scriptline.emotionsVec)
                            for i in range(4, 8):
                                if opposite_vec[i] == 1:
                                    scriptline.emotionsVec[i] += 1

                else:
                    if (word_emotions[10] == 0 and word_emotions[9] == 0) or \
                            (word_emotions[10] == 1 and word_emotions[9] == 1):
                        # The word is either not-negative and not-positive or
                        # both negative and positive
                        # Infer the emotional tendency of the word by the context of the
                        # other tweets it appears in, which refer to the same episode

                        # Look for the word in the tweet's ambiguous words list
                        # Insert if not there already
                        # These list will help modify the context for the episode's
                        # ambiguous words list
                        try:
                            ambig_word_index = scriptline.ambiguousWordsList.index(word)
                        except ValueError:
                            scriptline.ambiguousWordsList.append(word)  # Add the word to the list

                        # Look for the word in the episode's ambiguous words list
                        # Insert if not there, and continue to check the next word
                        # (if its not in the episode's list, then it obviously has no context yet)
                        try:
                            ambig_word_index = script.ambiguousWordsList.index(word)  # Get the word's index
                            script.ambiguousWordsList_instancesCount[ambig_word_index] += 1  # Update counter
                        except ValueError:
                            script.ambiguousWordsList.append(word)  # Add the word to the list
                            ambig_word_index = script.ambiguousWordsList.index(word)  # Get the insertion index
                            script.ambiguousWordsList_instancesCount.insert(ambig_word_index, 1)  # Initiate counter
                            continue

                        # If enough instances were collected, find the ambiguous-word's emotion
                        # with maximal value, and the ones that are close enough to it
                        if script.ambiguousWordsList_instancesCount[ambig_word_index] >= \
                                0.01 * AnalysisController.analyzed_scriptlines_words_counter \
                                and AnalysisController.analyzed_scriptlines_words_counter > 3\
                                and len(script.ambiguousWordsList_emotionsVector)>ambig_word_index:
                            # try:
                            # Add if it already exists
                            # if len(script.ambiguousWordsList_emotionsVector[ambig_word_index]) > 0:
                            maximal_emotion = max(script.ambiguousWordsList_emotionsVector[ambig_word_index])
                            max_index = script.ambiguousWordsList_emotionsVector[ambig_word_index].index(
                                maximal_emotion)

                            # Initialize a list for emotions with close value to 'top_emotions'
                            top_emotions = list()
                            for i in range(0, 8):
                                top_emotions.append(0)

                            # Select the emotions with high values with a '1'
                            for i in range(0, 8):
                                if script.ambiguousWordsList_emotionsVector[ambig_word_index][i] >= 0.9 * maximal_emotion:
                                    top_emotions[i] = 1

                            # Check if 'top_emotions' holds positive emotions
                            positive = 0
                            for i in range(0, 3):
                                if top_emotions[i] == 1:
                                    positive = 1

                            # Check if 'top_emotions' holds negative emotions
                            negative = 0
                            for i in range(4, 8):
                                if top_emotions[i] == 1:
                                    negative = 1

                            # The word is still ambiguous, skip to the next word
                            if positive == 1 and negative == 1:
                                continue

                            # If a context was collected, raise the values for each
                            # emotion in 'top_emotions'
                            if negation_flag == 1:
                                for i in range(0, 8):
                                    if top_emotions[i] == 1:
                                        scriptline.emotionsVec[i] += 1

                            # For each emotion that the opposite of the word's top-emotions vector represents:
                            # Increase the tweet's vector (both for positive and negative emotions)
                            else:
                                if negation_flag == 1:
                                    opposite_vec = AnalysisController.opposite_vector(top_emotions)
                                    for i in range(0, 8):
                                        if opposite_vec[i] == 1:
                                            scriptline.emotionsVec[i] += 1

                        # except IndexError:

                        # if episode.ambiguousWordsList_instancesCount[ambig_word_index] < 0.01 * AnalysisController.analyzed_tweets_words_counter:
                        # Not enough instances of this word yet to gather a context
                        else:
                            continue

        # Normalize the script-lines' emotions vector and save it as string (to save in DB)
        maximal_emotion = max(scriptline.emotionsVec)
        emotionsVecAsString = ""
        scriptline.wordsCounter = len(cleanTextList)

        # Not to divide by zero
        if maximal_emotion > 0:
            for i in range(0, 8):
                AnalysisController.sum_all_lines_emotions += scriptline.emotionsVec[i]

                # The right way to normalize:
                scriptline.emotionsVec[i] = scriptline.emotionsVec[i] / maximal_emotion

                # Some shallow, small-minded, unnecessary  way to do some useless stuff with numbers:
                #scriptline.emotionsVec[i] = scriptline.emotionsVec[i] / scriptline.wordsCounter

                scriptline.emotionsVec[i] = round(scriptline.emotionsVec[i],3)
                AnalysisController.summed_vector[i] += scriptline.emotionsVec[i]
                emotionsVecAsString += str(scriptline.emotionsVec[i]) + " "
            emotionsVecAsString = emotionsVecAsString[:-1]  # Lose last whitespace
        else:
            emotionsVecAsString = "0 0 0 0 0 0 0 0"


        # Update the vector in the tweet's DB tuple
        query = "UPDATE scriptline" \
                " SET EmotionsVec = " + "'" + emotionsVecAsString + "'" + \
                " WHERE LineID = " + str(scriptline.lineID) + ";"
        DBconnect.DBconnect.send_query(query)

        print(scriptline.lineID)

        # Increase the values of the episode's ambiguous words vectors
        # with the ambiguous words that appeared in the tweet, to update
        # the episode's context
        for word in scriptline.ambiguousWordsList:
            ambig_word_index = script.ambiguousWordsList.index(word)
            try:
                # Add if it already exists
                if len(script.ambiguousWordsList_emotionsVector[ambig_word_index]) > 0:
                    for i in range(0, 8):
                        script.ambiguousWordsList_emotionsVector[ambig_word_index][i] += scriptline.emotionsVec[i]

            except IndexError:
                # Initialize if the list is empty
                script.ambiguousWordsList_emotionsVector.insert(ambig_word_index, list())
                for i in range(0, 8):
                    script.ambiguousWordsList_emotionsVector[ambig_word_index].append(scriptline.emotionsVec[i])

        #print(AnalysisController.sum_all_lines_emotions)   # Total amount of  meaningful words in the scriptlines

    @staticmethod
    def opposite_vector(original_vec):
        opposite_vec = list()
        # Switch the values of each opposite couple of emotions
        # if both are '0' or '1' -> stats the same
        # if one is '1' and the other is '0' -> switched

        # Tweet's emotions vector
        if len(original_vec) == 11:
            opposite_vec.insert(0, original_vec[0])      # Insert word
            opposite_vec.insert(1, original_vec[3])      # anger <- fear
            opposite_vec.insert(2, original_vec[8])      # disgust <- trust
            opposite_vec.insert(3, original_vec[1])      # fear <- anger
            opposite_vec.insert(4, original_vec[6])      # sadness <- joy
            opposite_vec.insert(5, original_vec[7])      # surprise <- anticipation
            opposite_vec.insert(6, original_vec[4])      # joy <- sadness
            opposite_vec.insert(7, original_vec[5])      # anticipation <- surprise
            opposite_vec.insert(8, original_vec[2])      # trust <- disgust
            opposite_vec.insert(9, original_vec[10])     # negative <- positive
            opposite_vec.insert(10, original_vec[9])     # positive <- negative

        # Script-line's emotions vector
        elif len(original_vec) == 8:
            opposite_vec.insert(0, original_vec[2])  # anger <- fear
            opposite_vec.insert(1, original_vec[7])  # disgust <- trust
            opposite_vec.insert(2, original_vec[0])  # fear <- anger
            opposite_vec.insert(3, original_vec[5])  # sadness <- joy
            opposite_vec.insert(4, original_vec[6])  # surprise <- anticipation
            opposite_vec.insert(5, original_vec[3])  # joy <- sadness
            opposite_vec.insert(6, original_vec[4])  # anticipation <- surprise
            opposite_vec.insert(7, original_vec[1])  # trust <- disgust

        return opposite_vec
