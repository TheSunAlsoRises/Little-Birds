
import DBconnect


query_string = "SELECT * FROM tweets"
result = DBconnect.DBconnect.send_query(query_string)