#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import sys


def cylinder():
    """ returns cylinder area(full or not)"""
    h = int(input("Input height: "))
    r = int(input("Input radius: "))
    full_calculations = input("Do you want to know full calculations? Yes or No: ")

    if full_calculations.lower() == "yes":
        return 2 * math.pi * r * h + 2 * circle(r)
    else:
        return 2 * math.pi * r * h


def circle(r):
    """ returns circle area"""
    return math.pi * r ** 2


if __name__ == '__main__':
    print(cylinder())
