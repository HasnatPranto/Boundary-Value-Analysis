import numpy as np
import pandas as pd

def generateRobustTesting(minL,maxL,nov):

    roboArray = [[]]
    csvTable= pd.DataFrame()

    tmp = []
    for i in range(0, len(minL)):
        tmp.append(minL[i])
    roboArray.insert(0,tmp)
    tmp=[]
    for i in range(0, len(minL)):
        tmp.append(minL[i]+1)
    roboArray.insert(1, tmp)
    tmp=[]
    for i in range(0, len(minL)):
        tmp.append(minL[i]-1)
    roboArray.insert(2, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(maxL[i])
    roboArray.insert(3, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(maxL[i]-1)
    roboArray.insert(4, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(maxL[i]+1)
    roboArray.insert(5, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(np.math.ceil((maxL[i] + (minL[i] - 1)) / 2))
    roboArray.insert(6, tmp)

    tmp2=[]
    tl = list(range(1,6*nov+2))

    for i in range(0,nov):
        tmp=[]
        nom = roboArray[6][i]
        tmp2.append(nom)

        for j in range(0,6*(nov-1)):
            tmp.append(nom)
        for j in range(0,6):
            tmp.insert((i*6)+j,roboArray[j][i])

        csvTable[chr(97+i)] = tmp

    csvTable.loc[len(csvTable)]= tmp2
    csvTable.insert(0, 'Test Case Id', tl)
    csvTable['Expected Output']=''
    #print(csvTable)
    csvTable.to_csv('robust.csv', index=False)