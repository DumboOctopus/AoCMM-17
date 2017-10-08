# takes all the raw files for a person and creates a combined text. Then processes the combined text
import os
from data_cruncher import calculate_and_create_file

person_number = raw_input("person: ")

person_data_files = []
for file in os.listdir("Data/"):
    if file.startswith("r_p"+person_number):
        person_data_files.append(file)

paragraph_o = None
paragraph_t = None

quote_o = None
quote_t = None

for filename in person_data_files:
    f = open("Data/"+filename,"r")
    data = ""
    line = f.readline()
    while line:
        data += line
        line = f.readline()

    given = filename[filename.index("g") + 1:]
    if given == '9' or given =='10' or given =='11':
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
    else:
        out =calculate_and_create_file(
            data,
            person_number,
            99,
            paragraph_o,
            paragraph_t,
            write=False
        )

        paragraph_o, paragraph_t = out[0], out[1]
        print paragraph_o, paragraph_t

    f.close()

# Todo: if 2 texts are strung together and the ending char was C and starting char was U
# TODO: occurances of U|C increase... no bueno.
calculate_and_create_file("", person_number, 99, paragraph_o, paragraph_t, write=True)
calculate_and_create_file("", person_number, 89, paragraph_o, paragraph_t, write=True)