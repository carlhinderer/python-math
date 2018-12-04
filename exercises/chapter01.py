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
