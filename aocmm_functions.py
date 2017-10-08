import os

# This file just hosts a lot of functions which need to be refactored somewhere else
# so the code looks nicer. Note: this does not include ALL functions. For example,
# the compare function is still inside comparer.

_states = ['B', 'O', 'D', 'U', 'C']
def init_occurances_and_totals():
    occurrences = {}
    totals = {}

    for prev_state in _states:
        totals[prev_state] = 0
        for next_state in _states:
            occurrences[(next_state, prev_state)] = 0

    return occurrences, totals


def prob(occurrence, total):
    if total == 0:
        return 0
    else:
        return occurrence / (total + 0.0)


def to_probability_string(next_state, prev_state, probability):
    return "P(" + str(next_state) + "|" + str(prev_state) + ")=" + str(probability)


def get_probs(person, text_id, c):
    c.execute("Select probabilities_id from person_data where person='{}' and text_id ={} LIMIT 1".format(person, text_id))
    probabilities_id = c.fetchone()[0]

    fields_string = probabilities_in_order()

    #enforces ordering
    c.execute("SELECT {} From probabilities where id = {}".format(fields_string, probabilities_id))
    return c.fetchone()


def probabilities_in_order():
    fields_string = ""
    for s1 in _states:
        for s2 in _states:
            fields_string += s1 + s2 + ","
    fields_string = fields_string[0:len(fields_string) - 1]
    return fields_string

def insert_probabilities(probabilities,c):
    probabilities_id = 0
    c.execute("SELECT id FROM probabilities ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()
    if last_id is None:
        probabilities_id = 1
    else:
        probabilities_id = last_id[0] + 1

    # hard part, creating code which inserts all probabilities
    fields_string = "id,"
    values_strings = str(probabilities_id) + ","
    # DOO NOT MODIFY INSERT ORDER OR WE WILL BE SAD WITH COMPARING
    states = ['B', 'O', 'D', 'U', 'C']
    for s1 in states:
        for s2 in states:
            transition = s1 + s2
            fields_string += transition + ","
            values_strings += str(probabilities[(s1, s2)]) + ","
    values_strings = values_strings[0:len(values_strings) - 1]
    fields_string = fields_string[0:len(fields_string) - 1]
    c.execute("INSERT INTO probabilities ({}) VALUES ({})".format(fields_string, values_strings))
    return probabilities_id