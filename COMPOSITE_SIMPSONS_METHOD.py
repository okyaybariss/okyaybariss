
"""
Created on Thu Nov  2 23:43:58 2023

@author: okyaybariss
"""

def f(x):
    return x/(1+x)

def composite_simpsons_rule(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    integral = f(x[0]) + f(x[n])
    for i in range(1, n, 2):
        integral += 4 * f(x[i])
    for i in range(2, n-1, 2):
        integral += 2 * f(x[i])
    integral *= h / 3
    return integral

a = 1  
b = 5
n = 100

result = composite_simpsons_rule(f, a, b, n)
print(result)