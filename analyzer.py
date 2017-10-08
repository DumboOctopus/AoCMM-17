import os, pprint
from aocmm_functions import get_all_processed_files, parse_processed_filename
from comparer import compare

processed_data_files = get_all_processed_files()

data = {}
for filename1 in processed_data_files:
    for filename2 in processed_data_files:
        person_a, given_a = parse_processed_filename(filename1)
        person_b, given_b = parse_processed_filename(filename2)

        A = compare(person_a, given_a, person_b, given_b)

        stuff ="{}_{}  -  {}_{} = {}".format(person_a, given_a, person_b, given_b, A)
        if (person_a, given_a) in data:
            data[(person_a, given_a)].append(stuff)
            data[(person_a, given_a)] = sorted(data[(person_a, given_a)]) # keeps everything sorted f
        else:
            data[(person_a, given_a)] = [stuff]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)