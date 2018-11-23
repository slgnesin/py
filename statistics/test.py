import numpy as np
import base
import cluster

x=[]
f=open('../../data/ppl8.csv','r')
while True:
    lines=f.readlines(1000)
    if not lines:
        break
    for line in lines:
        x.append([float(i) for i in line.replace('\n','').split(',')])
f.close()

x=np.array(x)
#print(np.shape(x))

sort=cluster.kMeansProc(x,4,100)
#print(x)
#print(sort)
