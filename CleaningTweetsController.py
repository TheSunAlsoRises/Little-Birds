import Tweet
import Episode
import datetime

class CleaningTweetsController:
   episodes = list()
    #CALL DB TO ADD EPISODES TO THE VAR

   for episode in episodes:
        date = episode.date.split("/")
        episode.date = datetime.datetime(date[2], date[1], date[0])


def SetEpisodeID(tweet):

    date = tweet.date.split("/")
    tweet.date = datetime.datetime(date[2], date[1], date[0])

    for i in range(0,8):
        if tweet.date <= CleaningTweetsController.episodes[0]:
            tweet.episodeID = CleaningTweetsController.episodes[0]

        elif tweet.date > CleaningTweetsController.episodes[7]:
            tweet.episodeID = CleaningTweetsController.episodes[7]

        elif tweet.date <= CleaningTweetsController.episodes[i]:
            tweet.episodeID = CleaningTweetsController.episodes[i-1]
