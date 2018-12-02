
import DBconnect
import ScriptLine


class ScriptFilesController:

    # sceneID = 0  -> For now won't be used
    location = ""       # Global, because it affects all the lines in the current scene

    @staticmethod
    def file_to_scriptLines():
        # Perhaps get these two as parameters
        file = open("C://Users\אליה\PycharmProjects\script1.txt", "r")
        scriptID = 1

        lines_counter = ScriptLine.ScriptLine.static_lines_counter
        speaker = ""

        for line in file:

            speaker = ""

            if len(line) > 1:              # If the line isn't empty (has characters other than '\n'):

                upper_words = line.split()                      # Split the lines into a list of words
                words = list()
                text = ""
                for i in range(0, len(upper_words)):
                    words.append(upper_words[i].lower())        # Create a lowercase copy
                    text += upper_words[i].lower() + " "        # Clean text that will be saved to DB
                text = text[:-1]

                try:                                                            # A regular script line, said by a character
                    if words[0].index(":") + 1 == len(words[0]):                # (Option 1: only first name stated)

                        for i in range(0, len(words[0])-1):             # Save speaker name
                            speaker += words[0][i]

                except ValueError:
                    try:                                                        # A regular script line, said by a character
                        if words[1].index(":") + 1 == len(words[1]) \
                                and words[1] != "to:":                          # (Option 2: full name stated)
                                                                                # (and it's not "cut to:" location line)
                            #for i in range(0, len(words[0]) - 1):       # Save speaker name
                             #   speaker += words[0][i]
                            speaker += words[0] + " " + words[1]
                            speaker = speaker[:-1]

                    except ValueError:
                        if words[0] == "int." or words[0] == "ext." \
                           or (words[0] == "cut" and words[1] == "to:"):        # New scene head line

                                if words[0] == "int." or words[0] == "ext.":
                                    start = 1
                                else:
                                    start = 2

                                # sceneID += 1                            # Save scene ID

                                ScriptFilesController.location = ""      # Clean current location

                                try:
                                    for i in range(start, words.index('-')):
                                        ScriptFilesController.location += " "
                                        ScriptFilesController.location += words[i]            # Save scene location

                                except ValueError:
                                    for i in range(start, len(words)):
                                        ScriptFilesController.location += " "
                                        ScriptFilesController.location += words[i]            # Save scene location

                        else:                                                   # A line that describes actions
                            # Don't save any special data
                            pass

                q = '"'
                query = "insert into littlebirds.scriptline values(" + str(lines_counter) + ",NULL," + q + text + q + ","

                # Save line to DB
                if ScriptFilesController.location == "":
                    query += "NULL,"
                else:
                    query += q + ScriptFilesController.location + q + ","

                if speaker == "":
                    query += "NULL,"
                else:
                    query += q + speaker + q + ","

                query += str(scriptID) + ")"

                DBconnect.DBconnect.send_query(query)
                lines_counter += 1

        ScriptLine.ScriptLine.static_lines_counter += lines_counter         # Update the global number of script-lines
        file.close()
