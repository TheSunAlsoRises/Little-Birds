
import pymysql.cursors
import pymysql

class DBconnect:

    @staticmethod
    def send_query(query_string):

        db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="littlebirds",
            # Allows "load data local infile"
            local_infile = True
        )

        mycursor = db.cursor()
        mycursor.execute(query_string)
        result = mycursor.fetchall()

        db.commit()

        db.close()
        return result


    @staticmethod
    def tuple_to_list(query):
        emptyList = list()
        result = DBconnect.send_query(query)
        for i in range(0, len(result)):
            emptyList.append(list(result[i]))
        return emptyList


    #Upload a whole csv file of tweets to DB
    @staticmethod
    def upload_tweets_file():
        query = "load data local infile 'c:/csva.csv' into table tweet" \
                " fields terminated by ',' lines terminated by '\r\n' " \
                "(Date,@dummy1,TweetID,UserID,Location,UserName,OriginalText,@dummy2,@dummy3,Time);"
        #Date, Time, Tweet ID, User ID, User Name, Geo Location, Text, WE Score, WE Polarity, hour
        #use @dummy to skip fields

        DBconnect.send_query(query)
