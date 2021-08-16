import matplotlib.pyplot as plt
import numpy as np
file_name = r'C:\Users\jacky72503\PycharmProjects\report_for_webscience\tweet2012\goodmorning.txt'
rfp = open(file_name, "r")
time_stamps = []
time_names  = []
for row in rfp:
    utime, dtime = row.rstrip().split("\t")
    time_stamps.append(int(utime))
    d, t = dtime.split()
    time_names.append(t)
rfp.close()
T = len(time_stamps)
min_ut = min(time_stamps)
print(f"T: {T}\tmin: {min_ut}")
## 1時間ごとに集計
count_hour = [0]*24
for ut in time_stamps: count_hour[(ut-min_ut)//3600] += 1

## 1分ごとに集計
count_minute = [0]*1440
for ut in time_stamps: count_minute[(ut-min_ut)//60] += 1

## 1秒ごとに集計
count_second = [0]*86400
for ut in time_stamps: count_second[ut-min_ut] += 1
# デフォルト値の設定
plt.rcParams['figure.figsize'] = 20,20
plt.rcParams['figure.dpi'] = 100
plt.rcParams["font.size"] = 20
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.grid'] = True

# plt.subplot(3,1,1)
# plt.plot(count_hour, color="red")
# plt.xlabel('Time (hour)')
# plt.ylabel('#tweets')
# plt.minorticks_on()
# plt.tick_params(axis="both", which="major", direction="in", length=7, width=2, top="on", right="on")
# plt.tick_params(axis="both", which="minor", direction="in", length=4, width=1, top="on", right="on")

plt.subplot(3,1,2)
plt.plot(count_minute, color="green")
tick = list(np.arange(0,1440,60))*24

plt.xticks(tick, np.arange(0,24,1))
plt.xlabel('Time (min.)')
plt.ylabel('#tweets')
plt.minorticks_on()
plt.tick_params(axis="both", which="major", direction="in", length=7, width=2, top="on", right="on")
plt.tick_params(axis="both", which="minor", direction="in", length=4, width=1, top="on", right="on")

# plt.subplot(3,1,3)
# plt.plot(count_second, color="blue")
# plt.xticks(list(range(0,86400,3660))*24, list(range(0,24)))
# plt.xlabel('Time (sec.)')
# plt.ylabel('#tweets')
# plt.minorticks_on()
# plt.tick_params(axis="both", which="major", direction="in", length=7, width=2, top="on", right="on")
# plt.tick_params(axis="both", which="minor", direction="in", length=4, width=1, top="on", right="on")

plt.show()