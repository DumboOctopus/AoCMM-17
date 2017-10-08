# takes all the raw files for a person and creates a combined text. Then processes the combined text
import os
from data_cruncher import calculate_and_create_file
from aocmm_functions import is_file_paragraph, is_file_quote

person_number = raw_input("person: ")

person_data_files = []
for filenam in os.listdir("Data/"):
    if filenam.startswith("r_p"+person_number):
        person_data_files.append("Data/" + filenam)

paragraph_o = None
paragraph_t = None

quote_o = None
quote_t = None

for filename in person_data_files:
    f = open(filename,"r")
    data = f.readline()
    # just so that kind of error doesn't slip us by
    if f.readline():
        raise Exception("Warning: input file {} is not formatted correctly".format(filename))


    # TODO: how to ignore file 89 and 99 which are congloms and figure out which ones are paragraphs
    # TODO: and which ones are quotes... maybe add more data to file name
    if is_file_paragraph(filename):
        out = calculate_and_create_file(
            data,
            person_number,
            99,
            paragraph_o,
            paragraph_t,
            write=False
        )

        paragraph_o, paragraph_t = out[0], out[1]
    elif(is_file_quote(filename)):
        out = calculate_and_create_file(
            data,
            person_number,
            89,
            quote_o,
            quote_t,
            write=False
        )
        print out
        quote_o, quote_t = out[0], out[1]

    f.close()

calculate_and_create_file("", person_number, 99, paragraph_o, paragraph_t, write=True)
calculate_and_create_file("", person_number, 89, paragraph_o, paragraph_t, write=True)