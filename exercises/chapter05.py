# Chapter 5 Exercises

import random
import math
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from sympy import FiniteSet


# 5-1 Venn Diagrams
#
# Plot a Venn diagram of the set of odd numbers under 20 and the set of prime numbers under 20.

ODDS_UNDER_20 = FiniteSet(*range(1, 21, 2))
PRIMES_UNDER_20 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)


def draw_venn_diagram():
    sets = (ODDS_UNDER_20, PRIMES_UNDER_20)
    labels = ('Odds', 'Primes')
    venn2(subsets=sets, set_labels=labels)
    plt.show()


# 5-2 Law of Large Numbers
#
# Let's use a die roll as a discreet random variable.  The expected value of a roll is:
#
#   >>> e = 1*(1/6) + 2*(1/6) + 3*(1/6) + 4*(1/6) + 5*(1/6) + 6*(1/6)
#   >>> e
#   3.5
#
# According to the law of large numbers, the average value of results over multiple trials
#   approaches the expected value as the number of trials increases.  Verify this by
#   rolling a 6-sided die the following number of times: 100, 1000, 10000, 100000, 500000.

TRIAL_COUNTS = [100, 1000, 10000, 100000, 500000]
DIE_ROLLS = list(range(1, 7))


def law_of_large_numbers():
    print('Expected value:', expected_value())
    for count in TRIAL_COUNTS:
        average = do_trials(count)
        print('Trials: %s Trial Average: %s' % (count, average))


def do_trials(count):
    total = 0
    for i in range(count):
        total += random.randint(1, 6)
    return total / count


def expected_value():
    return sum(DIE_ROLLS) / len(DIE_ROLLS)


# 5-3 How Many Tosses Before You Run Out of Money?
#
# Let's consider a game in which a play wins $1 for heads and loses $1.50 for tails.
#   The game is over when the player's balance equals zero.  Write a program to
#   simulate this game.


def coin_game():
    current_amt = int(input('Enter your starting amount: '))
    num_tries = 0
    while current_amt > 0:
        flip = random.randint(0, 1)
        if flip == 0:
            current_amt += 1
            print('Heads! Current amount: ', current_amt)
        else:
            current_amt -= 1.5
            print('Tails! Current amount: ', current_amt)
        num_tries += 1
    print('Game over :( Current amount: %s, Coin tosses: %s' % (current_amt, num_tries))


# 5-4 Shuffling a Deck of Cards
#
# Create a deck of 52 cards and shuffle them.

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)


class Deck:
    SUITS = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def show(self):
        for card in self.cards:
            print(card)


def shuffled_deck():
    deck = Deck()
    deck.shuffle()
    deck.show()


# 5-5 Estimating the Area of a Circle
#
# The area of a circle can be estimated by throwing darts at a dartboard that is a square
#   with a circle inscribed.  Write a program that takes in a user-defined radius, and
#   throws (1000, 10000, 100000) darts to estimate the area of a circle.


DART_COUNTS = [1000, 10000, 100000]


def estimate_circle_area():
    radius = float(input('Enter the radius of the circle: '))
    print('Radius:', radius)
    for count in DART_COUNTS:
        estimate_area(radius, count)


def estimate_area(radius, dart_count):
    actual_area = math.pi * radius**2
    hits = 0
    for dart in range(dart_count):
        if throw_dart(radius):
            hits += 1
    estimated_area = (hits / dart_count) * (2 * radius)**2
    print('Area: %s, Estimated (%s darts): %s' % (actual_area, dart_count, estimated_area))


def throw_dart(radius):
    x, y = random_point(radius)
    distance_to_center = math.sqrt((radius - x)**2 + (radius - y)**2)
    return distance_to_center <= radius


def random_point(radius):
    return random_coord(radius), random_coord(radius)


def random_coord(radius):
    return random.uniform(0, 2 * radius)


if __name__ == '__main__':
    # draw_venn_diagram()
    # law_of_large_numbers()
    # coin_game()
    # shuffled_deck()
    estimate_circle_area()
