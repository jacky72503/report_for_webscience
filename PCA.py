import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

Colors = ["#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff", "#ffA500", "#800000", "#008000",
          "#000080", "#808000", "#800080", "#008080", "#808080", "#ffa2a2", "#a2ffa2", "#a2a2ff", "#400000", "#004000",
          "#000040", "#404000", "#400040", "#004040", "#404040"]
## 体力測定データの読み込み
file_name = r'C:\Users\jacky72503\PycharmProjects\report_for_webscience\mnist\mnist1000.dat'
rfp = open(file_name, "r")
tmp = rfp.readline().rstrip().split()
N = int(tmp[0])  # 生徒数＝オブジェクト数
H = int(tmp[1])  # 属性数＝次元数
X = np.zeros((N, H))
for i, row in enumerate(rfp):
    tmp = row.rstrip().split(" ")
    for j, val in enumerate(tmp):
        X[i, j] = float(val)
rfp.close()

# 性別ラベルの読み込み
file_name = r'C:\Users\jacky72503\PycharmProjects\report_for_webscience\mnist\mnist1000.cls'
rfp = open(file_name, "r")
types = [''] * N
for i, row in enumerate(rfp): types[i] = int(row.rstrip())
rfp.close()

print(f"#オブジェクト数:{N}  #次元数:{H}")

## データ行列を平均が0になるように平行移動
avg_scores = [np.average(x) for x in X.T]
print(avg_scores)
X = X-avg_scores
result = [np.average(x) for x in X.T] # 平均スコアを引いた行列の平均が0になっているか確認
print(result)

C = (1.0/N)*X.T@X # 分散共分散行列
eig_val, P = np.linalg.eig(C)

print(f"最大固有値：{eig_val[0]}") # 固有値 λ
print(f"最大固有ベクトル：{P[:,0]}") # 固有ベクトル p
print("-"*10)
print(f"第２固有値：{eig_val[1]}") # 固有値 λ
print(f"第２固有ベクトル：{P[:,1]}") # 固有ベクトル p

## データ行列を最大固有ベクトルと第２固有ベクトルに射影
y0 = X@P[:,0]
y1 = X@P[:,1]

# デフォルト値の設定
plt.rcParams['figure.figsize'] = 10,7
plt.rcParams['figure.dpi'] = 100
plt.rcParams["font.size"] = 20
plt.rcParams['font.family'] = 'IPAPGothic'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.grid'] = True
for i in range(N):
    if types[i] == 1: plt.scatter(y0[i], y1[i], color="blue")
    else: plt.scatter(y0[i], y1[i], color="red")
plt.show()

print(f"最大固有ベクトルへ射影後の分散：{np.var(y0)}")
print(f"第２固有ベクトルへ射影後の分散：{np.var(y1)}")

## 他の等価な解法（その１）
U, sng_val, V = np.linalg.svd(X, full_matrices=True)
y0 = sng_val[0]*U[:,0]
y1 = sng_val[1]*U[:,1]
for i in range(N):
    if types[i] == 1: plt.scatter(y0[i], y1[i], color="blue")
    else: plt.scatter(y0[i], y1[i], color="red")
plt.show()