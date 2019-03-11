import DBconnect

class LoginController:

    @staticmethod
    def login(username_input, password_input):
        login_result = list()
        q = "'"
        query_string = "SELECT * FROM littlebirds.manager where UserID like " + q + str(username_input) + q + \
                       "AND Password like " + q + str(password_input) + q
        result1 = DBconnect.DBconnect.tuple_to_list(query_string)

        if len(result1) == 0:
            login_result.append(-1)
            login_result.append("")
            return login_result

        else:
            query_string = "Update littlebirds.manager SET Status = 1 where UserID like " + q + str(username_input) + q
            result2 = DBconnect.DBconnect.tuple_to_list(query_string)
            if result2 is None:
                login_result.append(-1)
                login_result.append("")
                return login_result
            else:
                login_result.append(1)
                login_result.append((result1[0])[0])
                return login_result

    @staticmethod
    def logout(username_input):
        q = "'"
        query_string = "Update littlebirds.manager SET Status = 0 where UserID like " + q + str(username_input) + q
        result = DBconnect.DBconnect.tuple_to_list(query_string)
        if result is None:
            return -1
        else:
            return 1

    @staticmethod
    def isLoggedIn(username_input):
        q = "'"
        query_string = "SELECT Status FROM littlebirds.manager where UserID like " + q + str(username_input) + q
        result = DBconnect.DBconnect.tuple_to_list(query_string)
        if len(result) == 0:
            return -1
        else:
            return 1
