from sklearn.ensemble import RandomForestClassifier
import numpy as np

domainlist = []
class Domain:
	def __init__(self,_name,_label, _min, _max, _numip, _ipset):
		self.name = _name
		self.label = _label
		self.ttlmin = _min
		self.ttlmax = _max
		self.numip = _numip
		self.ipset = _ipset


	def returnData(self):
		return [self.ttlmin, self.ttlmax, self.numip]

	def returnLabel(self):
		if self.label == "good":
			return 0
		else:
			return 1
		
def initData(filename):
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if line.startswith("#") or line =="":
				continue
			tokens = line.split(",")
			name = tokens[0]
			label = tokens[1]
			ttlmin = int(tokens[2])
			ttlmax = int(tokens[3])
			numIP = int(tokens[4])
			ipset = set()
			for i in range(numIP):
				ipset.add(tokens[5+i])
			domainlist.append(Domain(name,label,ttlmin,ttlmax,numIP,ipset))

def main():
	initData("baddomaininfo")
	initData("gooddomaininfo")
	featureMatrix = []
	labelList = []
	for item in domainlist:
		featureMatrix.append(item.returnData())
		labelList.append(item.returnLabel())

	clf = RandomForestClassifier(random_state=0)
	clf.fit(featureMatrix,labelList)
	print(clf.predict([[3600,10000,3]]))
	print(clf.predict([[3600,3600,2]]))
	print(clf.predict([[100,100,3]]))
	print(clf.predict([[100,100,1]]))

if __name__ == '__main__':
	main()

