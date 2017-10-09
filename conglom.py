# takes all the raw files for a person and creates a combined text. Then processes the combined text
import os, sqlite3
from data_cruncher import calculate
from aocmm_functions import insert_probabilities
conn = sqlite3.connect("data.db")
c = conn.cursor()

person = raw_input("person: ")
c.execute("Select typing_data, is_english from person_data where person='{}' and is_conglom=0".format(person))
person_data = c.fetchall()

english_o = None
english_t = None
english_p = None

random_o = None
random_t = None
random_p = None

for typing_data, is_english in person_data:
    if is_english:
        out = calculate(
            typing_data,
            english_o,
            english_t,
            write=False
        )

        english_o, english_t, english_p = out
    else:
        out = calculate(
            typing_data,
            random_o,
            random_t,
            write=False
        )
        #print out
        random_o, random_t,random_p = out


c.execute("SELECT probabilities_id from person_data where person='{}' and is_conglom=1".format(person))
result = c.fetchone()

if result is None:
    probabilities_id = insert_probabilities(english_p, c)
    c.execute("INSERT INTO person_data (person, text_id, typing_data, probabilities_id, is_conglom, is_english)"
              +"Values('{}',{},'{}',{},{},{})".format(person, -1, 'NULL', probabilities_id, 1, 1))


    probabilities_id = insert_probabilities(random_p, c)
    c.execute("INSERT INTO person_data (person, text_id, typing_data, probabilities_id, is_conglom, is_english)"
              +"Values('{}',{},'{}',{},{},{})".format(person, -2, 'NULL', probabilities_id, 1, 0))
else:
    # I feel too afraid
    print "already exists meow"

conn.commit()
c.close()
conn.close()
