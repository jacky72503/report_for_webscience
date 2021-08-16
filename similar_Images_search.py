#search csd image by manhattan distance
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image  as img

file_name = "C:/Users/jacky72503/PycharmProjects/report/flag/flag_CSD.dat"
rfp = open(file_name, "r",encoding="utf-8")
N, H = rfp.readline().rstrip().split()
N = int(N)
H = int(H)
x = np.zeros((N,H))

for i, row in enumerate(rfp):
    tmp = row.rstrip().split()
    for j, t in enumerate(tmp): x[i,j] = float(t)
rfp.close()

file_name = "C:/Users/jacky72503/PycharmProjects/report/flag/flag_list.txt"
codes = ['']*N;  names = ['']*N;
rfp = open(file_name, "r",encoding="utf-8")
for i, row in enumerate(rfp):
    img_id, info = row.rstrip().split("\t")
    img_code, img_name = info.split()
    codes[i] = img_code
    names[i] = img_name
plt.imshow(img.imread(f"C:/Users/jacky72503/PycharmProjects/report/flag/png/jp.png"))

def l1_distance(vec1, vec2):
    if len(vec1) != len(vec2): return -1
    v = 0.0
    for v1, v2 in zip(vec1,vec2): v += abs(v1-v2)
    return v

plt.figure(figsize=(10,10))

def find_sub_max(arr, n):
    arr_ = 0
    for i in range(n-1):
        arr_ = arr
        arr_[np.argmax(arr_)] = np.min(arr)
        arr = arr_
    return np.max(arr_)
    #print("# arr中最大的數為{}，位於第{}位".format(np.max(arr_), np.argmax(arr_)+1))

def get_dist_rank(a,b):
    dist=np.zeros(len(b))
    for i in range(len(b)):
        if i == a: continue
        dist[i] = l1_distance(b[a], b[i])
    return dist

dist_rank = get_dist_rank(76,x)
min1 = np.where(dist_rank == np.sort(dist_rank)[1])[0]+1
min2 = np.where(dist_rank == np.sort(dist_rank)[2])[0]+1
min3 = np.where(dist_rank == np.sort(dist_rank)[3])[0]+1
print(codes[111],names[111])
print(codes[143],names[143])
print(codes[46],names[46])
print()
dist_rank = get_dist_rank(7,x)
min1 = np.where(dist_rank == np.sort(dist_rank)[1])[0]+1
min2 = np.where(dist_rank == np.sort(dist_rank)[2])[0]+1
min3 = np.where(dist_rank == np.sort(dist_rank)[3])[0]+1
print(codes[int(min1)],names[int(min1)])
print(codes[int(min2)],names[int(min2)])
print(codes[int(min3)],names[int(min3)])
print()
dist_rank = get_dist_rank(86,x)
min1 = np.where(dist_rank == np.sort(dist_rank)[1])[0]+1
min2 = np.where(dist_rank == np.sort(dist_rank)[2])[0]+1
min3 = np.where(dist_rank == np.sort(dist_rank)[3])[0]+1
print(codes[int(min1)],names[int(min1)])
print(codes[int(min2)],names[int(min2)])
print(codes[int(min3)],names[int(min3)])
print()
dist_rank = get_dist_rank(33,x)
min1 = np.where(dist_rank == np.sort(dist_rank)[1])[0]+1
min2 = np.where(dist_rank == np.sort(dist_rank)[2])[0]+1
min3 = np.where(dist_rank == np.sort(dist_rank)[3])[0]+1
print(codes[int(min1)],names[int(min1)])
print(codes[int(min2)],names[int(min2)])
print(codes[int(min3)],names[int(min3)])
print()

#print(find_sub_max(dist_rank,1),find_sub_max(dist_rank,2),find_sub_max(dist_rank,3),find_sub_max(dist_rank,4))
# for i in range(N):
#     min_dist = 100000000;
#     #plt.subplot(4,2,i*2+1)
#     #plt.imshow(img.imread(f"C:/Users/jacky72503/PycharmProjects/report/flag/png/{codes[i]}.png"))
#     for j in range(N):
#         if i == j: continue
#         dist = l1_distance(x[i], x[j])
#         if min_dist > dist:
#             min_dist = dist
#             arg_min  = j
#     #plt.subplot(4,2,i*2+2)
    #plt.imshow(img.imread(f"C:/Users/jacky72503/PycharmProjects/report/flag/png/{codes[arg_min]}.png"))