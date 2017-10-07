# takes all the raw files for a person and creates a combined text. Then processes the combined text
import os
from data_cruncher import calculate_and_create_file

person_number = input("person number: ")

person_data_files = []
for file in os.listdir("Data/"):
    if file.startswith("r") and file[3:file.index("g")] == str(person_number):
        person_data_files.append(file)

text = ""
for filename in person_data_files:
    f = open("Data/"+filename,"r")
    line = f.readline()
    while line:
        text += line
        line = f.readline()
    f.close()

calculate_and_create_file(text, person_number, 20)