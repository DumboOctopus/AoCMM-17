import data_cruncher
lines = []
while True:
    line = raw_input()
    if line:
        lines.append(line)
    else:
        break
typing_data = "".join(lines)
typing_data = typing_data.upper()

person_number = raw_input("Person Number: ")
given_number = input("Given Number: ")

f = open("Data/r_p"+str(person_number) + "g"+str(given_number), "w+")
f.write(typing_data)

data_cruncher.calculate_and_create_file(typing_data, person_number, given_number)