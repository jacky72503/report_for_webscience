import numpy as np
import random
times = np.zeros(9481)

f = open('wiki/wiki.link', 'r')
node_count = int(f.readline().split()[0])
D = np.zeros((node_count,node_count))
A = np.zeros((node_count,node_count))
check = True
i = 0
degreeArray = np.zeros(9481)

while(check and i < node_count):
    input = f.readline()
    degree = int(input.split()[0])
    degreeArray[i] = degree
    for j in range(degree):
        node = int(input.split()[j+1].split(":")[0])
        A[i][node-1] = 1
    i += 1
    if(input == ""):
        check = False

count = 0
current = 0

while(count < 1000000):
    times[current] += 1
    jump = int(random.random()*degreeArray[current])+1
    cur = 0
    for i in range(len(A[current])):
        if(A[current][i] == 1):
            cur += 1
        if(cur == jump):
            current = i
            break

    #print()
    count += 1
path = 'output.txt'
f = open(path, 'w')

for i in range(node_count):
    f.write(str(i)+" "+str(int(times[i]))+"\n")

f.close()