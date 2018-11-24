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
sort=cluster.kMeansProc(x,2,2,'mahalanobis',10)
print(x)
print(sort)
