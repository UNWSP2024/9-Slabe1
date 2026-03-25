# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

def random_write():
    file = open("numbers.txt", 'a')
    amount = int(input("How many numbers would you like to write? "))
    if amount > 1000:
        amount = 1000
    for x in range(amount):
        number = random.randint(1,500)
        file.write(f"{number}\n")
    file.close()


if __name__ == '__main__':
    random_write()

