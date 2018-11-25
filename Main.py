
import DBconnect


query_string = "SELECT count(*) FROM tweet"
result = DBconnect.DBconnect.send_query(query_string)