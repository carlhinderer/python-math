# Chapter 1 Exercises

# 1-1: Even-Odd Vending Machine
#
# Take an integer as input and
#   1. Print whether the integer is even or odd
#   2. Print the number followed by the next 9 even or odd numbers.
#   3. Validate that input is an integer


def even_odd_vending_machine():
    num = int(input('Enter an integer: '))
    if num % 2 == 0:
        print('Number is even.')
    else:
        print('Number is odd.')
    for i in range(num, num + 20, 2):
        print(i, end=' ')


# 1-2 Enhanced Multiplication Table Generator
#
# Take in an integer and a number of multiples to print, and print them.

def multiplication_table():
    num = int(input('Enter an integer: '))
    multiples = int(input('Enter number of multiples: '))
    table = [i * num for i in range(1, multiples + 1)]
    for mult in table:
        print(mult, end=' ')
