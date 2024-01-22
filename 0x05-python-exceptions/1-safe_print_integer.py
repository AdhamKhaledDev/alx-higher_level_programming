#!/usr/bin/python3
def safe_print_list_integers(input_list=[], num_elements=0):
    count = 0
    for index in range(num_elements):
        try:
            print("{:d}".format(input_list[index]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
