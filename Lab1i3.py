#Разложение Холецкого

import numpy as np
from math import sqrt

A = np.array([[17,3,10],[3,17,-2],[10,-2,12]],float)
x = np.array([1,3,4])
B = np.dot(A,x)

def Holecki(A):

	V = np.zeros((len(A),len(A)),float)

	for i in range(0,len(A),1):

		temp1 = 0
		temp2 = 0

		for j in range(0,i,1):
			for k in range(0,j,1):
				temp1 = temp1 + V[i,k]*V[j,k]
			V[i,j] = (A[i,j] - temp1)/V[j,j]
            
		for t in range(0,i,1):
			temp2 = temp2 + V[i,t]*V[i,t]
		V[i,i] = sqrt(A[i,i] - temp2)

	return V

C = Holecki(A)
print(C)

def sol_bottomtr(C,B):

	y = np.zeros(len(C))

	for i in range(0,len(C),1):

		temp = 0

		for j in range (0,i,1):
			temp = temp + C[i,j]*y[j]
		y[i] = (B[i] - temp)/C[i,i]

	return(y)

y = sol_bottomtr(C,B)

def sol_toptr(CT,y):

	x = np.zeros(len(CT),float)

	for i in range (len(CT),0,-1):

		temp = 0

		for j in range (i,len(CT),1):
			temp = temp + CT[i-1,j]*x[j]
		x[i-1] = (y[i-1] - temp)/CT[i-1,i-1]

	return(x)

x = sol_toptr(C.transpose(),y)
print(x)
