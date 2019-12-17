#Разностная схема для нелинейного уравнения
import math

#решаем задачу: u'' = f(x, u), u(0) = mu1, u(l) = mu2 с шагом h
def solve_diff_equ(f, l, mu1, mu2, h):
    N = int(l / h + 0.5)
    
    #разностная схема: (u[i-1] - 2 u[i] + u[i]) / h^2 == f(x[i], u[i]), u[0] = mu1, u[N] = mu2
    #нелинейное уравнение решаем итерационными методами (u[i-1][s] - 2 u[i][s] + u[i][s]) == h^2 f(x[i], u[i][s-1]), u[0] = mu1, u[N] = mu2
    
    #начальное приближение
    u = [0] * (N + 1)
    u[0] = mu1
    u[N] = mu2
    
    #счетчик итераций
    iter = 0
    while True:
        #каждый раз решаем систему методом прогонки
        xi = dict()
        th = dict()
        xi[1] = 0
        th[1] = mu1
        
        #(u[i-1][s] - 2 u[i][s] + u[i][s]) == h^2 f(x[i], u[i][s-1]), u[0] = mu1, u[N] = mu2
        #-u[i-1][s] + 2 u[i][s] - u[i][s]) == -h^2 f(x[i], u[i][s-1])
        #alpha = beta = 1, gamma = 2, phi[i] = -h^2 f(x[i], u[i][s-1])
        for i in range(1, N):
            xi[i + 1] = 1 / (2 - xi[i])
            th[i + 1] = (-h * h * f(i * h, u[i]) + th[i]) / (2 - xi[i])
        
        #новое приближение  
        new_u = [0] * (N + 1)
        
        new_u[N] = mu2
        for i in reversed(range(0, N)):
            new_u[i] = xi[i + 1] * new_u[i + 1] + th[i + 1]
        
        if sum((new_u[i] - u[i]) * (new_u[i] - u[i]) for i in range(N + 1)) < 1e-9: 
            return new_u
            
        if iter > 100: 
            return new_u
            
        iter += 1
        #новое приближение становится старым
        u = new_u.copy()

sol = solve_diff_equ(lambda xx, uu: -math.exp(uu), 1, 0, 0, 0.1)

print(sol)

for i in range(11):
    print("u(" + str(0.1 * i) + ") =", sol[i])
