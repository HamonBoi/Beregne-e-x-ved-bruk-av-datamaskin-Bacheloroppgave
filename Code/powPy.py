def pow(a, b):
    out = 1
    for i in range(b):
        out = out*a
    return out

def pow2(a, b):
    out = 1
    if b>0:
         for i in range(b):
            out = out*a
    elif b<0:
        for i in range(-b):
            out = out/a
    return out

def fact(n):
    out = 1
    if n==0 or n==1:
        return out
    for i in range(1, n+1):
        out = out * i
    return out

def exp(x, n=50):
    out = 0
    for i in range(n):
        out += pow(x, i)/fact(i)
    return out

def exp2(x, n=50):
    out = 0
    m = 1
    while x>10:
        x = x/10
        m = m*10
    for i in range(n):
        out += pow(x, i)/fact(i)
    return pow(out, m)


def ln(x, n = 50):
    out = 0
    for i in range(1, n):
        out += pow(-1, i-1)*pow(x, i)/i
    return out

def pow3(a, x, n=50):
    out = 0
    d = ln(a)
    for i in range(n):
        out += pow(d, i)*pow(x, i)/fact(i)
    return out
    