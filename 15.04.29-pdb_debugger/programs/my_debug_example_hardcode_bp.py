#!/usr/bin/env python

"""Example file to demonstrate pdb to debug a poorly written program"""
from a_random_function import foo

def main():
    """Main function to be executed"""

    a_string = "I'm a string"
    a_dict   = {'a_key':[1,2,3], 'another_key':'Hey, Macarena!'}
    a_number = 10

    output = first_func(a_string, a_dict, a_number)

    print("Execution completed, output = {0}".format(output))


def first_func(s, d=None, *args):
    """'Unreadable' function, with bad docstring, which purpose is
    1. To call another function, and print its output
    2. To do some 'stuff', and return 'something'"""

    # Here is the function call and the output
    output = second_func(first_func, d['a_key'])
    print("second_func returned {}".format(output))

    # Here we do some 'stuff'
    b = 1
    something = args[0] + b
    return something


def second_func(a_function, a_list):
    """We can illustrate some nice features with pdb with this second
    function. What it does is completely irrelevant, but it contains a
    for loop"""

    # A hard coded breakpoint
    pdb.set_trace()
    foo()
    for i in range(len(a_list)):
        a_list[i] += 1

    return a_list


if __name__ == '__main__':
    import pdb
    main()
