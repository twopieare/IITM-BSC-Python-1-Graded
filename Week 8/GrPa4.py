def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps 

    Argument:
        n: integer
    Return:
        result: integer
    """
    if(n==0):
        return 1
    if(n<0):
        return 0
    return steps(n-1)+steps(n-2)+steps(n-3)
    
