import data_cruncher, sqlite3
from aocmm_functions import insert_probabilities
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
## end get data from user

if len(typing_data) > 999: raise Exception("VAR CHAR TOO SMALL BRO")
occurrences, totals, probabilities = data_cruncher.calculate(typing_data, None, None)
probabilities_id = insert_probabilities(probabilities, c)


## creates english_paragraphs or random_paragraphs record

c.execute("INSERT INTO person_data (person, text_id, typing_data, is_conglom, probabilities_id, is_english) " +
              "VALUES ('{}',{},'{}',{}, {}, {})".format(person, text_id, typing_data, 0, probabilities_id, is_english))

## end



#Commits data
conn.commit()
c.close()
conn.close()
#commits data
