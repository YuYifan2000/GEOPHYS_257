#!/usr/bin/env python3
res = 0
for i in range(0,1000000):
    if i%2 == 0:
        res = res+1./(i*2+1.)
    else:
        res = res-1./(i*2+1.)
res = res*4

f=open("result1.txt","w")
f.write(str(res))
f.close()
