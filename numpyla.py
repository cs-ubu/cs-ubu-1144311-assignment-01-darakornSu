import numpy as np
import csv
#import numpy.linalg as linalg
#A = np.array(
#   [
#      [4.0, -2.0, 1.0],
#        [-2.0, 4.0, -2.0],
#        [1.0, -2.0, 3.0]
#   ]
#)
#b = np.array([1.0, 4.0, 2.0])
#print(np.dot(A, b))

#1.read matrix A from 'A.csv'
f = open('A.csv', 'r')
A = []
for line in f.readlines():
    A.append( [float(x) for x in line.strip().split(',')])
print(A)
f.close() 

#2.read matrix b from 'b.csv
def csv2mat(filename):
    return np.array(list(csv.reader(open(filename, "rt"),delimiter=",")))
A = csv2mat('A.csv')
b = csv2mat('b.csv')
print(A)
print(b)

#3
def matmul(A, b):
    m, n = len(A), len(b[0])
    J = len(A[0])
    if len(A[0])== len(b):
        #C = [ [0]*n for i in range(m)]
        C = [ [0]*n]*m
        for r in range(m):
            for c in range(n):
                C[r][c] = sum([float(A[c][j])*float(b[j][c]) for j in range(J) ])
        return C
    return [] #ไม่สามารถคูณได้

#4.print C
print(matmul(A,b))
#5.test
A = [
    [1,2,3,4],
    [2,1,3,4],
    []
]