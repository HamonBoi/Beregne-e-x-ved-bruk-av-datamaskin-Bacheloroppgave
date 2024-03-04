from gmpy2 import mpz, mpfr, mul, div, add, sub

def exp(x, n=50, precision = 53):
    n = mpz(n)
    if x < 0:
        l = 1
        x = mpfr(-x, precision)
    else:
        l = 0
        x = mpfr(x, precision)
    m = mpz(0)
    while x > 1:
        x = div(x, 2)
        m = add(m, 1)
    sum = mpfr(add(1, div(x, n)), precision)
    for i in range(n, 0, -1):
        sum = mpfr(add(1, mpfr(mul(div(x, i), sum), precision)), precision)
    for i in range(m):
        sum = mpfr(mul(sum, sum), precision)
    return sum