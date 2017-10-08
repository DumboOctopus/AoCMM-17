import data_cruncher, sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()


## Gets data from user
lines = []
while True:
    line = raw_input()
    if line:
        lines.append(line)
    else:
        break
typing_data = "".join(lines)
typing_data = typing_data.upper()


person = raw_input("Person: ")
text_id = input("Text id: ")
is_english = input("Is English (1/0): ")
is_given = input("Is the person known? (1/0): ")
## end get data from user



## creates probabilities record and enters it
occurrences, totals, probabilities = data_cruncher.calculate(typing_data, None, None)

#just checking
if len(typing_data) > 999: raise Exception("VAR CHAR TOO SMALL BRO")
id = 0
c.execute("SELECT id FROM probabilities ORDER BY id DESC LIMIT 1")
last_id = c.fetchone()
if last_id is None:
    id = 1
else:
    id = last_id[0] + 1

# hard part, creating code which inserts all probabilities
fields_string = "id,"
values_strings = str(id) + ","

# DOO NOT MODIFY INSERT ORDER OR WE WILL BE SAD WITH COMPARING
states = ['B', 'O', 'D', 'U', 'C']
for s1 in states:
    for s2 in states:
        transition = s1 + s2
        fields_string += transition + ","
        values_strings += str(probabilities[(s1, s2)]) + ","
values_strings = values_strings[0:len(values_strings) - 1]
fields_string = fields_string[0:len(fields_string) - 1]
c.execute("INSERT INTO probabilities ({}) VALUES ({})".format(fields_string, values_strings))
## end of getting probabilities record and entering it


## creates english_paragraphs or random_paragraphs record

c.execute("INSERT INTO english_paragraphs (person, text_id, typing_data, is_given, is_conglom, probabilities_id, is_english) " +
              "VALUES ('{}',{},'{}',{},{}, {})".format(person, text_id, typing_data, is_given, 0, id, is_english))

## end



#Commits data
conn.commit()
c.close()
conn.close()
#commits data
