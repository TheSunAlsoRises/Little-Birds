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

def Preprocessing_data():
    #Create dictionary
    query_string = "SELECT Word FROM word"
    words = DBconnect.DBconnect.send_query(query_string)
    dict = ["tweet_text"]

    for word in words:
        word = ''.join(word)
        dict.append(word)
    dict.append("emotion_value")

    with open('table1.csv','w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(dict)

    #Collect all CleanText of tweet
    query_string = "SELECT CleanText,EmotionsVec FROM tweet limit 0,10000;"
    result = DBconnect.DBconnect.send_query(query_string)
    tweets = tupleToList(result)

    for tweet in tweets:
        text = tweet[0]
        emotion_vector = tweet[1].split(" ")
        tweet_array = [0]*len(dict)
        tweet_array[0] = text

        emotion_value=0
        for i in range(8):
            x = float(emotion_vector[i])
            emotion_value += x * float(2**(7-i))
        tweet_array[len(dict)-1]=emotion_value/255

        words = text.split(" ")
        for word in words:
            try:
                index_of_word =dict.index (word)
                tweet_array[index_of_word]+=1
            except:
                pass

        with open('table1.csv', 'a') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(tweet_array)


def Linear_reggression(T):
    dataset = pd.read_csv('table1.csv')

    names = []
    for i in range(1, 6149):  # all col without first and last
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
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Fitting Multiple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    # Predicting the Test set result
    y_pred = regressor.predict(x_test)
    print('Coefficients: \n', regressor.coef_)
    print("T : ",T)
    # The mean squared error
    print("Mean squared error: %.4f"
          % mean_squared_error(y_test, y_pred))


#Preprocessing_data()
for t in range (2,5):
    Linear_reggression(t)
