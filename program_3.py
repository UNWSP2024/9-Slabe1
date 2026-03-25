# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    try:
        file = open("numbers.txt", 'r')
        number = file.readline()
        number = number.rstrip('\n')
        total = 0
        while number != '':
            total += int(number)
            number = file.readline()
            number = number.rstrip('\n')
        print("total is:", total)
        file.close()
    except IOError as err:
        print(err)
    except ValueError as err:
        print(err)
    except:
        print("An error occured")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()