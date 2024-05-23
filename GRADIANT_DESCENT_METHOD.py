# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:27:54 2023

@author: okyaybariss
"""
def gradient_descent(x, y, alpha, iterations):
    for i in range(iterations):
        df_dx = 0.52 * x - 0.48 * y
        df_dy = 0.52 * y - 0.48 * x

        x = x - alpha * df_dx
        y = y - alpha * df_dy

        f_value = 0.26 * (x**2 + y**2) - 0.48 * x * y

        print(f'Iteration {i + 1}: x = {x:.4f}, y = {y:.4f}, f(x, y) = {f_value:.4f}')

    return x, y
# Up here we are finding the values of X and Y for each iteration

# intial points
x1 = 9
y1 = 9

# (S or alpha value in our problems) This is a small positive constant that is multiplied with the gradient of the objective function concerning the parameters
alpha = 1

# number of iterations
iterations = 200

optimal_x, optimal_y = gradient_descent(x1, y1, alpha, iterations)

print("\nOptimal Point:")
print(f'x = {optimal_x:.4f}, y = {optimal_y:.4f}')
