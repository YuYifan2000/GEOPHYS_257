#!/usr/bin/env python3
import sys
import random
filename = sys.argv[1]
arr_id = str(filename)
random.seed(arr_id)
sum = 0.
for i in range(0, 10000):
    a = random.random()
    b = random.random()
    if a**2+b**2 <= 1:
        sum += 1

frac = sum/10000*4
f = open(filename+'.txt', 'w')
f.write(str(frac))
f.close()
