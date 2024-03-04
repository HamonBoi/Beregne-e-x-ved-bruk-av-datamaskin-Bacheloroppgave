from gmpy2 import mpz, mpfr, mul, div, add, sub

def pow(a, b, precision = 53):
    a = mpfr(a, precision)
    b = mpz(b)
    out = mpfr(1, precision)
    for i in range(mpz(0), b):
        out = mpfr(mul(out, a), precision)
    return out

def fact(n):
    n = mpz(n)
    out = mpz(1)
    if n==mpz(0) or n==mpz(1):
        return out
    for i in range(mpz(1), n+1):
        out = mul(out, i)
    return out

def exp(x, n=50, precision = 53):
    out = mpfr(0, precision)
    x = mpfr(x, precision)
    n = mpz(n)
    for i in range(n):
        out = mpfr(add(out, div(pow(x, i), fact(i))), precision)
    return out

def exp2(x, n=50):
    out = mpfr(0)
    x = mpfr(x)
    n = mpz(n)
    m = mpz(1)
    while x>mpfr(10):
        x = div(x, mpfr(10))
        m = div(x, mpfr(10))
    for i in range(n):
        out = add(out, div(pow(x, i), fact(i)))
    return pow(out, m)