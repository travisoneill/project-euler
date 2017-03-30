from math import factorial

c = lambda n, r: factorial(n) // ( factorial(r) * factorial(n-r) )
