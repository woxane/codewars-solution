from numpy import matrix
def fib(n):
    return (matrix('0 1; 1 1' if n >= 0 else '-1 1; 1 0', object) ** abs(n))[0, 1]
