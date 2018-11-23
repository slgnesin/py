import numpy as np
from matplotlib import pyplot as plt

def preprocess(data,tag):
    if tag=='minmax':
        return np.divide(data-np.min(data),np.max(data)-np.min(data))
    elif tag=='zscore':
        return np.divide(i-np.mean(data),np.std(data))
    elif tag=='rmvmean':
        return data-np.mean(data)

def descriptive(data,xLabel,yLabel):
    str=''
    str+='\n'+"Minimum : %f" % np.min(data)
    str+='\n'+"Maximum : %f" % np.max(data)
    str+='\n'+"Mean : %f" % np.mean(data)
    str+='\n'+"Median : %f" % np.median(data)
    str+='\n'+"Variance : %f" % np.var(data)
    str+='\n'+"Standard Deviation : %f" % np.std(data)
    s=pd.Series(data)
    str+='\n'+"Skewness : %f" % s.skew()
    str+='\n'+"Kurtosis : %f" % s.kurt()
    plt.hist(data,bins=100)
    plt.text(xLabel,yLabel,str)
    plt.show()

def distance(value1,value2,tag,data=None,p=None):
    '''
    默认行为样本，列为特征
    '''
    if tag=='euclidean':
        return np.sqrt(np.sum(np.power(value1-value2,2)))
        #return np.linalg.norm(data[v1]-data[v2])
    elif tag=='seuclidean':#标准欧氏距离，先对数据标准化，然后再用普通欧氏距离计算
        mean=np.array([np.mean(data.T[i]) for i in range(len(data.T))])
        mean=np.reshape(mean,(1,len(mean)))
        stdev=np.array([np.std(data.T[i]) for i in range(len(data.T))])
        stdev=np.reshape(stdev,(1,len(stdev)))
        sdata=(data-mean)/stdev
        return np.sqrt(np.sum(np.power(sdata[value1]-sdata[value2],2)))
    elif tag=='mahalanobis':
        '''
        1.求协方差矩阵s及其逆矩阵si
        2.求两个样本的差diff
        3.求diff和si的点积tmp1，求tmp和diff.T的点积tmp2
        4.求tmp2平方根
        '''
        s=np.cov(data.T)
        si=np.linalg.inv(s)
        diff=data[value1]-data[value2]
        result=np.sqrt(np.dot(np.dot(diff,si),diff.T))
        return result
    elif tag=='manhattan':
        return np.sum(np.abs(value1-value2))
    elif tag=='chebyshev':
        return np.max(np.abs(value1-value2))
    elif tag=='minkowski':
        return np.power(np.sum(np.power(np.abs(value1-value2),p)),1/p)
    elif tag=='hamming':
        return None
    else:
        return None

def similarity(value1,value2,tag,data=None):
    if tag=='cosine':
        return np.sum(np.multiply(value1,value2))/(np.sqrt(np.sum(np.power(value1,2)))+np.sum(np.power(value2,2)))
    elif tag=='pearon':
        return None
    elif tag=='jaccard':
        return None
    elif tag=='tanimoto':
        return None
    else:
        return None
