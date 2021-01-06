import numpy as np
import pandas as pd

def generateBvc(minL,maxL,nov):

    bvcArray = [[]]
    csvTable= pd.DataFrame()

    tmp = []
    for i in range(0, len(minL)):
        tmp.append(minL[i])
    bvcArray.insert(0,tmp)
    tmp=[]
    for i in range(0, len(minL)):
        tmp.append(minL[i]+1)
    bvcArray.insert(1, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(maxL[i])
    bvcArray.insert(2, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(maxL[i]-1)
    bvcArray.insert(3, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(np.math.ceil((maxL[i] + (minL[i] - 1)) / 2))
    bvcArray.insert(4, tmp)

    tmp2=[]
    tl = list(range(1,4*nov+2))

    for i in range(0,nov):
        tmp=[]
        nom = bvcArray[4][i]
        tmp2.append(nom)

        for j in range(0,4*(nov-1)):
            tmp.append(nom)
        for j in range(0,4):
            tmp.insert((i*4)+j,bvcArray[j][i])

        csvTable[chr(97+i)] = tmp

    csvTable.loc[len(csvTable)]= tmp2
    csvTable.insert(0, 'Test Case Id', tl)
    csvTable['Expected Output']=''
    #print(csvTable)
    csvTable.to_csv('BVC.csv', index=False)