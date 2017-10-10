import aocmm_functions, sqlite3

def calculate_2_state(typing_data, in_occurances, in_totals, write=True):
    typing_data = typing_data.upper().strip()
    typing_data = typing_data.replace("B", "I")
    typing_data = typing_data.replace("D", "I")
    typing_data = typing_data.replace("U", "I")
    typing_data = typing_data.replace("O", "I")

    print typing_data

    occurrences, totals = {'CC': 0, 'IC': 0,'CI': 0,'II': 0,}, {'C': 0, 'I': 0}

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

conn = sqlite3.connect("data.db")
c = conn.cursor()

c.execute("SELECT typing_data FROM person_data")