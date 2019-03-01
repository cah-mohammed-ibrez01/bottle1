# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:14:51 2018

@author: Maliha
"""

a = [1,2,3,5,6,7]
b = [3,2,6,5,9,10]
err = []

for (c,d) in zip(a,b):
    err.append( (c,d,abs(c-d)) )

err = sorted(err,key=lambda x: x[2])

cleaned = [(x,y) for (x,y,z) in err ]
print(cleaned[:2])