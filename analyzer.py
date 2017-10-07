import os, pprint
from decimal import *
from comparer import compare

processed_data_files = []
for file in os.listdir("Data/"):
    if file.startswith("p"):
        processed_data_files.append(file)

data = {}
for filename1 in processed_data_files:
    for filename2 in processed_data_files:
        person_a, given_a = filename1[3:filename1.index("g")], filename1[5:]
        person_b, given_b = filename2[3:filename1.index("g")], filename2[5:]

        file1 = open("Data/p_p" + person_a + "g" + given_a, "r")
        file2 = open("Data/p_p" + person_b + "g" + given_b, "r")

        A = compare(person_a, given_a, person_b, given_b)

        stuff ="{}_{}  -  {}_{} = {}".format(person_a, given_a, person_b, given_b, A)
        if (person_a, given_a) in data:
            data[(person_a, given_a)].append(stuff)
            data[(person_a, given_a)] = sorted(data[(person_a, given_a)])
        else:
            data[(person_a, given_a)] = [stuff]

        file1.close()
        file2.close()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)