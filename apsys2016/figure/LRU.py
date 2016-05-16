import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FixedLocator
import numpy as np

with open('./LRU.result') as f:
	lines = f.read().splitlines()

entryList = []
accurateList = []

for line in lines:
	tmp = line.split()
	accurateList.append(float(tmp[3]) * 100)
	entryList.append(int(tmp[0]))


#for i in rateList:
#	print i, accumList[i]

fig, ax = plt.subplots()
ax.plot(entryList, accurateList, 'r-x', markersize=6)


major_ticks = np.arange(0, 1001, 100) 


xmin = -1
xmax = 1001
ax.set_xlim(xmin, xmax)
#xticks = ax.xaxis.get_major_ticks()
#xticks[0].label1.set_visible(False)
ax.set_xticks(major_ticks)
plt.xlabel('The number of cache entries', fontsize=14)

ymin = 0
ymax = 101
ax.set_ylim(ymin, ymax)
plt.ylabel('Cache hit rates (%)',  fontsize=14)

ax.grid(True)
#plt.title('Cumulative frequencies')
#plt.show()
fig.savefig('LRU.pdf')
plt.close(fig)