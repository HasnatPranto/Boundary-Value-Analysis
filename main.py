import bvc
import robust
import worst

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maxL=[]
    minL = []
    numberOfVariables = int(input('How Many Parameters?\n'))

    for i in range(0,numberOfVariables):
        print('Enter min & max for',i+1, 'th Parameter')
        a,b = input().split()
        maxL.append(int(b))
        minL.append(int(a))

    bvc.generateBvc(minL, maxL, numberOfVariables)
    robust.generateRobustTesting(minL,maxL,numberOfVariables)
    worst.generateWorstTesting(minL,maxL,numberOfVariables)

    print('Test cases generated!\nTest files: BVC.csv, robust.csv, worst.csv')
