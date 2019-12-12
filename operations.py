#!/usr/bin/env python

import sys
import types
import math

def operations(number_1, number_2):
    print("Sum:\t\t", number_1 + number_2)
    print("Difference:\t\t", number_1 - number_2)
    print("Product:\t\t", number_1 * number_2)
    if number_2 != 0:
        print("Quotient:\t\t", number_1 / number_2)
        print("Remainder:\t\t", number_1 % number_2)
    else:
        print("Quotient:\t\tERROR (div by zero)")
        print("Remainder:\t\tERROR (modulo by zero)")
    return

def main():
    if len(sys.argv) != 3:
        print('ERROR 1 - only two argv.\n- usage: python operations.py <int> <int>')
        sys.exit(1)
    if sys.argv[1].isdigit() == True and  sys.argv[2].isdigit() == True :
        number_1 = int(sys.argv[1])
        number_2 = int(sys.argv[2])
        operations(number_1, number_2)
    else:
        print('ERROR 2 - only numbers\n- usage: python operations.py <int> <int>')
    sys.exit(1)

if __name__ == '__main__':
  main()