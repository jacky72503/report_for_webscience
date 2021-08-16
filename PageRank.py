import numpy as np
import pandas as pd

f = open('wiki/wiki.link', 'r')
node_count = int(f.readline().split()[0])
D = np.zeros((node_count,node_count))
A = np.zeros((node_count,node_count))
check = True
i = 0
origin_score = np.ones(node_count)

while(check and i < node_count):
    input = f.readline()
    degree = int(input.split()[0])
    D[i][i] = degree
    for j in range(degree):
        node = int(input.split()[j+1].split(":")[0])
        A[i][node-1] = 1
    i += 1
    if(input == ""):
        check = False

D = np.linalg.inv(D)
P=D.dot(A)
new_score = origin_score.T
d=0.15
for j in range(500):
    new_score = d/node+(1-d)*new_score.dot(P)

f = open('wiki/wiki.node', 'r', encoding="utf-8")
check = True
i = 0
node =[]
while(check and i < node_count):
    input = f.readline()
    node.append(input.split()[1])
    i += 1
    if(input == ""):
        check = False
#print(node)

for j in range(10):
    current = 0
    max = 0
    for k in range(node_count):
        if(new_score[k] > max):
            max=new_score[k]
            current=k
            new_score[k] = 0
    print(node[current]+" "+str(max))




