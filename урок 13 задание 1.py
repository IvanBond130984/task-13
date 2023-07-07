import random
def vector(c,m):
    rezult=[]
    s0=m*-1
    s1=m
    for i in range(c):
        x=random.randint(s0, s1)
        rezult.append(x)
        random.seed()
    return rezult
def matrix(r,c,m):
    temp_matrix=[]
    for i in range(r):
        temp_matrix.append(vector(c, m))
    return temp_matrix
def summa_matrix(m0, m1):
    temp_matrix=[]
    temp_vector = []
    for i in range(len(m0)):
        t=len(m0[i])
        for j in range(t):
            temp_vector.append(m0[i][j]+m1[i][j])
        temp_matrix.append(temp_vector)
        temp_vector=[]
    return temp_matrix
def print_matrix(m0):
    for r in m0:
        print(*r)
print('Введите количество строк: ')
r=int(input())
print('Введите количество стобцов: ')
c=int(input())
print('Введите максимальное случайное число: ')
m=int(input())
matrix_1=matrix(r, c, m)
print('матрица 1')
print_matrix(matrix_1)
matrix_2=matrix(r, c, m)
print('матрица 2')
print_matrix(matrix_2)
print('матрица 3')
matrix_3=summa_matrix(matrix_1, matrix_2)
print_matrix(matrix_3)