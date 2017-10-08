import os, pprint, sqlite3
from comparer import compare
conn = sqlite3.connect("data.db")
c = conn.cursor()
c.execute("SELECT person, text_id from person_data where is_english=1")
stuffs = c.fetchall()
print stuffs

data = {}
for person_a, text_a in stuffs:
    for person_b, text_b in stuffs:

        A = compare(person_a, text_a, person_b, text_b)

        stuff ="{}_{}  -  {}_{} = {}".format(person_a, text_a, person_b, text_b, A)
        if (person_a, text_a) in data:
            data[(person_a, text_a)].append(stuff)
            data[(person_a, text_a)] = sorted(data[(person_a, text_a)]) # keeps everything sorted f
        else:
            data[(person_a, text_a)] = [stuff]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)