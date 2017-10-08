from decimal import *
import sqlite3, aocmm_functions

def compare(person_a, text_a, person_b, text_b):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    probs1 = aocmm_functions.get_probs(person_a, text_a,c)
    probs2 = aocmm_functions.get_probs(person_b, text_b,c)

    A = 0
    for times in xrange(5**2):
        p1 = Decimal(probs1[times]) # to cut of P(X|Y)=
        p2 = Decimal(probs2[times]) # ^
        A += abs(p1 - p2)
    c.close()
    conn.close()
    return A

if __name__ == "__main__":
    person_a = raw_input("Person A: ")
    given_a = raw_input("Given A: ")
    person_b = raw_input("Person B: ")
    given_b = raw_input("Given B: ")
    print compare(person_a, given_a, person_b, given_b)