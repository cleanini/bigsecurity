import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':
	sDataFile = '../data/countryCorrelation.stat'
	fData = open(sDataFile, 'r')

	countryList = []

	while True:
		line = fData.readline()
		if not line:
			break

		tmpList = line.split()

		strTmp = ' '.join(tmpList[1:])
		tupleStat = ast.literal_eval(strTmp)

		if cmp(tmpList[0], 'None') == 0:
			continue

		countryList.append([tmpList[0], tupleStat])

	countryList.sort(key=lambda country: country[1][2], reverse = True)

	#for country in countryList:
	#	print country

	XList = []
	YList = []
	errList = []

	N = 20
	numIndex = 0

	while numIndex < N:
		XList.append(countryList[numIndex][0])
		tupleStat = countryList[numIndex][1]
		numSqrt = tupleStat[0]
		numSum = tupleStat[1]
		numNum = tupleStat[2]

		YList.append(float(numSum * 1.0/numNum))
		errList.append(compCI.compCI(numSqrt, numSum, numNum))

		numIndex += 1

	ind = np.arange(len(YList))
	width = 0.5 
	fig, ax = plt.subplots()
	rects = ax.bar(ind, YList, width, color='r', yerr=errList)

	plt.xlabel('Country', fontsize=24)
	plt.ylabel('Detection Ratio', fontsize=24)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)


	#print XList
	#print ind + width/2
	plt.xticks(ind+width/2, XList)

	#plt.show()

	fig.savefig('Country.png')
	plt.close(fig)

