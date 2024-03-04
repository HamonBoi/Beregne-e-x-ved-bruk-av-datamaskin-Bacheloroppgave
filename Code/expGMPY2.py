import gmpy2 as g


def exp(x, n=50, precision = 53):
    g.get_context().precision = precision
    n = g.mpz(n)
    if x < 0:
        l = 1
        x = g.mpfr(-x)
    else:
        l = 0
        x = g.mpfr(x)
    m = g.mpz(0)
    while x > 1:
        x = g.div(x, g.mpfr(2))
        m = g.add(m, 1)
    sum = g.add(g.mpfr(1), g.div(x, n))
    for i in range(n, 0, -1):
        sum = g.mul(sum, g.div(x, g.mpfr(i)))
        sum = g.add(g.mpfr(1), sum)
    for i in range(m):
        sum = g.mul(sum, sum)
    return sum
