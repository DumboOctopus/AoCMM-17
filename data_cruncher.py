def calculate_and_create_file(typing_data, personNumber, givenNumber, in_occurances, in_totals, write=True):
    typing_data = typing_data.upper().replace("OO", "O").strip()
    occurrences = {}
    totals = {}
    states = ['B', 'O', 'D', 'U', 'C'];

    if in_occurances == None:
        for prev_state in states:
            totals[prev_state] = 0
            for next_state in states:
                occurrences[(next_state, prev_state)] = 0
    else:
        occurrences = in_occurances
        totals = in_totals

    for i in xrange(len(typing_data) - 1):
        prev_state = typing_data[i]
        next_state = typing_data[i+1]

        occurrences[(next_state, prev_state )] += 1
        totals[prev_state] += 1

    probabilities = []
    non_zero_probabilities = []
    for key in sorted(occurrences.keys()):
        probability = 0
        if totals[key[1]] != 0:
            probability = occurrences[key]/(totals[key[1]] + 0.0)     # 0.0 so it does floating point division
        output = "P("+key[0]+"|"+ key[1] + ")=" + str(probability)

        if probability > 0:
            non_zero_probabilities.append(output)
        probabilities.append(output)


    # Output
    if write:
        print "Processed Input: ", typing_data
        print "===================ALL Probabilities==============="
        for probability in probabilities:
            print probability
        print "==================NON ZERO Probs==================="
        for probability in non_zero_probabilities:
            print probability

        f = open("Data/p_p"+ str(personNumber) + "g"+ str(givenNumber), "w+")
        for probability in probabilities:
            f.write(probability+"\n")

    return occurrences, totals, probabilities, non_zero_probabilities

# call function
# if  __name__ == "__main__":
#     lines = []
#     while True:
#         line = raw_input()
#         if line:
#             lines.append(line)
#         else:
#             break
#     typing_data = "".join(lines)
#
#     personNumber = raw_input("Person: ")
#     givenNumber = raw_input("Given: ")
#     typing_data = typing_data.upper().replace("OO", "O").strip()
#
#     calculate_and_create_file(typing_data, personNumber, givenNumber)