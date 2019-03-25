import pandas as pd
import DBconnect
import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

#CONVERT TUPLE TO LIST FUNCTION
def tupleToList(t):
    emptyList = list()
    for i in range(0,len(t)):
        emptyList.append(list(t[i]))
    return emptyList

def Preprocessing_data(set_of_tweets):

    # Not enough data
    if len(set_of_tweets) < 500:
        return None
    # Too much data, take only the first 7000
    if len(set_of_tweets)> 1000:
        set_of_tweets = set_of_tweets[:1000]

    #Create dictionary
    emotions = ["Anger", "Disgust", "Fear", "Sadness", "Surprise", "Joy", "Anticipation", "Trust"]
    for e in emotions:
        query_string = "SELECT Word FROM word WHERE " + e + ">0"
        words = DBconnect.DBconnect.send_query(query_string)
        dict = ["tweet_text"]

        for word in words:
            word = ''.join(word)
            dict.append(word)
        dict.append("emotion_value")

        with open(e+'.csv','w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(dict)

        #Collect all CleanText of tweet
        #query_string = "SELECT CleanText,EmotionsVec FROM tweet limit 0,1000;"
        #result = DBconnect.DBconnect.send_query(query_string)
        #tweets = tupleToList(result)

        for tweet in set_of_tweets:
            text = tweet[12]
            emotion_vector = tweet[10].split(" ")
            tweet_array = [0]*len(dict)
            tweet_array[0] = text

            emotion_value= emotion_vector[emotions.index(e)]
            tweet_array[len(dict)-1]=emotion_value

            words = text.split(" ")
            for word in words:
                try:
                    index_of_word =dict.index (word)
                    tweet_array[index_of_word]+=1
                except:
                    pass

            with open(e+'.csv', 'a') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(tweet_array)
    return 1

def Linear_reggression():
    emotions = ["Anger", "Disgust", "Fear", "Sadness", "Surprise", "Joy", "Anticipation", "Trust"]
    results = []

    for e in emotions:
        print("\nEmotion :", e)
        dataset = pd.read_csv(e+'.csv')
        datasetsize = dataset.shape

        best_t = 1
        best_error = 11111111111111111111111111111
        for T in range(2,10):
            names = []
            for i in range(1, datasetsize[1]-1):  # all col without first and last
                r = dataset.iloc[0:, i].values
                name = dataset.columns[i]
                if sum(r)<T:
                    names.append(name)
            # dropping passed columns
            dataset.drop(names, axis=1, inplace=True)

            datasetsize = dataset.shape

            # Split to input and lable
            x = dataset.iloc[:, 1:-1].values
            y = dataset.iloc[:, datasetsize[1]-1].values

            # Split the dataset into the Training set and Test set
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

            # Fitting Multiple Linear Regression to the Training set
            regressor = LinearRegression()
            regressor.fit(x_train, y_train)

            # Predicting the Test set result
            y_pred = regressor.predict(x_test)
            #print('Coefficients: \n', regressor.coef_)
            print("T : ",T)
            # The mean squared error
            x = mean_squared_error(y_test, y_pred)
            print("Mean squared error: %.4f" %x)
            if(x<best_error):
                best_t = T
                best_error = x

        print("Best t: " + str(best_t))
        #print("The value of y_pred for emotion " + e + " is:" + str(sum(y_pred)/len(y_pred)))
        print("The sum of y_pred for emotion " + e + " is:" + str(sum(y_pred)))
        #print("The value of y_test for emotion " + e + " is:" + str(sum(y_test)/len(y_test)))
        print("The sum of y_test for emotion " + e + " is:" + str(sum(y_test)))
        #results.append(sum(y_pred)/len(y_pred))
        results.append(sum(y_pred))

    return results

def prediction(set_of_tweets):
    if Preprocessing_data(set_of_tweets) == None:
        return  None
    x =  Linear_reggression()
    if len(set_of_tweets) > 1000:
        x.append(1000)
    elif len(set_of_tweets) < 500:
        x.append(0)
    else:
        x.append(len(set_of_tweets))
    return x
