
import DBconnect
import ScriptLine
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re, string



stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()        # Sets a word into its basic form


class ScriptFilesController:


    # sceneID = 0  -> For now won't be used
    location = ""       # Global, because it affects all the lines in the current scene

    @staticmethod
    def file_to_scriptLines(path,scriptID):
        # Important note: the script must not contain quotes (")

        # Perhaps get these two as parameters
        #file = open("C://Users\אליה\PycharmProjects\script2.txt", "r")
        #scriptID = 2

        file = open(path, "r")

        # Get current amount of scriptlines in the DB, and add '1' for the first line of the current script
        lines_counter = 1 + ScriptLine.ScriptLine.static_lines_counter
        speaker = ""


        # Get the names and nicks from the DB, so they'l be ignored in the cleaning
        nicks = list()
        result = DBconnect.DBconnect.tuple_to_list \
            ("SELECT CharacterName FROM littlebirds.category where CategoryID=1"
             + " union " +
             "SELECT LocationName FROM littlebirds.category where CategoryID=2"
             + " union " +
             "SELECT HouseName FROM littlebirds.category where CategoryID=3"
             + " union " +
             "SELECT Nick FROM littlebirds.nick;")
        for i in range(0, len(result)):
            nicks.append((result[i])[0])

        for line in file:

            speaker = ""                                        # Reset for each script-line

            if len(line) > 1:              # If the line isn't empty (has characters other than '\n'):

                words = list(line.lower().split())              # Split the lines into a list of words in lowercase

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

                # Clean the text so it can be analyzed
                clean_text = ""
                for i in range(0, len(words)):
                    # Remove punctuation
                    words[i] = re.sub('['+string.punctuation+']', '',words[i])
                    if words[i] in nicks:
                        # Simply add the words with a meaning in the series
                        clean_text += words[i]
                        clean_text += ' '
                    else:
                        # Set regular words to their basic form
                        # First option - with stemming : caught 1293 words this way
                        # clean_text += (stemmer.stem(lemmatiser.lemmatize(words[i])))

                        # Second option - without stemming : caught 1442 words this way
                        clean_text += (lemmatiser.lemmatize(words[i]))
                        clean_text += ' '
                clean_text = clean_text[:-1]    # Remove last whitespace

                # Also save the original line (without the '\n' character)
                text = line[:-1]

                q = '"'
                query = "insert into littlebirds.scriptline values(" + str(lines_counter) + ",NULL,"\
                        + q + text + q + "," + q + clean_text + q + ","

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
                print(lines_counter)

        # May not be necessary now that we get the amount straigh from the DB (see in class file)
        ScriptLine.ScriptLine.static_lines_counter += lines_counter         # Update the global number of script-lines
        file.close()
