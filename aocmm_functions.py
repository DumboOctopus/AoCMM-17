import os

# This file just hosts a lot of functions which need to be refactored somewhere else
# so the code looks nicer. Note: this does not include ALL functions. For example,
# the compare function is still inside comparer.

# TODO: fix file naming convention
# TODO: quotes are actually the english paragraphs and paragraphs are actually the random ones .... RENAME STUFFF

def init_occurances_and_totals(states):
    occurrences = {}
    totals = {}

    for prev_state in states:
        totals[prev_state] = 0
        for next_state in states:
            occurrences[(next_state, prev_state)] = 0

    return occurrences, totals


def prob(occurrence, total):
    if total == 0:
        return 0
    else:
        return occurrence / (total + 0.0)


def to_probability_string(next_state, prev_state, probability):
    return "P(" + str(next_state) + "|" + str(prev_state) + ")=" + str(probability)


def generate_p_filename(person, given):
    return "Data/p_p" + person + "g" + given


def is_file_paragraph(filename):
    person, given = parse_processed_filename(filename)
    for i in xrange(1, 9):
        if given == str(i):
            return True
    return False


def is_file_quote(filename):
    person, given = parse_processed_filename(filename)
    return given == '9' or given == '10' or given == '11'


def write_processed_file(person, given, probabilities):
    f = open("Data/p_p" + str(person) + "g" + str(given), "w+")
    for probability in probabilities:
        f.write(probability + "\n")


def parse_processed_filename(filename):
    person = filename[3:filename.index('g')]
    given = filename[filename.index('g') + 1:]
    return person, given


def get_all_processed_files():
    processed_data_files = []
    for file in os.listdir("Data/"):
        if file.startswith("p"):
            processed_data_files.append(file)
    return processed_data_files