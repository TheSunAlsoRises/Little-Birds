import pymysql


class DBconnect:

    @staticmethod
    def send_query(query_string):

        db = pymysql.connect(
              host="localhost",
              user="root",
              passwd="root",
              database="littlebirds"
        )

        mycursor = db.cursor()
        mycursor.execute(query_string)
        result = mycursor.fetchall()

        db.commit()
        db.close()
        return result