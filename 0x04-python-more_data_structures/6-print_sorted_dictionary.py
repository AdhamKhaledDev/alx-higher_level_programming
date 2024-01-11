#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for neo in sorted (a_dictionary.keys()):
        print("{}: {}".format (neo, a_dictionary[neo]))
