import aocmm_functions


def calculate(typing_data, in_occurances, in_totals, write=True):
    typing_data = typing_data.upper().replace("OO", "O").strip()
    states = ['B', 'O', 'D', 'U', 'C'];
    occurrences, totals = aocmm_functions.init_occurances_and_totals(states)

    if in_occurances is not None:
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
        probability = aocmm_functions.prob(occurrences[key], totals[key[1]])
        text.append(aocmm_functions.to_probability_string(key[0], key[1], probability))
        probabilities[key] = probability

    # Output
    if write:
        print "Processed Input: ", typing_data
        print "===================ALL Probabilities==============="
        for out in text:
            print out

    return occurrences, totals, probabilities
