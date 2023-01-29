#!/usr/bin/env python3
import os
sum = 0
for i in range(1, 101):
    f = open(str(i)+'.txt', 'r')
    frac = float(f.read())
    f.close()
    os.remove(str(i)+'.txt')
    sum = sum + frac
sum = sum/100
f = open('result2.txt', 'w')
f.write(str(sum))
f.close()
