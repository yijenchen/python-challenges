#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Use Babylonian/Heron's method to estimate square root of a non-negative
# interger
#
# Problem source: MITx 6.00.1x
#
# Created on Wed Jun 24 10:38:47 2020 by Yi-Jen Chen

import random

def sqrt_babylon(x, epsilon=0.01, max_iters=100):
    random.seed(0)
    g = random.uniform(0, x)
    num_iters = 0

    while abs(g**2 - x) >= epsilon:
        print(f'Iter {num_iters}: {g:10.5f}')
        g = (g + x/g) / 2
        num_iters += 1

        if num_iters > max_iters:
            print('-' * 50)
            print(f'Failed to find square root of {x} within {max_iters} iterations')
            break
            
    else:
        print('-' * 50)
        print(f'Approx. square root of {x}: {g:.10f} after {num_iters} interations')

sqrt_babylon(25, epsilon=1e-5)