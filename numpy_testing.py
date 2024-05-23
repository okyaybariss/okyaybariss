# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:50:49 2024

@author: okyaybariss
"""
"""
import matplotlib.pyplot as plt
import numpy as np
np.pi
x=np.linspace(0, 2*np.pi, 200)
y=np.sin(x)

plt.plot(x, y)
"""


import numpy as np
import matplotlib.pyplot as plt

a= np.array([1, 1])
b=np.array([1,0])
c=np.add(a, b)

def Plotvec1(a, b, c):
    ax = plt.axes()
    plt.plot(a, "r")
    plt.plot(b, "b")
    plt.plot(c, "g")

Plotvec1(a, b, c)    
