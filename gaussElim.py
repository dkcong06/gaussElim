import numpy as np
import time
import matplotlib.pyplot as plt

def main():
    for i in range(20):
        timeCalc(i+1, 1000)
        ##print is here just to keep track of where the code is
        print(i+1)
    createGraph()

##creating the fuction that makes random arrays and run them
##in milliseconds
matrixSize = []
runtime = []
def timeCalc(size, reps):
    birth = time.time()
    for i in range(reps):
        randomArr1 = np.random.rand(size, size)
        randomArr2 = np.random.rand(size, 1)
        gaussElim(randomArr1, randomArr2)
    death = time.time()
    total = (death - birth) * 1000
    matrixSize.append(size)
    runtime.append(total)

##creating the graph
def createGraph():
    plt.plot(matrixSize, runtime)
    plt.xlabel("Matrix Size")
    plt.ylabel("Time in Milliseconds for 1000 Runs")
    plt.title("Matrix Size vs Time")
    plt.show()

##the function to solve the matrix using gaussElim
def gaussElim(a, b):
    n = len(a)
    augMatrix = np.column_stack((a, b))
    augMatrix = augMatrix.astype(float)

    for i in range(n):
        PivotRow = i
        max = abs(augMatrix[i][i])

        for j in range(i + 1, n):
            if abs(augMatrix[j][i]) > max:
                max = abs(augMatrix[j][i])
                PivotRow = j 
    
        if PivotRow != i:
            augMatrix[i], augMatrix[PivotRow] = augMatrix[PivotRow].copy(), augMatrix[i].copy() 

        if abs(augMatrix[i][i]) < 1989e-12:
            return("DNE")
        
        pivotVal = augMatrix[i][i]
        augMatrix[i] = augMatrix[i]/pivotVal

        for k in range(i+1, n):
            multi = augMatrix[k][i]
            augMatrix[k] = augMatrix[k] - multi*augMatrix[i]

    ##The matrix has now been converted to reduced row echolon form 
    zeros = np.zeros(n)
    for i in range(n-1, -1, -1):
        zeros[i] = augMatrix[i][-1]
        for j in range(i+1, n):
            zeros[i] = zeros[i] - augMatrix[i][j] * zeros[j]
    return zeros
    ##returns the solution

main()