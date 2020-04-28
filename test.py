from sklearn.ensemble import RandomForestClassifier
import numpy as np

domainlist = []
class Domain:
        def __init__(self,_name,_label):
                self.name = _name
                self.label = _label

        def returnData(self):
                numSum = 0
                ltrSum = 0
                for letter in self.name:
                        if letter.isdigit() == True:
                                numSum = numSum + 1
                        elif letter != '.':
                                ltrSum = ltrSum + 1
                return [numSum,ltrSum]

        def returnLabel(self):
                if self.label == "notdga":
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
                        domainlist.append(Domain(name,label))

# TODO 1:read the test.txt and output the result

def main():
        initData("train.txt")
        featureMatrix = []
        labelList = []
        for item in domainlist:
                featureMatrix.append(item.returnData())
                labelList.append(item.returnLabel())

        clf = RandomForestClassifier(random_state=0)
        clf.fit(featureMatrix,labelList)
        print(clf.predict([[6,20]]))
        print(clf.predict([[9,18]]))

if __name__ == '__main__':
        main()

