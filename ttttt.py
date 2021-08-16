import numpy as np
import matplotlib.pyplot as plt
import copy

def corr(vec1, vec2):
    v1 = copy.copy(vec1); v2 = copy.copy(vec2);
    if len(v1) != len(v2): return None
    v1 -= np.average(v1)
    v1 /= np.linalg.norm(v1, ord=2)
    v2 -= np.average(v2)
    v2 /= np.linalg.norm(v2, ord=2)
    return v1.dot(v2)
file_name = "C:/Users/jacky72503/PycharmProjects/report/mannga2014/userlist.txt"
rfp = open(file_name, "r",encoding="utf-8")
users = []
for row in rfp:
    uid, info, url = row.rstrip().split("\t")
    users.append(info)
rfp.close()
num_of_users = len(users)

file_name = "C:/Users/jacky72503/PycharmProjects/report/mannga2014/itemlist.txt"
rfp = open(file_name, "r",encoding="utf-8")
items = []
for row in rfp:
    iid, info, url = row.rstrip().split("\t")
    items.append(info)
rfp.close()
num_of_items = len(items)

R = np.zeros((num_of_users, num_of_items))
file_name = "C:/Users/jacky72503/PycharmProjects/report/mannga2014/reviewlist.txt"
rfp = open(file_name, "r",encoding="utf-8")
num_of_reviews = 0
reviews = []
for row in rfp:
    uid, iid, score, unixtime = row.rstrip().split("\t")
    R[int(uid)-1, int(iid)-1] = int(score)
    reviews.append((int(uid)-1,int(iid)-1))
    num_of_reviews += 1
rfp.close()
print(f"#users:{num_of_users}  #items:{num_of_items}  #reviews:{num_of_reviews}/{num_of_users*num_of_items} (={num_of_reviews/(num_of_users*num_of_items)*100:.2f}%)")

review_items = [[] for _ in range(num_of_users)]
print(R)
review_dist = {}
for uid, revs in enumerate(R):
    review_items[uid] = set(np.where(revs > 0)[0])
    num = len(review_items[uid])
    review_dist.setdefault(num, )
    try:    review_dist[num] += 1
    except: review_dist[num] = 1
print(R.shape)

plt.rcParams['figure.figsize'] = 10,8
plt.rcParams['figure.dpi'] = 100
plt.rcParams["font.size"] = 20
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.grid'] = True

plt.scatter(review_dist.keys(), review_dist.values(), s=100, color="orange", marker="*")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("#reviews")
plt.ylabel("#users")
# plt.show()

review_users = [[] for _ in range(num_of_items)]
review_dist = {}
for iid, revs in enumerate(R.T):
    review_users[iid] = np.where(revs > 0)[0]
    num = len(review_users[iid])
    review_dist.setdefault(num, )
    try:    review_dist[num] += 1
    except: review_dist[num] = 1

plt.rcParams['figure.figsize'] = 10,8
plt.rcParams['figure.dpi'] = 100
plt.rcParams["font.size"] = 20
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.grid'] = True

plt.scatter(review_dist.keys(), review_dist.values(), s=100, color="purple", marker="*")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("#reviews")
plt.ylabel("#items")
# plt.show()

def nmf_predict(R, k,result):
    W = np.abs(np.random.uniform(low=np.min(R), high=np.max(R), size=(num_of_users, k)))
    H = np.abs(np.random.uniform(low=np.min(R), high=np.max(R), size=(num_of_items, k)))
    for itr in range(1000):
        W = W * ((R@H)   / (W@H.T@H))
        H = H * ((R.T@W) / (H@W.T@W))
        if itr%100 == 0:
            print(itr)
            print(type(int(np.where(k)[0][0])), 10 - (1000 - itr) % 100)
            err = 0
            for (uid,iid) in reviews:
                diff = R[uid,iid]-np.dot(W[uid,:], H[iid,:])
                err += diff*diff
            result[np.where(k)[0][0]][10-(1000-itr)%100] = np.sqrt(err/num_of_reviews)
            print(f"誤差：{np.sqrt(err/num_of_reviews)}")
    return W, H,result

k = np.array([10,100,200,300,400,500,600])
result=np.array((len(k),10))
for i in k:
    print("K=",i)
    W, H ,result= nmf_predict(R, i,result)
print(result)
R_predicted = W@H.T

