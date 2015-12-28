import os

__author__ = 'tusharsaurabh'


def prepareStr(name,line,char):
    lenName = len(name)
    lenLine = len(str(line))
    space1 = ''
    for x in range(50-lenName):
        space1 = space1 + ' '
    space2 = ''
    for x in range(15-lenLine):
        space2 = space2 + ' '
    return name + space1 + str(line) + space2 + str(char)  + '\n'


home = os.environ['HOME']

source = home + '/Documents/whatsAppDataAnalysisTodaysChat.txt'
destination = home + '/Documents/DataAnalysis.txt'

f=open(source,'r')
w=open(destination,'w')

listIndex = 0
dataAnalyticsList = []
dataAnalyticsDict = {}
DATE = "11/10/2015"

for line in f:

    if line[0:len(DATE)] == DATE:
        hypenPos = line.find("-")
        colonPos = line[hypenPos:].find(":")
        changedIcon = line.find("changed this group's icon")

        if changedIcon > 0:
            name = line[(hypenPos+1):(hypenPos + changedIcon )].strip(" ")
        else:
            name = line[(hypenPos+1):(hypenPos + colonPos)].strip(" ")

            found = False

            for item in dataAnalyticsList:
                if name == item["name"]:
                    dataAnalyticsDict["name"] = name
                    dataAnalyticsDict["line"] = item.get("line",0) +  1
                    dataAnalyticsDict["char"] = item.get("char",0) + len(line[(hypenPos + colonPos):].strip(" "))
                    dataAnalyticsList[dataAnalyticsList.index(item)] = dataAnalyticsDict.copy()
                    found = True

            if not found:
                dataAnalyticsDict["name"] = name
                dataAnalyticsDict["line"] = 1
                dataAnalyticsDict["char"] = len(line[(hypenPos + colonPos):].strip(" "))
                dataAnalyticsList.append(dataAnalyticsDict.copy())
    else:
        for item in dataAnalyticsList:
            if name == item["name"]:
                dataAnalyticsDict["name"] = name
                dataAnalyticsDict["line"] = item.get("line",0) +  1
                dataAnalyticsDict["char"] = item.get("char",0) + len(line[(hypenPos + colonPos):].strip(" "))
                dataAnalyticsList[dataAnalyticsList.index(item)] = dataAnalyticsDict.copy()

for item in dataAnalyticsList:
    line=prepareStr(item.get("name"),item.get("line"),item.get("char"))
    w.write(line)

w.close()
f.close()
