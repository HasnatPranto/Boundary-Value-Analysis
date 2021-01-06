import numpy as np
import pandas as pd

def generateWorstTesting(minL,maxL,nov):

    worstArray = [[]]
    csvTable= pd.DataFrame()

    tmp = []
    for i in range(0, len(minL)):
        tmp.append(minL[i])
    worstArray.insert(0,tmp)
    tmp=[]
    for i in range(0, len(minL)):
        tmp.append(minL[i]+1)
    worstArray.insert(1, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(maxL[i])
    worstArray.insert(2, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(maxL[i]-1)
    worstArray.insert(3, tmp)
    tmp=[]
    for i in range(0, len(maxL)):
        tmp.append(np.math.ceil((maxL[i] + (minL[i] - 1)) / 2))
    worstArray.insert(4, tmp)

    tl = list(range(1,pow(5,nov)+1))

    for i in range(0,nov):
        tmp=[]
        while len(tmp)<pow(5,nov):
            for j in range(0,5):
                for k in range(0,pow(5,nov-(i+1))):
                    tmp.append(worstArray[j][i])

        csvTable[chr(97+i)] = tmp

    csvTable.insert(0, 'Test Case Id', tl)
    csvTable['Expected Output']=''
    #print(csvTable)
    csvTable.to_csv('worst.csv', index=False)
