import numpy as np
import base
import cluster

x=[]
f=open('../../data/data1.csv','r')
while True:
    lines=f.readlines(1000)
    if not lines:
        break
    for line in lines:
        x.append([float(i) for i in line.replace('\n','').split(',')])
f.close()

x=np.array(x)

res=cluster.kMeansProc(x,4,50,'seuclidean',10)
#print(res)
