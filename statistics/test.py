import numpy as np
import base
import cluster
from cluster import KMeans

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

res=cluster.kMeansProc(x,5,20,'euclidean',10)
print(len(res))
