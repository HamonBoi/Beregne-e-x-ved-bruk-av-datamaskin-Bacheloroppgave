def pow(a, b):
    out = 1
    for i in range(b):
        out = out*a
    return out

def fact(n):
    out = 1
    if n==0 or n==1:
        return out
    for i in range(1, n+1):
        out = out * i
    return out

def exp(x, n=18):
    out = 0
    for i in range(n):
        out = out + pow(x, i)/fact(i)
    return out

def exp2(x, n=18):
    out = 0
    m = 1
    s = 0
    if x<0:
        x = -x
        s = 1
    while x>1:
        x = x/2
        m = m*2
    for i in range(n):
        out = out + pow(x, i)/fact(i)
    if s:
        return 1/pow(out, m)
    else:
        return pow(out, m)

def exp3(x, n=18):
    out = 1
    m = 0
    s = 0
    if x<0:
        x = -x
        s = 1
    while x>1:
        x = x/2
        m = m+1
    for i in range(n, 0, -1):
        out = 1 + out*x/i
    for i in range(m):
        out = out*out
    if s:
        out = 1/out
    return out
        