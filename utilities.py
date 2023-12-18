# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:01:33 2023

@author: DELL LATITUDE
"""

import settings

def height_prcnt(percentage):
    return (settings.HEIGHT/100) * percentage

def width_prcnt(percentage):
    return (settings.WIDTH/100) * percentage

def area(x1, x2, y1, y2):
    if (x1 != x2 and y1 != y2):
        return ((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))
    elif (x1 == x2):
        return (abs(y2 - y1) + 1)
    else:
        return (abs(x2 - x1 + 1))
