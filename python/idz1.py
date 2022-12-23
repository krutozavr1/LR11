#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


def test():
    """ checks if variable positive or negative"""
    a = int(input())

    if a < 0:
        negative()
    elif a > 0:
        positive()


def positive():
    print("Positive")


def negative():
    print("Negative")


if __name__ == '__main__':
    test()
