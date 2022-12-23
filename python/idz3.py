#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import sys


def infinite_prod():
    """ prods numbers until 0 is entered"""
    prod = 1
    while True:
        a = int(input("Enter number: "))

        if a != 0:
            prod *= a
            print(f"Cur prod: {prod}")
        else:
            print(f"Final prod: {prod}")
            break


if __name__ == '__main__':
    infinite_prod()
