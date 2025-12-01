import random
import timeit

print("alkjdf")


## PROBLEM : 1
def Matrix_Multiplication(A, B, C, n):
    for i in  range(0, n):
        for j in range(0, n):
            for k in range (0, n):
                C[i][j] = C[i][j] + (A[i][k])*(B[k][j])


## PROBLEM : 2
# slicing the matrix into n/2 based on length (even number of course)
def Matrix_Multiply_Recursive(A, B, C, n):
    if n == 1:
        C[0][0] += A[0][0] * B[0][0]
        return
    
    m = n // 2   #length [and width] of the matrix

    A11 = [row[:m] for row in A[:m]]
    A12 = [row[m:] for row in A[:m]]
    A21 = [row[:m] for row in A[m:]]
    A22 = [row[m:] for row in A[m:]]

    B11 = [row[:m] for row in B[:m]]
    B12 = [row[m:] for row in B[:m]]
    B21 = [row[:m] for row in B[m:]]
    B22 = [row[m:] for row in B[m:]]

    C11 = [row[:m] for row in C[:m]]
    C12 = [row[m:] for row in C[:m]]
    C21 = [row[:m] for row in C[m:]]
    C22 = [row[m:] for row in C[m:]]

    Matrix_Multiply_Recursive(A11, B11, C11, m)
    Matrix_Multiply_Recursive(A11, B12, C12, m)
    Matrix_Multiply_Recursive(A21, B11, C21, m)
    Matrix_Multiply_Recursive(A21, B12, C22, m)
    Matrix_Multiply_Recursive(A12, B21, C11, m)
    Matrix_Multiply_Recursive(A12, B22, C12, m)
    Matrix_Multiply_Recursive(A22, B21, C21, m)
    Matrix_Multiply_Recursive(A22, B22, C22, m)

    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j + m] = C12[i][j]
            C[i + m][j] = C21[i][j]
            C[i + m][j + m] = C22[i][j]



## PROBLEM 3
def Strassen_Multiplication(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
        return C

    m = n // 2  

    A11 = [row[:m] for row in A[:m]]
    A12 = [row[m:] for row in A[:m]]
    A21 = [row[:m] for row in A[m:]]
    A22 = [row[m:] for row in A[m:]]

    B11 = [row[:m] for row in B[:m]]
    B12 = [row[m:] for row in B[:m]]
    B21 = [row[:m] for row in B[m:]]
    B22 = [row[m:] for row in B[m:]]

    S1  = [[B12[i][j] - B22[i][j] for j in range(m)] for i in range(m)]
    S2  = [[A11[i][j] + A12[i][j] for j in range(m)] for i in range(m)]
    S3  = [[A21[i][j] + A22[i][j] for j in range(m)] for i in range(m)]
    S4  = [[B21[i][j] - B11[i][j] for j in range(m)] for i in range(m)]
    S5  = [[A11[i][j] + A22[i][j] for j in range(m)] for i in range(m)]
    S6  = [[B11[i][j] + B22[i][j] for j in range(m)] for i in range(m)]
    S7  = [[A12[i][j] - A22[i][j] for j in range(m)] for i in range(m)]
    S8  = [[B21[i][j] + B22[i][j] for j in range(m)] for i in range(m)]
    S9  = [[A11[i][j] - A21[i][j] for j in range(m)] for i in range(m)]
    S10 = [[B11[i][j] + B12[i][j] for j in range(m)] for i in range(m)]

    P1 = Strassen_Multiplication(A11, S1)
    P2 = Strassen_Multiplication(S2, B22)
    P3 = Strassen_Multiplication(S3, B11)
    P4 = Strassen_Multiplication(A22, S4)
    P5 = Strassen_Multiplication(S5, S6)
    P6 = Strassen_Multiplication(S7, S8)
    P7 = Strassen_Multiplication(S9, S10)

    C11 = [[0 for _ in range(m)] for _ in range(m)]
    C12 = [[0 for _ in range(m)] for _ in range(m)]
    C21 = [[0 for _ in range(m)] for _ in range(m)]
    C22 = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            C11[i][j] = P5[i][j] + P4[i][j] - P2[i][j] + P6[i][j]
            C12[i][j] = P1[i][j] + P2[i][j]
            C21[i][j] = P3[i][j] + P4[i][j]
            C22[i][j] = P5[i][j] + P1[i][j] - P3[i][j] - P7[i][j]

    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j + m] = C12[i][j]
            C[i + m][j] = C21[i][j]
            C[i + m][j + m] = C22[i][j]

    return C

    

##  TEST SECTION

# A = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 420]
# ]

# B = [
#     [1, 1, 1, 1],
#     [14, 14, 420, 14],
#     [17, 17, 17, 17],
#     [2, 2, 2, 2]
# ]


# C = [                   #used for the recursive
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]

# Matrix_Multiply_Recursive(A, B, C, 4)  #no return statement so no assignment for C like in strassen
# #C = Strassen_Multiplication(A, B)
# print(C)


def random_matrix(n):
    return [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

sizes = [32] 

for n in sizes:
    print(f"\nTiming for {n}x{n} matrices:\n")

    #lambda for a sort of generic object
    A = random_matrix(n)
    B = random_matrix(n)
    C = [[0 for _ in range(n)] for _ in range(n)]
    iteration_time = timeit.timeit(lambda: Matrix_Multiplication(A, B, C, n), number=1000)
    print("Iteration Time:", iteration_time)

    A = random_matrix(n)
    B = random_matrix(n)
    C = [[0 for _ in range(n)] for _ in range(n)]
    recursive_time = timeit.timeit(lambda: Matrix_Multiply_Recursive(A, B, C, n), number=1000)
    print("Recursive Time:", recursive_time)


    A = random_matrix(n)
    B = random_matrix(n)
    strassen_time = timeit.timeit(lambda: Strassen_Multiplication(A, B), number=1000)
    print("Strassen Time:", strassen_time)