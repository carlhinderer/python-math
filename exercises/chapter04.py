# Chapter 4 Exercises

from sympy import (Symbol, symbols, pprint, init_printing, sympify, solve, summation,
                   sin, Poly, solve_poly_inequality, solve_rational_inequalities,
                   solve_univariate_inequality)
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


# 4-4 Solving Inequalities
#
# In addition to solving equations, sympy can also solve single-variable inequalities.
#   Write a function that will take any inequality, solve it, and return the result.


def solve_inequality():
    inequality = get_inequality_from_user()
    x = Symbol('x')
    if inequality.is_polynomial():
        result = solve_polynomial_inequality(inequality, x)
    elif inequality.is_rational_function():
        result = solve_rational_inequality(inequality, x)
    else:
        result = solve_uni_inequality(inequality, x)
    print(result)


def solve_polynomial_inequality(inequality, symbol):
    lhs = inequality.lhs
    p = Poly(lhs, symbol)
    rel = inequality.rel_op
    return solve_poly_inequality(p, rel)


def solve_rational_inequality(inequality, symbol):
    lhs = inequality.lhs
    numer, denom = lhs.as_numer_denom()
    p1, p2 = Poly(numer), Poly(denom)
    rel = inequality.rel_op
    return solve_rational_inequalities([[((p1, p2), rel)]])


def solve_uni_inequality(inequality, symbol):
    return solve_univariate_inequality(inequality, symbol, relational=False)


def get_inequality_from_user():
    return sympify(input('Enter the inequality (in terms of x): '))


if __name__ == '__main__':
    # graphical_equation_solver()
    # series_summation()
    solve_inequality()
