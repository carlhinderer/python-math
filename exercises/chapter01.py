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


# 1-3 Enhanced Unit Converter
#
# Write functions to convert between units.
#   1. For length (between km and miles)
#   2. For mass (between kg and lbs)
#   3. For temperature (between Celsius and Farenheit)

MILES_IN_KILOMETER = 0.62137119
KILOGRAMS_IN_POUND = 2.20462262185


def km_to_miles(km):
    return km * MILES_IN_KILOMETER


def miles_to_km(miles):
    return miles * (1 / MILES_IN_KILOMETER)


def kg_to_lbs(kg):
    return kg * KILOGRAMS_IN_POUND


def lbs_to_kg(lbs):
    return lbs * (1 / KILOGRAMS_IN_POUND)


def celsius_to_farenheit(degrees_celsius):
    return (9 / 5 * degrees_celsius) + 32


def farenheit_to_celsius(degrees_farenheit):
    return 5 / 9 * (degrees_farenheit - 32)



# 1-4 Fraction Calculator
#
# Ask the user for 2 fractions and the operation they want to carry out, then return the result.
from fractions import Fraction


def fraction_calculator():
    f1 = Fraction(input('Enter the first fraction: '))
    f2 = Fraction(input('Enter the second fraction: '))
    op = input('Enter the operation to perform (Add|Subtract|Multiply|Divide): ')
    if op == 'Add':
        print('Result of Addition: %s' % (f1 + f2))
    elif op == 'Subtract':
        print('Result of Subtraction: %s' % (f1 - f2))
    elif op == 'Multiply':
        print('Result of Multiplication: %s' % (f1 * f2))
    elif op == 'Divide':
        print('Result of Division: %s' % (f1 / f2))
