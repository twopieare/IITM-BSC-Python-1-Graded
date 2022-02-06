'''
The range of a list of numbers is the difference between the maximum and minimum values in the list.

Write a function named get_range that accepts a list of real numbers as argument. It should return the range of the list.
'''

def get_range(L):
    """
    compute the range of a list L

    Argument:
        L: list
    Return:
        range: float
    """
    minimum = 999999
    maximum = 0
    rangeL = 0
    for x in L:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    rangeL = maximum - minimum
            
    return float(rangeL)
