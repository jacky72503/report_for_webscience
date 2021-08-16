import time
from scipy.stats import rankdata
import numpy as np
from random import randint

file_name = "C:/Users/jacky72503/PycharmProjects/report/ekimei/name_mini.txt"
rfp = open(file_name, "r")
names = []
for row in rfp:
    names.append(row.rstrip())
N = len(names)
#print(N)
def l1_distance(vec1, vec2):
    if len(vec1) != len(vec2): return -1
    v = 0.0
    for v1, v2 in zip(vec1,vec2): v += abs(v1-v2)
    return v
## レーベンシュタイン距離
def levenshtein_distance(str1, str2):
    if not str1: return len(str2)
    if not str2: return len(str1)
    if str1[0] == str2[0]: return levenshtein_distance(str1[1:], str2[1:])
    l1 = levenshtein_distance(str1,     str2[1:])
    l2 = levenshtein_distance(str1[1:], str2)
    l3 = levenshtein_distance(str1[1:], str2[1:])
    return 1 + min(l1, l2, l3)


str1 = "hachiouji"
names2 = ["hachiouji", "tachikouji", "kichijouji", "sashiougi", "ichijouji", "hachimori", "hachisu"]
i = 0
start = time.time()
for str2 in names:
    dist = levenshtein_distance(str1, str2)
    if(dist < 4): print(str1, str2, dist)

end = time.time()

print(f"{end-start:.3}秒")

