'''
A n \times nn×n square matrix of positive integers is called a magic square if the following sums are equal:
(1) row-sum: sum of numbers in every row; there are nn such values, one for each row
(2) column-sum: sum of numbers in every column; there are nn such values, one for each column
(3) diagonal-sum: sum of numbers in both the diagonals; there are two values

There are n + n + 2 = 2n + 2n+n+2=2n+2 values involved. All these values must be the same for the matrix to be a magic-square.
'''

def is_magic(mat):
    """
    determine if a matrix is magic square

    Argument:
        mat: list of lists
    Return:
        string: 'YES' or 'NO'
    """
    
    n = len(mat)
    sumd1=0
    sumd2=0
    for i in range(n):
        sumd1+=mat[i][i]
        sumd2+=mat[i][n-i-1]
    if not(sumd1==sumd2):
        return "NO"
    for i in range(n):
        sumr=0
        sumc=0
        for j in range(n):
            sumr+=mat[i][j]
            sumc+=mat[j][i]
    if not(sumr==sumc==sumd1):
        return "NO"
    return "YES"
