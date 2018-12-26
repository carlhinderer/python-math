# Chapter 5 Exercises

import random
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


if __name__ == '__main__':
    # draw_venn_diagram()
    law_of_large_numbers()
