#!/usr/bin/python3
def weight_average(input_list=[]):
    if not input_list:
        return 0

    numerator = 0
    denominator = 0

    for pair in input_list:
        numerator += pair[0] * pair[1]
        denominator += pair[1]

    return (numerator / denominator)
