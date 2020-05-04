#遗传算法
import numpy as np
import math
import random as rd

# max y = x + 10sin(5x) + 7cos(4x)
# 0 <= x <= 10

def code (x):              #编码  用22位2进制码对x进行表示
    s = bin(round(x / 10 * 4194303))
    s = s[2:]
    for i in range(22 - len(s)):
        s = '0' + s
    return s

def f(x):                  #目标函数
    return x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)

def decode(s):              #解码
    return int(s,2) * 10 / 4194303

def fitnessEva(race):       #评估种群适应性,适应度取为每次迭代的最小值的绝对值加上目标函数值
    x = []
    for i in range(len(race)):
        x.append(f(decode(race[i])))
    minVal = abs(min(x))
    for i in range(len(x)):
        x[i] = minVal + x[i]
    return x

def choose(race):           #比例选择算子
    fitness = fitnessEva(race)
    nextRace = []
    roulette = np.array(fitness).cumsum()       #生成轮盘
    while len(nextRace) != N:
        for i in range(len(race)):
            r = rd.uniform(min(roulette),max(roulette))
            if roulette[i] >= r:
                nextRace.append(race[i])
                if len(nextRace) == N:
                    break
    return nextRace

def intersect(race):              #单点交叉算子
    pair = []
    selected = []
    for i in range(len(race)):
        if i in selected:
            continue
        selected.append(i)
        r = np.random.randint(i,len(race))
        while r in selected:
            r = np.random.randint(i, len(race))
        selected.append(r)
        pair.append([i,r])            #随机两两配对
    for i in range(len(pair)):
        interlocaition = np.random.randint(0,21)
        r = rd.random()
        if r < pc:
            exchange(race,interlocaition,pair[i])

def mutate(race):                #基本位变异算子
    for i in range(len(race)):
        r = rd.random()
        if r < pm:
            mutLocation = np.random.randint(0,22)
            if race[i][mutLocation] == '0':
                race[i] = race[i][:mutLocation] + '1' + race[i][mutLocation + 1:]
            else:
                race[i] = race[i][:mutLocation] + '0' + race[i][mutLocation + 1:]

def exchange(race,location,pairNum):          #交换两个个体的部分染色体
    # s = race[pairNum[0]]
    # race[pairNum[0]][location + 1:] = race[pairNum[1]][location + 1:]
    # race[pairNum[1]][location + 1:] = s[location + 1:]
    s1 = race[pairNum[0]][:location + 1]
    s2 = race[pairNum[0]][location + 1:]
    s3 = race[pairNum[1]][:location + 1]
    s4 = race[pairNum[1]][location + 1:]
    race[pairNum[0]] = s1 + s4
    race[pairNum[1]] = s3 + s2

if __name__ == '__main__':
    N = 50           #群体大小
    Ger = 100        #终止代数
    pc = 0.65        #杂交概率
    pm = 0.05        #变异概率
    generation = 0
    race = []
    for i in range(N):
        x = rd.uniform(0, 10)
        race.append(code(x))
    while generation < Ger:
        race = choose(race)             #选择
        intersect(race)                 #杂交
        mutate(race)                    #变异
        generation += 1
    fitness = fitnessEva(race)
    print("函数最大值为：")
    print(f(decode(race[fitness.index(max(fitness))])))