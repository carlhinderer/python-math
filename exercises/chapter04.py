# Chapter 4 Exercises

from sympy import Symbol, symbols, pprint, init_printing, sympify, solve, summation
from sympy.plotting import plot

# 4-2 Graphical Equation Solver
#
# Get 2 expressions from the user and graph them.  Also, print their solution.


def graphical_equation_solver():
    f1, f2 = get_functions_from_user()
    print_solution(f1, f2)
    graph_functions(f1, f2)


def get_functions_from_user():
    x = Symbol('x')
    y = Symbol('y')
    f1 = input('Enter the first expression: ')
    f2 = input('Enter the second expression: ')
    try:
        f1 = sympify(f1)
        f2 = sympify(f2)
        return f1, f2
    except:
        print('Invalid expression')


def graph_functions(f1, f2):
    graphs = []
    for f in (f1, f2):
        graph = solve(f, Symbol('y'))[0]
        graphs.append(graph)
    plot(graphs[0], graphs[1])


def print_solution(f1, f2):
    solution = solve((f1, f2), dict=True)[0]
    x, y = solution[Symbol('x')], solution[Symbol('y')]
    print('Solution: (x: %s, y: %s)' % (x, y))


# 4-3 Series Summation
#
# Write a program that takes an expression for the nth term in a series and a
#   number of terms.  Print the summation of the sequence.

def series_summation():
    nth_term, num_terms = get_series_and_terms()
    print_summation(nth_term, num_terms)


def get_series_and_terms():
    nth_term = input('Enter the expression for the nth term in the series: ')
    num_terms = int(input('Enter the number of terms: '))
    return nth_term, num_terms


def print_summation(nth_term, num_terms):
    a, d, n = symbols('a,d,n')
    nth_term = sympify(nth_term)
    s = summation(nth_term, (n, 1, num_terms))
    pprint(s)


if __name__ == '__main__':
    series_summation()
