#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator_ = 0
    denominator_ = 0

    for tup in my_list:
        numerator_ += tup[0] * tup[1]
        denominator_ += tup[1]

    return (numerator_ / denominator_)
