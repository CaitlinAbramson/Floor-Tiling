# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:35:03 2019

@author: Caitlin Abramson
"""

from floor_tiling import FloorTiling

w = 19
h = 8
main_solution = [[0 for i in range(w)] for j in range(h)]
ft = FloorTiling()
order_main = ft.tile(main_solution)
print(order_main)