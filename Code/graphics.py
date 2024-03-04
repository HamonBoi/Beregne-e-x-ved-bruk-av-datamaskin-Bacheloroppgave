import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2, 2, 1000)
y = np.zeros(1000)
p = np.zeros(1000)

for i in range(1000):
    y[i] = math.exp(x[i])

p = p + 1

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=0")
plt.show()

p = p + x

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=1")
plt.show()

p = p + x*x/2

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=2")
plt.show()

p = p + x*x*x/6

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=3")
plt.show()

p = p + x*x*x*x/24

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=4")
plt.show()

p = p + x**5/math.factorial(5)

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=5")
plt.show()

p = p + x**6/math.factorial(6)

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=6")
plt.show()

p = p + x**7/math.factorial(7)

plt.plot(x, y)
plt.plot(x, p)
plt.xlim(-2.2, 2.2)
plt.ylim(0, 8)
plt.title("n=7")
plt.show()
