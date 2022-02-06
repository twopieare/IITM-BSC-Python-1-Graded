'''
The transpose of a matrix swaps its rows and columns:
[[a,b,c], [d,e,f]]   ---->   [[a,d], [b,e], [c,f]]
Write a function named transpose that accepts a matrix mat as input and returns its transpose.
'''

def transpose(mat):
    """
    compute the transpose of the matrix

    Argument:
        mat: list of lists
    Return:
        mat_trans: list of lists
    """
    rez = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return rez
