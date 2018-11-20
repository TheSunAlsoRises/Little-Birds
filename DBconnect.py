import pymysql


class DBconnect:

    @staticmethod
    def send_query(query_string):

        db = pymysql.connect(
              host="localhost",
              user="root",
              passwd="root",
              database="Tweets"
        )

        mycursor = db.cursor()
        mycursor.execute(query_string)
        result = mycursor.fetchall()

        for x in result:
          print(x[6])

        db.close()

        return result