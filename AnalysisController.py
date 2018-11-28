
import DBconnect
import Tweet
import Word

class AnalysisController:

    analyzed_words_counter = 0

    lexicon = list()            # List of the words in the NRC lexicon
                                # and their emotional and sentimental values
    words_of_lexicon = list()   # List of only the words in the NRC lexicon
                                # (no emotional or sentimental values)

    def analyze_tweet(self, tweet, episode):

        # Initialize the tweet's emotions vector
        tweet.emotionsVec = list(8)
        for i in tweet.emotionsVec:
            tweet.emotionsVec[i] = 0

        for word in tweet.cleanText:
            try:
                index_in_lexicon = self.words_of_lexicon.index(word)
            except ValueError:
                # The word doesn't appear in the lexicon
                continue  # Skip to next word

            # Increment the counter: another word will be analyzed now
            self.analyzed_words_counter += 1

            # Get the emotional and sentimental values of the word
            word_emotions = self.lexicon[index_in_lexicon]

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
                    if ((word_emotions[10] == 0 and word_emotions[9] == 0)
                        or (word_emotions[10] == 1 and word_emotions[9] == 1)):
                        # The word is either not-negative and not-positive or
                        # both negative and positive
                        # Infer the emotional tendency of the word by the context of the
                        # other tweets it appears in, which refer to the same episode

# Perhaps switch the following paragraph with the next one:

                        # Look for the word in the tweet's ambiguous words list
                        # Insert if not there
                        try:
                            i = tweet.ambiguousWordsList.index(word)
                        except ValueError:
                            tweet.ambiguousWwordsList.insert(word) # Add the word to the list


                        # Look for the word in the episode's ambiguous words list
                        # Insert if not there, and continue to check the next word
                        # (if its not in the episode's list, then it has no context yet)
                        try:
                            i = episode.ambiguousWordsList.index(word) # Get the word's index
                            episode.ambiguousWordsList_instancesCount[i] += 1 # Update counter
                        except ValueError:
                            tweet.ambiguousWordsList.insert(word) # Add the word to the list
                            try:
                                i = episode.ambiguousWordsList.index(word)  # Get the insertion index
                                episode.ambiguousWordsList_instancesCount[i] = 0    # Initiate counter
                                continue
                            except ValueError:
                                print("failed to insert", word, " to ", episode)
                                continue