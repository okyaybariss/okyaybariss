# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:22:24 2024

@author: okyaybariss
"""

import matplotlib.pyplot as plt

class Circle:
    
    def __init__ (self, color, radius):
        self.color=color;
        self.radius=radius;
     
        
    def add_radius(self, r):
        self.radius=self.radius+r
        return (self.radius)
    
    def plotting (self, name):
        plt.gca().add_patch(plt.Circle((0,0), fc=self.color, radius=self.radius, ))
        plt.axis('scaled')
        plt.title(name)
        plt.show()
        
        
cemberim=Circle("green", 10) 
cemberim.plotting("green Circle") 
cemberim.add_radius(100)
 