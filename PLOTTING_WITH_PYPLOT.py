# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 00:10:36 2023

@author: okyaybariss
"""

import matplotlib.pyplot as plt
x= [8, 31, 69, 118, 183, 257]
y= [0.756, 0.745, 0.756, 0.74, 0.742, 0.73,]

plt.plot(x, y, 'ro', label="veri noktaları")

plt.title('Psc - Cos0')
plt.xlabel('Psc')
plt.ylabel('Cos0')
plt.legend()
plt.show()