import numpy as np
import matplotlib.pyplot as plt
file_name = "pref/pref.crd"
rfp = open(file_name, "r",encoding="utf-8")
N, tmp = rfp.readline().rstrip().split()
N = int(N)
X = np.zeros(N)
Y = np.zeros(N)
for i, row in enumerate(rfp):
    lat, lng = row.rstrip().split()
    X[i] = float(lng)
    Y[i] = float(lat)
rfp.close()

file_name = "pref/pref.linklist"
rfp = open(file_name, "r",encoding="utf-8")
N, M = rfp.readline().rstrip().split()
N = int(N); M = int(M)
linklist = []
fromlist = []
tolist   = []
for row in rfp:
    f, t = row.rstrip().split()
    f = int(f)-1
    t = int(t)-1
    linklist.append((f,t)); fromlist.append(f); tolist.append(t)
    linklist.append((t,f)); fromlist.append(t); tolist.append(f)
rfp.close()

file_name = "pref/pref.node"
rfp = open(file_name, "r",encoding="utf-8")
names = [""]*N
for i in range(N):
    itmp, name = rfp.readline().rstrip().split("\t")
    names[i] = name
rfp.close()

adj_nodes = [[] for _ in range(N)]
for (f,t) in linklist: adj_nodes[f].append(t)
# デフォルト値の設定
plt.rcParams['figure.figsize'] = 20,16
plt.rcParams['figure.dpi'] = 100
plt.rcParams["font.size"] = 20
plt.rcParams['font.family'] = 'IPAPGothic'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.grid'] = False

fig = plt.figure()
plt.plot([X[fromlist],X[tolist]], [Y[fromlist],Y[tolist]], color="grey", zorder=1)
plt.scatter(X, Y, s=100, color="grey", marker="o", zorder=2)
for i in range(N): plt.text(X[i], Y[i], str(i)+names[i][names[i].find("・")+1:], fontname="IPAPGothic", fontsize=20)

print(N,M)
# ノード間距離の計算（幅優先探索）
def calc_distance(src):
    queue = []
    dist = np.ones(N)*-1
    sim  = np.ones(N)
    d = 0
    dist[src] = d
    queue.append(src)

    h1 = 0; h2 = 1
    while True:
        d += 1
        h1 = 0; h2 = len(queue)
        for h in range(h1, h2):
            node = queue.pop(0)
            for adj_node in adj_nodes[node]:
                if dist[adj_node] != -1: continue
                dist[adj_node] = d
                sim[adj_node] = 1.0/(1.0+d)
                queue.append(adj_node)
        if len(queue) == 0: break
    return sim

simM = np.ones((N,N))*-1  # 類似度行列
for src in range(N): simM[src] = calc_distance(src)
print(simM)
# 反復解法
def calc_members(clsV):
    K = max(clsV.values())+1
    members = [[] for k in range(K)]
    for k in range(K):
        members[k] = [idx for idx,v in clsV.items() if v == k]
    return members

def select_pivots(members, simM):
    K = len(members)
    P = [-1]*K
    for k in range(K):
        max_sum = -1
        for i in members[k]:
            sum_sim = -simM[i,i]
            for j in members[k]: sum_sim += simM[i,j]
            if max_sum < sum_sim:
                max_sum = sum_sim
                arg_max = i
        P[k] = arg_max
    return P

def assign_clusters(P, simM):
    K = len(P)
    N = len(simM)
    clsV = {i:-1 for i in range(N)}
    obj_func_val = 0.0
    for i in range(N):
        max_sim = -1
        for k in range(K):
            pivot = P[k]
            if max_sim < simM[i,pivot]:
                max_sim = simM[i,pivot]
                clsV[i] = k
        obj_func_val += max_sim
    return clsV, obj_func_val


from random import sample, randint
K = 5
_P = sample(range(N), K)

itr = 0
while True:
    clsV, ofv = assign_clusters(_P, simM)
    print(f"{ofv:.6f}",_P)
    members = calc_members(clsV)
    P = select_pivots(members, simM)
    if P == _P: break
    _P = P
    itr += 1
# 貪欲解法
def calc_members(clsV):
    K = max(clsV.values())+1
    members = [[] for k in range(K)]
    for k in range(K):
        members[k] = [idx for idx,v in clsV.items() if v == k]
    return members

def select_pivots(P, simM, muV):
    N = len(simM)
    K = len(P)
    max_mg = -1.0
    cnt = 0
    for i in range(N):
        mg = 0.0
        for j in range(N):
            if j == i or j in P: continue
            rho = simM[i,j]
            mu  = muV[j]
            mg += rho-mu if rho > mu else 0  # Marginal gain
        if max_mg < mg:
            max_mg = mg
            arg_max = i
        cnt += 1
    print(max_mg)
    obj_func_val = 0.0
    for j in range(N):
        if muV[j] < simM[arg_max,j]:
            muV[j] = simM[arg_max,j]
            clsV[j] = K
        obj_func_val += muV[j]
    return clsV, muV, obj_func_val, arg_max

print("start")
K = 47
P = [12,26]
clsV = {i:-1 for i in range(N)}
muV = np.zeros(N)
for k in range(K):
    clsV, muV, ofv, pivot = select_pivots(P, simM, muV)
    P.append(pivot)
    print(f"{ofv:.6f}",P)
    # members = calc_members(clsV)