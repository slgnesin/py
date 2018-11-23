import numpy as np
import base

'''
K均值聚类:
1.随机分配K个重心索引
2.计算样本与各重心距离，归类
3.重新随机分配K个重心索引
4.重复第2步，直到归类结果不再发生改变
'''

class KMeans:

    def __init__(self,data,k):
        self.data=data
        self.k=k

    def initCores(self):
        indCore=np.random.randint(0,len(self.data)-1,self.k)
        cores=[]
        for i in indCore:
            cores.append(self.data[i])
        return cores

    def sort(self,cores,distTag,p):
        sortList=[]
        for i in range(len(self.data)):
            #对比样本到每个质心的距离，将距离最近的质心索引存入到sortList中
            dists=[]
            for j in range(self.k):
                dist=base.distance(self.data[i],cores[j],distTag,self.data,p)
                dists.append(dist)
            sortList.append(np.argmin(dists))
            sort=np.array(sortList)
            sort=np.reshape(sort,(len(sort),1))
        return sort

    def updateCores(self,sort):
        #重新计算sort中所有同类样本的各特征均值，将结果存入新的质心
        cores=[]
        for i in range(self.k):
            core=[]
            samples=[]
            for j in range(len(self.data)):
                if sort[j]==i:
                    samples.append(self.data[j])
            samples=np.array(samples)
            for j in range(len(samples.T)):
                core.append(np.mean(samples.T[j]))
            core=np.array(core)
            core=np.reshape(core,(1,len(self.data.T)))
            cores.append(core)
        return cores

    def silhouette(self):
        return None

def kMeansProc(data,k,times=2,distTag='euclidean',p=1):
    #分类不再发生变化，或迭代完成时结束
    clu=KMeans(data,k)
    cores=clu.initCores()
    oldSort=np.zeros((len(data),1))
    for i in range(times):
        sort=clu.sort(cores,distTag,p)
        sum=len(sort)
        for j in range(len(sort)):
            if oldSort[j]==sort[j]:
                sum-=1
        if sum==0:
            print("Iteration times : %d" % i)
            break
        oldSort=sort
        cores=clu.updateCores(sort)
    return sort
