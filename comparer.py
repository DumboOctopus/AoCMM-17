from decimal import *

def compare(person_a, given_a, person_b, given_b):
    file1 = open("Data/p_p"+person_a + "g"+given_a, "r")
    file2 = open("Data/p_p"+person_b + "g"+given_b, "r")

    A = 0
    for times in xrange(5**2):
        p1 = Decimal(file1.readline()[7:]) # to cut of P(X|Y)=
        p2 = Decimal(file2.readline()[7:]) # ^
        A += abs(p1 - p2)

    return A

if __name__ == "__main__":
    person_a = raw_input("Person A: ")
    given_a = raw_input("Given A: ")
    person_b = raw_input("Person B: ")
    given_b = raw_input("Given B: ")
    print compare(person_a, given_a, person_b, given_b)