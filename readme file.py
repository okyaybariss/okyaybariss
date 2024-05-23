# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:06:25 2024

@author: okyaybariss
"""
with open (r"myfile.txt", "r") as readmefile:
    okuyucu=readmefile.readline()
    print(okuyucu, end="")
    okuyucu=readmefile.readline()    
    print(okuyucu, end="")
    okuyucu=readmefile.readline()
    print(okuyucu, end="")
    okuyucu=readmefile.readline()
    print(okuyucu, end="")
    with open (r"myfile.txt", "w") as write_the_file:
        for line in readmefile:
            write_the_file.write(line)
            
        
    
    

