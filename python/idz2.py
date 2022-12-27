#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import sys


def cylinder(h, r, full_calculations):
    """ returns cylinder area(full or not)"""
    if full_calculations.lower() == "yes":
        return 2 * math.pi * r * h + 2 * circle(r)
    else:
        return 2 * math.pi * r * h


def circle(r):
    """ returns circle area"""
    return math.pi * r ** 2


if __name__ == '__main__':
    h = int(input("Input height: "))
    r = int(input("Input radius: "))
    full_calculations = input("Do you want to know full calculations? Yes or No: ")
    
    print(cylinder(h, r, full_calculations))
