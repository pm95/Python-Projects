# Author: Pietro Malky
# Purpose: test out arithmetic expression evaluation algorithms
# Date: 09/09/2019

import re


# Function Definitions
def tokenizeExpression(expr):
    pattern = "([*| /| +| -])"
    expr = re.split(pattern, expr)

    # takes care of wrongly-tokenized negative numbers
    i = 0
    while i < len(expr)-2:
        if expr[i] == '' and expr[i+1] == '-':
            expr[i+2] = str(-1 * float(expr[i+2]))
            del expr[i+1]
            del expr[i]
        i += 1

    return expr


def evalStatement(a, b, op):
    a = float(a)
    b = float(b)

    if op == '*':
        return a * b
    elif op == '/' and b != 0:
        return a / b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b


def evalHighPrecedence(expr, ops=['*', '/']):
    i = 0
    while i < len(expr):
        if expr[i] in ops:
            l = i - 1
            r = i + 1

            expr[i] = evalStatement(expr[l], expr[r], expr[i])

            del expr[r]
            del expr[l]
        i += 1
    return expr


def evalLowPrecedence(expr, ops=['+', '-']):
    i = 1
    while len(expr) > 1:
        l = i - 1
        r = i + 1
        expr[i] = evalStatement(expr[l], expr[r], expr[i])
        del expr[r]
        del expr[l]

    return expr


def evalExpression(expr):
    # Tokenize expression into numbers and operators
    expr = tokenizeExpression(expr)

    # Evaluate high-precedence operations first
    expr = evalHighPrecedence(expr)

    # Evaluate low-precedence operations second
    expr = evalLowPrecedence(expr)

    # Result will be first (and only) element in resulting list
    return expr[0]


# Test expressions
# test and verify:
# "55555*99999":"1e-7"
# 44+(Clear)13+45(backspace) = 17 (Should compute 13 + 4)
expressions = {
    "5+4*12-100+52/2": -21,
    "5+2": 7,
    "6-3": 3,
    "4*8": 32,
    "15/3": 5,
    "32.6/3.2+90.7": 100.8875,
    "-1.5+6": 4.5,
    "19-27.2": -8.2,
    "56+34+14+5.5": 109.5,
}


for e in expressions:
    calc = evalExpression(e)
    real = expressions[e]

    print("\nExpression:%s\nCalculated Value:%s\nReal Value:%s\n" %
          (e, calc, real))
