#模拟退火算法解TSP问题
import numpy as np
import random as rd

def lengthCal(path,distmat):             #计算距离
    length = 0
    for i in range(len(path) - 1):
        length += distmat[path[i]][path[i + 1]]
    length += distmat[path[-1]][path[0]]
    return  length

def exchange(path,exchangeSeq):        #交换路径中的两点得到新路径
    newPath = []
    for i in range(len(path)):
        newPath.append(path[i])
    temp = newPath[exchangeSeq[0]]
    newPath[exchangeSeq[0]] = newPath[exchangeSeq[1]]
    newPath[exchangeSeq[1]] = temp
    return newPath

distmat = np.array([[0,35,29,67,60,50,66,44,72,41,48,97],
                 [35,0,34,36,28,37,55,49,78,76,70,110],
                 [29,34,0,58,41,63,79,68,103,69,78,130],
                 [67,36,58,0,26,38,61,80,87,110,100,110],
                 [60,28,41,26,0,61,78,73,103,100,96,130],
                 [50,37,63,38,61,0,16,64,50,95,81,95],
                 [66,55,79,61,78,16,0,49,34,82,68,83],
                 [44,49,68,80,73,64,49,0,35,43,30,62],
                 [72,78,103,87,103,50,34,35,0,47,32,48],
                 [41,76,69,110,100,95,82,43,47,0,26,74],
                 [48,70,78,100,96,81,68,30,32,26,0,58],
                 [97,110,130,110,130,95,83,62,48,74,58,0]])

T = 100              #初始温度
α = 0.97              #温度变化率
iters = 1000          #每个温度的迭代次数
path= [i for i in range(12)]    #随机初始化路径
rd.shuffle(path)
while T > 10:
    for i in range(iters):
        exchangeSeq = rd.sample(range(0,12),2)
        newPath = exchange(path,exchangeSeq)       #随机交换路径中的两个点
        distanceDif = lengthCal(newPath,distmat) - lengthCal(path,distmat)
        if distanceDif < 0:
            path = newPath                         #接受新的解
        else:
            if rd.random() < np.exp(- distanceDif * 10/ T):  #以概率exp(-ΔT/T)接受新的解(这里乘上10是为了以更低的概率接收更差的解)
                path = newPath
    T = α * T
print("满意解为")
print(path)
print("距离为")
print(lengthCal(path,distmat))