import gmpy2 as g

# Laster filen "optimalNs.txt" og lagrer den som en vanlig python liste
with open("optimalNs.txt", "r") as file:
    NsString = file.read()
    Ns = list(map(int, NsString.split(',')))

def exp(x, precision = 53):
    # 3 input, x for e^x, n iterasjoner i Maclaurin polynomet, precision på mpfr hvor standard er 53
    # Setter "global presisjon"
    g.get_context().precision = precision
    # Setter n til mpz basert på optimal n
    n = g.mpz(Ns[precision-53])
    # Lagres mpfr(1) på en variabel så vi slipper å definere den for ofte
    one = g.mpfr(1)
    # Sjekker om x er positiv eller negativ, hvis negativ vil den si ifra til slutten at den skal dele på svaret
    if x < 0:
        s = 1
        x = g.mpfr(-x)
    else:
        s = 0
        x = g.mpfr(x)
    # Setter opp m, som skal brukes til å "skalere" x
    m = g.mpz(0)
    # "skaleringen", hvis x er større enn 1 deler vi den på 2 til den er mindre, korreksjon skjer rundt slutten
    while x >1:
        x = g.div(x, g.mpfr(2))
        m = g.add(m, 1)
    # Setter opp for summen med å begynne på 1
    out = one
    # Horners metode, vi putter det i to linjer for å se bedre ut
    for i in range(n, 0, -1):
        out = g.mul(out, g.div(x, g.mpfr(i)))
        out = g.add(one, out)
    # Her "reskalerer" vi, får tilbake den originale størrelsen
    for i in range(m):
        out = g.square(out)
    # Sjekker om vi begynte med et positivt eller negativt tall, hvis positivt returnerer sum, hvis negativt returnerer 1/sum
    if s:
        return g.div(one, out)
    return out