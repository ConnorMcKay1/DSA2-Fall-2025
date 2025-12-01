import timeit

# Probided by Dr. Emily Kaplitz

setUp = '''
import random
import math
'''

insert ='''
def RandomArray():
    A = []
    for i in range(0,100):
        A.append(random.randint(0, 100))
    return A

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i -1
        A[i + 1] = key

A = RandomArray()
insertionSort(A)'''

selection ='''
def RandomArray():
    A = []
    for i in range(0,100):
        A.append(random.randint(0, 100))
    return A

def selectionSort(A):
    n = len(A)
    for i in range(0, n - 1): 
        smallest = i
        for j in range(i + 1, n):
            if A[j] < A[smallest]:
                smallest = j
        temp = A[i]
        A[i] = A[smallest]
        A[smallest] = temp
        
A = RandomArray()
selectionSort(A)'''

merge ='''
def RandomArray():
    A = []
    for i in range(0,100):
        A.append(random.randint(0, 100))
    return A

def mergeSort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)  
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j +1]

    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0

    for k in range(p, r +1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        
A = RandomArray()
mergeSort(A, 0 , len(A)-1)'''

print("Insertion Sort: ", timeit.timeit(setup = setUp, stmt = insert, number=10000))
print("Selection Sort: ", timeit.timeit(setup = setUp, stmt = selection, number=10000))
print("Merge Sort: ", timeit.timeit(setup = setUp, stmt = merge, number=10000))
