
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

        #for x in result:
        #  print(x[0])
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