print("whoop whoop")

text = input("Enter the text you want to seach: ")
print('\t' + "===>" + text)
print('\n'+'\n')
pattern = input("Enter What you're looking for: ")
print('\t' + "===>" + pattern)


def Alignment(text, pattern, Alpha, Delta):


    m = len(pattern)
    n = len(text)


    #Declare A[0 . . . m][0... n]
    array = [[0 for j in range(n + 1)] for i in range(m + 1)]
    
    #Initialize A[i, 0]= i$\delta$ for each i
    for i in range(1, m + 1):
        array[i][0] = i*Delta
    #Initialize A[0, j]= j$\delta$ for each j
    for j in range(1, n + 1):
        array[0][j] = j*Delta



    for i in range(1, m+1):
        for j in range(1, n+1):

            Diagonal = 0 if pattern[i - 1] == text[j - 1] else Alpha

            #array[i][j] = min(Alpha*(array[i][j]) + min(i-1, j-1), Delta + min(i-1, j), Delta + min(i, j-1))
            array[i][j] = min((array[i - 1][j - 1] + Diagonal), (array[i - 1][j] + Delta), (array[i][j - 1] + Delta))



    return array[m][n]
        



def matrix():
    rows = 3
    cols = 2
    grid = [[range(cols)] for _ in range(rows)]
    print(grid)


'''
pulls text in
pulls pattern in
'''
Delta = 3
Alpha = 1
cost = Alignment(text, pattern, Delta, Alpha)

print(cost)



