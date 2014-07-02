"""
Filename: quad.py
Authors: Chase Coleman, Spencer Lyon, John Stachurski, Thomas Sargent
Date: 2014-07-01

Defining various rootfinding routines in pure python.

"""
from __future__ import division, print_function


def bisect(f, a, b, tol=1e-13, maxit=100):
    """
    Bisection method for finding the root of a scalar function f on the
    interval from a to b. It must be the case that f(a) and f(b) have
    different signs.

    Parameters
    ----------
    f : function
        The function to be optimized

    a : scalar, float
        The lower bound for the optimization interval

    b : scalar, float
        The upper bound for the optimization interval

    tol : scalar, float, optional(default=1e-13)
        The tolerance level for convergence

    maxit : scalar, int, optional(default=100)
        The maximum number of iterations to attempt

    Returns
    -------
    root : scalar
        The root of the function.

    """
    if f(a) * f(b) > 0:
        print("f(a) and f(b) must have different signs")
        return False

    err = 1.0
    its = 0

    # See if they already passed us a root. That'd be awesome.
    if abs(f(a)) < tol:
        return a

    if abs(f(b)) < tol:
        return b

    for i in range(maxit):
        c = (a + b) / 2.0
        if abs(f(c)) < tol:
            return c

        its += 1
        if f(c) * f(a) >= 0:
            a = c
        else:
            b = c

    else:
        print("Max Iterations exceeded in bisect")
        return False

