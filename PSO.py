import numpy as np
import random as rd

# min y = X1 * X1 + X2 * X2
# X1 >= -10
# X2 <= 10

def update(location,speed,pBest,gBest):      #更新粒子群的位置和速度
    for i in range(len(location)):
        for j in range(len(speed[0])):
            speed[i][j] = 0.5 * speed[i][j] + 2.0 * rd.random() * (pBest[i][j] - location[i][j]) + 2.0 * rd.random() * (gBest[j] - location[i][j])
            location[i][j] += speed[i][j]
            if location[i][j] < -10:
                location[i][j] = -10
            if location[i][j] > 10:
                location[i][j] = 10

def objFunction(X1,X2):                    #计算目标函数值
    f = X1 ** 2 + X2 ** 2
    return f

def assess(location,pBest,gBest):         #更新粒子的历史最优与全局最优
    for i in range(len(location)):
        if objFunction(location[i][0],location[i][1]) < objFunction(pBest[i][0],pBest[i][1]):
            pBest[i][0] = location[i][0]
            pBest[i][1] = location[i][1]
    for i in range(len(pBest)):
        if objFunction(pBest[i][0],pBest[i][1]) < objFunction(gBest[0],gBest[1]):
            gBest[0] = pBest[i][0]
            gBest[1] = pBest[i][1]

def init():                              #随机初始化5个粒子的位置和速度
    location,speed= [],[]
    for i in range(5):
        X1 = rd.uniform(-10, 10)
        X2 = rd.uniform(-10,10)
        V1 = rd.uniform(-5,5)
        V2 = rd.uniform(-5,5)
        location.append([X1,X2])
        speed.append([V1,V2])
    return location,speed

if __name__ == '__main__':
    location,speed = init()
    pBest = location
    min = float("inf")
    gBest = [0,0]
    iters = 10000              #迭代次数
    for i in range(len(pBest)):
        if objFunction(pBest[i][0],pBest[i][1]) < min :
            min = objFunction(pBest[i][0],pBest[i][1])
            gBest[0] = pBest[i][0]
            gBest[1] = pBest[i][1]
    for i in range(iters):
        update(location, speed, pBest, gBest)
        assess(location, pBest, gBest)
    print("最优解：" + str(gBest))
    print("目标函数最优值：" + str(objFunction(gBest[0],gBest[1])))