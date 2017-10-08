## THIS script was only temporary, we don't need it anymore


# import sqlite3, os, aocmm_functions, data_cruncher
# conn = sqlite3.connect('data.db')
# c = conn.cursor()
#
#
# data_files = []
# for filenam in os.listdir("Data/"):
#     if filenam.startswith("r_p"):
#         data_files.append(filenam)
#
# # iterate over all raw files
# # calculate probabilities using data_cruncher
# # create probabilities record.
# # create english paragraphs record or random paragraphs record and link it to probabilities record.
#
# for filename in data_files:
#     f = file("Data/"+filename, "r")
#     person, given = aocmm_functions.parse_processed_filename(filename)
#     if given == 99 or given == 89:
#         continue
#     else:
#         typing_data = f.readline()
#         if f.readline():
#             raise Exception("yo dawg")
#
#         occurrences, totals, probabilities = data_cruncher.calculate_and_create_file(typing_data, person, given, None, None, write=False)
#         if len(typing_data) > 999:
#             raise Exception("VAR CHAR TOO SMALL BRO")
#         # create probabilities entry:
#         id = 0
#         last_id = c.execute("SELECT id FROM probabilities ORDER BY id DESC LIMIT 1")
#         last_id = c.fetchone()
#         if last_id is None:
#             id = 1
#         else:
#             id = last_id[0] + 1
#
#
#         # hard part, creating code which inserts all probabilities
#         fields_string = "id,"
#         values_strings = str(id)+","
#
#         states = ['B', 'O', 'D', 'U', 'C']
#         for s1 in states:
#             for s2 in states:
#                 transition = s1 + s2
#                 fields_string += transition + ","
#                 values_strings += str(probabilities[(s1, s2)]) + ","
#         values_strings = values_strings[0:len(values_strings)-1]
#         fields_string = fields_string[0:len(fields_string) - 1]
#         c.execute("INSERT INTO probabilities ({}) VALUES ({})".format(fields_string, values_strings))
#
#         is_given = 1 if person != "Q" else 0
#         is_conglom = 0
#         is_paragraph = input("is "+filename + " a paragraph? (True/False): ")
#         if is_paragraph:
#             # person varchar(10), text_id integer, typing_data varchar(1000), is_given tinyint, probabilities_id integer
#             print "INSERT INTO english_paragraphs (person, text_id, typing_data, is_given, is_conglom, probabilities_id) " +"VALUES ('{}',{},'{}',{},{}, {})".format( person, given, typing_data, is_given, is_conglom, id)
#             c.execute("INSERT INTO english_paragraphs (person, text_id, typing_data, is_given, is_conglom, probabilities_id) " +
#                       "VALUES ('{}',{},'{}',{},{}, {})".format( person, given, typing_data, is_given, is_conglom, id))
#         else:
#             c.execute(
#                 "INSERT INTO random_paragraphs (person, text_id, typing_data, is_given, is_conglom, probabilities_id) " +
#                 "VALUES ('{}',{},'{}',{},{}, {})".format(person, given, typing_data, is_given, is_conglom, id))
#
# conn.commit()
# c.close()
# conn.close()