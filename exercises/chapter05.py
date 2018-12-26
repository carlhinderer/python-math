# Chapter 5 Exercises

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


if __name__ == '__main__':
    draw_venn_diagram()
