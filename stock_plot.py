import numpy as np
import matplotlib.pyplot as plt
import copy
Colors = ["#000000","#ff0000","#00ff00","#0000ff","#ffff00","#ff00ff","#00ffff","#ffA500","#800000","#008000","#000080","#808000","#800080","#008080","#808080","#ffa2a2","#a2ffa2","#a2a2ff","#400000","#004000","#000040","#404000","#400040","#004040","#404040"]
## 株価終値の読み込み
file_name = r'C:\Users\jacky72503\PycharmProjects\report_for_webscience\stock\values.txt'
rfp = open(file_name, "r",encoding="utf-8")
tmp = rfp.readline().rstrip().split()
N = int(tmp[0]) # 銘柄数
T = int(tmp[1]) # 時点数
X = np.zeros((N,T)) # 株価行列
for i, row in enumerate(rfp):
    tmp = row.rstrip().split(" ")
    for t, val in enumerate(tmp):
        X[i,t] = int(val)
rfp.close()

## 銘柄名の読み込み
file_name = r'C:\Users\jacky72503\PycharmProjects\report_for_webscience\stock\names.txt'
rfp = open(file_name, "r",encoding="utf-8")
names = ['']*N
for i, row in enumerate(rfp): names[i] = row.rstrip()
rfp.close()

## 日付の読み込み
file_name = r'C:\Users\jacky72503\PycharmProjects\report_for_webscience\stock\dates.txt'
rfp = open(file_name, "r",encoding="utf-8")
dates = ['']*T
for t, row in enumerate(rfp): dates[t] = row.rstrip()
rfp.close()
#dates = pd.DataFrame(dates)

# 業種の読み込み
file_name = r'C:\Users\jacky72503\PycharmProjects\report_for_webscience\stock\types.txt'
rfp = open(file_name, "r",encoding="utf-8")
types = ['']*N
for i, row in enumerate(rfp): types[i] = int(row.rstrip())
rfp.close()
plt.rcParams['font.sans-serif'] = ['MS Gothic']
print(f"#銘柄数:{N}  #時点数:{T}")

# 株価のプロット
# デフォルト値の設定
plt.rcParams['figure.figsize'] = 20,10
plt.rcParams['figure.dpi'] = 100
plt.rcParams["font.size"] = 20
plt.rcParams['font.family'] = 'IPAPGothic'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.grid'] = True

# fig, ax = plt.subplots()
# ax.plot(X[0,:], label=names[0], color="red")
# ax.plot(X[1,:], label=names[1], color="green")
# ax.plot(X[4,:], label=names[4], color="blue")
# ax.legend(loc='upper left', prop={"family":"MS Gothic"})
# ax.set_xlabel('Date')
# ax.set_ylabel('Value')
# ax.minorticks_on()
# ax.tick_params(axis="both", which="major", direction="in", length=7, width=2, top="on", right="on")
# ax.tick_params(axis="both", which="minor", direction="in", length=4, width=1, top="on", right="on")
# plt.show()
# def corr(vec1, vec2):
#     v1 = copy.copy(vec1); v2 = copy.copy(vec2);
#     if len(v1) != len(v2): return None
#     v1 -= np.average(v1)
#     v1 /= np.linalg.norm(v1, ord=2)
#     v2 -= np.average(v2)
#     v2 /= np.linalg.norm(v2, ord=2)
#     return v1.dot(v2)
# U = np.log(X[:,1:T-1])-np.log(X[:,0:T-2])
# R = np.zeros((N,N))
# for i in range(N):
#     for j in range(i, N):
#         R[i,j] = R[j,i] = corr(U[i,:], U[j,:])
# D = 1-R
# J = np.eye(N)-((1/N)*np.ones((N,N)))
# __eig_val, __eig_vec = np.linalg.eig(-0.5*J@(D*D)@J)  # 固有値，固有ベクトルを求める
# # 固有値の大きい順に並び替える
# idx = np.array(np.argsort(__eig_val)[::-1])
# eig_val = np.zeros(N)
# eig_vec = np.zeros((N,N))
# for i, index in enumerate(idx):
#     eig_val[i] = __eig_val[index]
#     eig_vec[i] = __eig_vec[:,index]
#
# plt.rcParams['figure.figsize'] = 20,20
# for i in range(N):
#     plt.plot(eig_val[0]*eig_vec[0,i], eig_val[1]*eig_vec[1,i], marker="o", color=Colors[types[i]])
#     plt.text(eig_val[0]*eig_vec[0,i], eig_val[1]*eig_vec[1,i], names[i], fontname="IPAPGothic", fontsize=10)
# plt.show()
plt.rcParams['figure.figsize'] = 10,30
K = 5; #変化点の数
target = 642 # 検出対象の銘柄番号
print(names[420])
Y = np.zeros(T+1);  Y[0] = 0;  Y[1:] = np.cumsum(X[target,:]) # 累積値
F = [0, T] # 変化点
Z = np.zeros(T)
M = np.zeros(K+1) # 各区間の平均値
for k in range(K):
    h = 0; s = -1; e = -1; w = -1.0
    for t in range(T-1):
        Z[t] = 0;
        if t == F[h]:  # t が区間の左端の時
            s = F[h]   # 対象区間の左端
            e = F[h+1] # 対象区間の右端
            w = (Y[e]-Y[s])*(Y[e]-Y[s])/(e-s);
            #print(f"t:{t} s:{s} e:{e} Y[s]:{Y[s]:e} Y[e]:{Y[e]:e} w:{w:e}")
            h = h+1
            continue
        x = (Y[t]-Y[s])*(Y[t]-Y[s])/(t-s);
        y = (Y[e]-Y[t])*(Y[e]-Y[t])/(e-t);
        z = x + y - w;
        #print(f"t:{t} Y[t]:{Y[t]} x:{x:e} y:{y:e} w:{w:e} z:{z:e}")
        Z[t] = z

    [valmax, argmax] = [np.max(Z), np.argmax(Z)]
    F.append(argmax);  F.sort()
    print(f"{k} {argmax} {dates[argmax]} {-0.5*T*np.log(valmax/T):e}")

    plt.subplot(K,1,k+1)
    plt.plot(X[target,:], color="gray");
    for h in range(k+2):
        M[h] = np.mean(X[target, F[h]:F[h+1]-1])
        plt.plot([F[h], F[h+1]], [M[h], M[h]], linewidth=3, color=Colors[k+1]);
    for h in range(1, k+2):
        plt.plot([F[h], F[h]], [M[h-1], M[h]], linewidth=3, color=Colors[k+1]);
plt.show()