#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import sys


def get_input():
    return input()


def test_input(s):
    if s.isnumeric():
        return True
    else:
        return False


def str_to_int(s):
    return int(s)


def print_int(a):
    print(a)


if __name__ == '__main__':
    s = get_input()
    if test_input(s):
        print_int(str_to_int(s))
