#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Use exhaustive enumeration to compute integer cube root, if it exists, of an
# integer
#
# Problem source: MITx 6.00.1x
#
# Created on Tue Jun 30 20:16:54 2020 by Yi-Jen Chen

x = int(input('Enter an integer: '))
sgn = -1 if x < 0 else 1

g = 0
while g**3 < sgn*x:
    g += 1
    
if g**3 != sgn*x:
    print(f'{x} is not a perfect cube')
else:
    print(f'Cube root of {x} is {sgn*g}')