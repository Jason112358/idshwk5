from sklearn.ensemble import RandomForestClassifier
import numpy as np

domainlist = []
testdmlist = []
testlist = []
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

def readTest(filename):
        with open(filename) as f:
                for line in f:
                        numSum = 0
                        ltrSum = 0
                        line = line.strip()
                        if line.startswith("#") or line == "":
                                continue
                        for letter in line:
                                if letter.isdigit() == True:
                                        numSum = numSum + 1
                                elif letter != '.':
                                        ltrSum = ltrSum + 1
                        testdmlist.append(line)
                        testlist.append([numSum,ltrSum])

def main():
        tmp = 0
        initData("train.txt")
        readTest("test.txt")
        featureMatrix = []
        labelList = []
        for item in domainlist:
                featureMatrix.append(item.returnData())
                labelList.append(item.returnLabel())
        clf = RandomForestClassifier(random_state=0)
        clf.fit(featureMatrix,labelList)
        prelist = clf.predict(testlist)
        with open('result.txt','wt') as resfile:
                for each in prelist:
                    if each == 1:
                            print(testdmlist[tmp]+",dga",file = resfile)
                    else:
                            print(testdmlist[tmp]+",notdga",file = resfile)
                    tmp = tmp + 1

if __name__ == '__main__':
        main()
        print("FINISHED")
