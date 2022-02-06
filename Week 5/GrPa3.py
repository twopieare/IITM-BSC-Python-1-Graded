'''
The distance between two letters in the English alphabet is one more than the number of letters between them. Alternatively, it can be defined as the number of steps needed to move from the alphabetically smaller letter to the larger letter. This is always a non-negative integer. For example:

Letter-1	Letter-2	Letter-Distance
a	a	0
a	c	2
a	z	25
z	a	25
e	a	4
The distance between two words is defined as follows:

It is -1, if the words are of unequal lengths.
Write a function named distance that accepts two words as arguments and returns the distance between them.
'''

def distance(word_1, word_2):
    """
    compute distance between two words

    Arguments:
        word_1, word_2: strings
    Return:
        word_distance: int
    """
    wordis = 0;
    if(len(word_1) != len(word_2)):
        return -1
    for i in range(len(word_1)):
        wordis += abs(ord(word_1[i]) - ord(word_2[i]))
    return wordis
