# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:30:31 2023

@author: okyaybariss
"""

import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

# DC motor parameters
R = 10.0
L = 5
K = 0.01  # Motor constant
J = 0.01  # Moment of inertia
B = 0.1   # Viscous damping coefficient

# Transfer function of the DC motor
numerator = [K]
denominator = [J, B, K**2]
system = signal.TransferFunction(numerator, denominator)

# Time vector
time, response = signal.step(system)


plt.plot(time, response)
plt.title('Step Response of DC Motor')
plt.xlabel('Time (mili scond)')
plt.ylabel('Angular Position')
plt.grid(True)
plt.show()
