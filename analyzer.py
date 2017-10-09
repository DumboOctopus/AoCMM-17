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
        if text_a != -1 or text_b != -1: continue
        c.execute("Select is_given from person_unknown where person = '{}'".format(person_a))
        is_given_a = c.fetchone()[0] == 1
        if not is_given_a: continue
        c.execute("Select is_given from person_unknown where person = '{}'".format(person_b))
        is_given_b = c.fetchone()[0] == 1
        if is_given_b: continue


        A = compare(person_a, text_a, person_b, text_b)

        stuff = (person_b, text_b, A)
        if (person_a, text_a) in data:
            data[(person_a, text_a)].append(stuff)
            data[(person_a, text_a)] = sorted(data[(person_a, text_a)], key=lambda a: a[2])
        else:
            data[(person_a, text_a)] = [stuff]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)