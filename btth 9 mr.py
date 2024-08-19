# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:15:29 2024

@author: NGUYEN DUC LOI
"""

import math
a = float(input("Nhập vào số a = "))
b = float(input("Nhập vào số b = "))
A = (math.sqrt(a) - math.sqrt(b)) / ((a ** (1/4)) - (b ** (1/4)))
B = (math.sqrt(a) + ((a * b) ** (1/4))) / ((a ** (1/4)) + (b ** (1/4)))
print("Kết quả của phép tính là: ", A - B)
