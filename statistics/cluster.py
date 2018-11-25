import numpy as np
import base
import random

'''
K均值聚类:
1.随机分配K个重心索引
2.计算样本与各重心距离，归类
3.重新随机分配K个重心索引
4.重复第2步，直到归类结果不再发生改变
'''

class KMeans:

    def __init__(self,data):
        self.data=data

    def initCores(self,k):
        #生成不重复随机索引
        indCore=random.sample(range(0,len(self.data)-1),k)
        cores=[]
        for i in indCore:
            cores.append(self.data[i])
        return cores

    def sort(self,cores,k,distTag,p):
        sort=[]
        for i in range(len(self.data)):
            #对比样本到每个质心的距离，将距离最近的质心索引存入到sortList中
            dists=[]
            for j in range(k):
                dist=base.distance(self.data[i],cores[j],distTag,self.data,p)
                dists.append(dist)
            sort.append(np.argmin(dists))
        return sort

    def updateCores(self,sort,indsort):
        #重新计算sort中所有同类样本的各特征均值，将结果存入新的质心
        cores=[]
        for i in indsort:
            core=[]
            samples=[]
            for j in range(len(sort)):
                if sort[j]==i:
                    samples.append(self.data[j])
            samples=np.array(samples)
            for j in range(len(samples.T)):
                core.append(np.mean(samples.T[j]))
            core=np.array(core)
            core=np.reshape(core,(1,len(self.data.T)))
            cores.append(core)
        return cores

    #评估效果
    def silhouette(self):
        return None

def kMeansProc(data,k,times=2,distTag='euclidean',p=1):
    #分类不再发生变化，或迭代完成时结束
    clu=KMeans(data)
    cores=clu.initCores(k)
    oldSort=np.zeros((len(data),1))
    for i in range(times):
        sort=clu.sort(cores,k,distTag,p)
        #处理分类数量下降问题
        indsort=[]
        cpsort=[]
        for j in range(len(sort)):
            if sort[j] not in cpsort:
                indsort.append(sort[j])
            cpsort.append(sort[j])
        k=len(indsort)
        #检查本次分类是否和上次一致，若一致则结束迭代
        sum=len(sort)
        for j in range(len(sort)):
            if oldSort[j]==sort[j]:
                sum-=1
        if sum==0:
            print("Iteration times : %d" % i)
            break
        oldSort=sort
        cores=clu.updateCores(sort,indsort)
    return sort

class Hierarchical:
    def __init__(self,data):
        self.data=data

def hierarchicalProc(data,method):
    return None

class DBSCAN:
    def __init__(self,data):
        self.data=data
