#!/usr/bin/env python

import sys
import random

def secret_num(num):
    if num == 42:
        print("The answer to the ultimate question of life, the universe and everything is", num)

def success(a):
    if a == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!")
        print("You won in", a, "attempts!")
    sys.exit(1)

def guess():
    num = random.randint(1, 99)
    attempt = 0
    close = "exit"
    while True:
        try:
            answer = int(input("What's your guess between 1 and 99? "))
        except (KeyboardInterrupt, SystemExit):
            print("\nGood bye!")
            sys.exit(0)
        except ValueError:
            print("That's not a number.")
            attempt +=1
            continue  
        if answer > num: 
            print("Too high!")
            attempt +=1
            continue
        elif answer < num:
            print("Too low!")
            attempt +=1
            continue
        else:
            attempt +=1
            break
    secret_num(num)
    success(attempt)

def intro():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Press ctrl + c to end the game.")
    print("Good luck!")
    return

def main():
    if len(sys.argv) != 1:
        print('ERROR 1 - No argv.\n- usage: python guess.py')
        sys.exit(0)
    intro()
    guess()


if __name__ == '__main__':
  main()
