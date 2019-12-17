#Метод Гаусса с частичным выбором ведущего элемента

import numpy as np

A = np.array([[3,17,10],[2,4,-2],[6,18,-12]],float)
x = np.array([1,3,4])
B = np.dot(A,x)
piv = np.zeros(len(A)-1,float)

def gaus(x):
	x = np.array(x,float)
	return x[1:]/x[0]


def gaus_app(C, v):
	C = np.array(C, float)
	v = np.array([[v[i]] for i in range(len(v))], float)
	C[1:,:] = C[1:,:] - v*C[0,:]
	return C


def LU_part(A):

	A = np.array(A,float)

	for k in range(0,len(A)-1,1):
		piv[k] = list(A[k:,k]).index(max(A[k:,k]))
		ch = np.array(A[k,k:len(A)],float)
		A[k,k:len(A)] = A[int(piv[k]),k:len(A)]
		A[int(piv[k]),k:len(A)] = ch
		if A[k,k] != 0:
			v = gaus(A[k:,k])
		A[k+1:,k] = v
		A[k:,k+1:] = gaus_app(A[k:,k+1:],v)

	return A

def LU_solve(A,B):

    C = LU_part(A)

    print(piv)

    ch1 = np.zeros(len(A),float)

    M = []
    E = []

    for i in range (len(A)+1):
        M.append(np.identity(len(A),float))
        E.append(np.identity(len(A),float))

    for j in range(0,len(A)-1,1):
        ch1[:] = E[j][j,:]
        E[j][j,:] = E [j][int(piv[j]),:]
        E[j][int(piv[j]),:] = ch1[:]

    for k in range(1,len(A)):
        M[k-1][k:,k-1] = -np.dot(E[k],C)[k:,k-1]

    U = np.array(A,float)
    y = np.array(B,float)

    for v in range(0,len(A)-1):
        U=np.dot(M[t],np.dot(E[t],U))
        y=np.dot(M[t],np.dot(E[t],y))

    print(U)
    print(y)

    r = np.zeros(len(A),float)

    for i in range (len(A),0,-1):

        temp = 0

        for j in range (i,len(A),1):
            temp = temp + U[i-1,j]*r[j]
        r[i-1] = (y[i-1]-temp)/U[i-1,i-1]
        
    print(r)
    
LU_solve(A,B)
