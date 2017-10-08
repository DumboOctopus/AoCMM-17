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

    probabilities = {}
    text = []
    for key in sorted(occurrences.keys()):
        probability = 0
        if totals[key[1]] != 0:
            probability = occurrences[key]/(totals[key[1]] + 0.0)     # 0.0 so it does floating point division
        output = "P("+key[0]+"|"+ key[1] + ")=" + str(probability)

        text.append(output)
        probabilities[key] = probability

    # Output
    if write:
        print "Processed Input: ", typing_data
        print "===================ALL Probabilities==============="
        for out in text:
            print out

        f = open("Data/p_p" + str(personNumber) + "g" + str(givenNumber), "w+")
        for line in text:
            f.write(line + "\n")

    return occurrences, totals, probabilities
