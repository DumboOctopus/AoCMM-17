import os, pprint, sqlite3
from munkres import Munkres
from comparer import compare


conn = sqlite3.connect("data.db")
c = conn.cursor()
c.execute("SELECT person, text_id from person_data where is_english=0 and is_conglom = 1")
stuffs = c.fetchall()
print stuffs

data = {}
for person_a, text_a in stuffs:
    for person_b, text_b in stuffs:
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
            data[(person_a, text_a)] = sorted(data[(person_a, text_a)], key=lambda a: a[0] + str(a[1]))
        else:
            data[(person_a, text_a)] = [stuff]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

matrix = []
for key in data.keys():
    row = []
    for thing in data[key]:
        row.append(thing[2])
    matrix.append(row)

print "\n\n\n\n\n\n\n\n"

m = Munkres()
indexes = m.compute(matrix)
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print '%s -> %f %s' % (data.keys()[row][0], value, data[data.keys()[0]][column][0])
print 'total cost: %f' % total