from nltk.stem import WordNetLemmatizer
import DBconnect
import string
import re
from datetime import datetime


# CONVERT TUPLE TO LIST FUNCTION
def tupleToList(t):
    emptyList = list()
    for i in range(0, len(t)):
        emptyList.append(list(t[i]))
    return emptyList

nicks = list()
query_string = "SELECT Nick FROM nick"
result = DBconnect.DBconnect.send_query(query_string)
result = tupleToList(result)


for i in result:
    tmp = i
    tmp = ''.join(tmp)
    nicks.append(tmp)

result = nicks
nicks = ""

for i in result:
    tmp = i
    tmp = ''.join(tmp)
    nicks = nicks + tmp + "   "


episodesDate = list()
query_string = "SELECT episode.BroadcastingDate FROM episode"
result = DBconnect.DBconnect.send_query(query_string)

result = tupleToList(result)

for i in result:
    tmp = i
    tmp = ''.join(tmp)
    episodesDate.append(tmp)


# SAVE DATES AS A DATETIME TYPE IN ORDER TO COMPARE WITH TWO DATES
dates = list()
for date in episodesDate:
    newDate = datetime.strptime(date, '%d/%m/%y')
    dates.append(newDate)

tweets = list()
query_string = "SELECT * FROM tweet WHERE Date like '16%'"
result = DBconnect.DBconnect.send_query(query_string)
result = tupleToList(result)

for i in result:
    tweet = i
    date = tweet[0]
    date = date.split("/")
    newDate = datetime(int(date[2]), int(date[1]), int(date[0]))
    tweet[0] = newDate

    for j in range(0, len(dates)):
        if tweet[0] <= dates[0]:
            tweet[8] = 1
            break
        elif tweet[0] >= dates[6]:
            tweet[8] = 7
            break
        elif tweet[0] < dates[j]:
            tweet[8] = j
            break

    tweets.append(tweet)

query_string = "SELECT expression.Expression FROM expression where Discriminator=1"
result = DBconnect.DBconnect.send_query(query_string)
result = tupleToList(result)

foreign_words = list()
for i in result:
    tmp = i
    tmp = ''.join(tmp)
    foreign_words.append(tmp)

lemmatiser = WordNetLemmatizer()

for tweet in tweets:
    tweet[9] = list()
    txt = tweet[6]
    foreign_words_counter = 0
    delete_flag = 0

    txt = txt.split(" ")
    for word in txt:
        word = word.lower()

        # REMOVE PUNCTUATION
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        word= regex.sub('', word)

        while (len(word) > 0):
            if word.find("ud8") == -1 and word.find("u27") == -1:
                if word in foreign_words:
                    foreign_words_counter += 1

                    #IF FORIEGN WORDS COUNTER BIGGER THAN 2 WE DELETE THE TWEET
                    if foreign_words_counter >=2:
                        q = '"'
                        id = tweet[2]
                        print(id)
                        query_string = "DELETE FROM tweet where TweetID="+ q+id+q
                        DBconnect.DBconnect.send_query(query_string)
                        delete_flag = 1
                        break

                if word not in nicks:
                    word = lemmatiser.lemmatize(word,pos="v")
                tweet[9].append(word)
                word = ""
            else:
                index = word.find("ud8")
                if index == -1:
                    index = word.find("u27")
                    cnt = word.count("u27")
                else:
                    cnt = word.count("ud8")

                if index != 0:
                    left = word[0:index]
                    emoji = word[index:index + 10]
                    tweet[9].append(left)
                    tweet[9].append(emoji)
                    word = word.replace(left + emoji, "" + "")

                else:
                    emoji = word[index:index + 10]
                    for i in range(0, cnt):
                        tweet[9].append(emoji)
                    word = word.replace(emoji, "" + "")

        if delete_flag==1:
            delete_flag=0
            foreign_words_counter = 0
            tweet[9]=list()
            break

    str = ""
    # CONVERT THE LIST OF THE CLEANING WORDS TO STRING AND INSERT TO DB
    for i in tweet[9]:
        tmp = i
        tmp = ''.join(tmp)
        str = str + tmp + " "


    q = '"'
    id = tweet[2]
    query_string = "update tweet set CleanText = " + q + str + q + "where TweetID = " + q + id + q
    DBconnect.DBconnect.send_query(query_string)