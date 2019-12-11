#!/usr/bin/env python

import sys
import types
import math

def controler(number):
    if number == 0:
        print("I'm Zero.")
    elif (number % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return

def main():
    if len(sys.argv) != 2:
        print('ERROR 1 - usage: ./whosis.py <int>')
        sys.exit(1)
    if sys.argv[1].isdigit() == True :
        number = int(sys.argv[1])
        controler(number)
    else:
        print('ERROR 2 - usage: ./whosis.py <int>')
    sys.exit(1)

if __name__ == '__main__':
  main()
