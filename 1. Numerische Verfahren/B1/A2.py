from math import sqrt, log, exp, sin, pi, e

f = lambda x, y: x**2 - y

print(f(2,1))

f = lambda x: 0 if x < 0 else (x if 0 <= x <= 2 else 2)
print(f(4))