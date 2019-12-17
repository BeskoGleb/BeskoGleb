#Метод Якоби

import numpy as np
import math
from timeit import default_timer as timer

#решение системы A x = b методом Якоби c точностью eps
def jacobi(A, b, eps):
    x = [1] * len(b)
    
    it = 0
    while True:
        xn = [0] * len(b)
        for i in range(len(x)):
            s1 = 0
            s2 = 0
            
            for j in range(i):
                s1 += A[i][j] * x[j]
            
            for j in range(i + 1, len(b)):
                s2 += A[i][j] * x[j]
            
            xn[i] = (b[i] - s1 - s2) / A[i][i]
        
        if (math.sqrt(sum([(xn[i] - x[i]) * (xn[i] - x[i]) for i in range(len(b))])) < eps):
            return xn
            
        it += 1
        if (it > 100):
            return xn
            
        x = xn

#решение системы A x = b методом Якоби c точностью eps и векторизацией
def jacobi_vec(A, b, eps):
    x = np.array([1] * len(b))
    U = np.triu(A, k = 1)
    L = np.tril(A, k = -1)
    D = np.diag(A)
    D = np.array([1 / d for d in D])
    D = np.diagflat(D)
    
    it = 0
    
    while True:
        xn = np.dot(D, b - np.dot(L + U, x))
        if (np.linalg.norm(xn - x) < eps):
            return xn
        
        it += 1
        if (it > 100):
            return xn
            
        x = xn
        

A = [[1, 0.2, 0.3], [0.3, 1, 0.06], [0.07, 0.08, 1]]
b = [1, 2, 3]

#решение
sol = jacobi(A, b, 1e-6)
print("solution", sol)
print(np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - b), ("bad!", "ok!")[np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - b) < 1e-6])

#решение и векторизация
sol = list(jacobi_vec(np.matrix(A), np.array(b), 1e-6))
print("solution", sol)
print(np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - b), ("bad!", "ok!")[np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - b) < 1e-6])

#сравнение времени работы
start = timer()
for i in range(1000):
    sol = jacobi(A, b, 1e-6)
end = timer()

cycle = end - start

start = timer()
AA = np.matrix(A)
bb = np.array(b)
for i in range(1000):
    sol = jacobi_vec(AA, bb, 1e-6)
end = timer()

vector = end - start

print("time of cycle", cycle)
print("time of vector", vector)
