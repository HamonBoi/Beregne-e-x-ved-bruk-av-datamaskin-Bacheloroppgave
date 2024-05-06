import gmpy2 as g

from expGMPY import exp


Ns = list(range(0, 1000))

N = 1
for i in range(53, 1053):
    while exp(1, n=N, precision=i)!=exp(1, n=N+10, precision=i):
        N = N+1
    else:
        Ns[i-53] = N
        


NsString = ','.join(map(str, Ns))
with open("optimalNs.txt", "w") as file:
    file.write(NsString)






